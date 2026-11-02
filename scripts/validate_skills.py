"""Validate the repository's skill catalog. Run from any working directory."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently overwriting metadata."""


def unique_mapping(loader, node):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node)
    return mapping


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION = re.compile(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?")
LINK = re.compile(r"!?\[[^\]\n]*\]\(<?([^\s)>]+)>?(?:\s+\"[^\"]*\")?\)")
# Local machine paths must not be required to use a distributed skill.
MACHINE_PATH = re.compile(r"(?i)(?:\b[A-Z]:[\\/][^\s`<>]*|/(?:Users|home)/[^\s`<>]+)")


def read_yaml(text):
    return yaml.load(text, Loader=UniqueLoader)


def check_links(file, root, errors):
    text = file.read_text(encoding="utf-8")
    for target in LINK.findall(text):
        if re.match(r"^[A-Za-z]:[\\/]", target):
            errors.append(f"{file}: absolute local link: {target}")
            continue
        url = urlsplit(target)
        if url.scheme or url.netloc or not url.path:
            continue
        path = (file.parent / unquote(url.path)).resolve()
        if not path.is_relative_to(root.resolve()):
            errors.append(f"{file}: link leaves distribution: {target}")
        elif not path.exists():
            errors.append(f"{file}: broken link: {target}")


def validate(root):
    root = Path(root).resolve()
    errors = []
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        return ["skills/ directory is missing"]
    skills = sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not skills:
        errors.append("No skills found")
    readme = root / "README.md"
    catalog = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    if not catalog:
        errors.append("README.md is missing or empty")
    catalog_paths = set(LINK.findall(catalog))
    expected_paths = {f"skills/{p.name}/SKILL.md" for p in skills}
    listed_paths = {p for p in catalog_paths if re.fullmatch(r"skills/[^/]+/SKILL\.md", p)}
    if listed_paths != expected_paths:
        errors.append(f"README catalog mismatch: missing={expected_paths - listed_paths}, stale={listed_paths - expected_paths}")
    for skill in skills:
        try:
            entry = skill / "SKILL.md"
            text = entry.read_text(encoding="utf-8")
            match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
            if not match:
                raise ValueError("missing YAML frontmatter")
            data = read_yaml(match.group(1))
            if not isinstance(data, dict):
                raise ValueError("frontmatter must be a mapping")
            name = data.get("name")
            if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) >= 64 or name != skill.name:
                errors.append(f"{entry}: invalid name or directory mismatch")
            description = data.get("description")
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                errors.append(f"{entry}: description must contain 1-1024 characters")
            metadata = data.get("metadata")
            version = metadata.get("version") if isinstance(metadata, dict) else None
            if not isinstance(version, str) or not VERSION.fullmatch(version):
                errors.append(f"{entry}: metadata.version must be a quoted semantic version")
            if isinstance(version, str) and not re.search(
                rf"\|\s*\[{re.escape(skill.name)}\]\(skills/{re.escape(skill.name)}/SKILL\.md\)\s*\|\s*{re.escape(version)}\s*\|", catalog
            ):
                errors.append(f"{entry}: README catalog version is missing or outdated")
            for file in skill.rglob("*"):
                if file.is_symlink():
                    errors.append(f"{file}: symlinks are not supported")
                if file.suffix.lower() in {".md", ".yaml", ".yml"} and file.is_file():
                    content = file.read_text(encoding="utf-8")
                    if MACHINE_PATH.search(content):
                        errors.append(f"{file}: machine-specific absolute path")
                    if file.suffix.lower() == ".md":
                        check_links(file, skill, errors)
                    else:
                        parsed = read_yaml(content)
                        if not isinstance(parsed, dict):
                            errors.append(f"{file}: YAML must be a mapping")
            agent = skill / "agents/openai.yaml"
            if agent.is_file():
                data = read_yaml(agent.read_text(encoding="utf-8"))
                interface = data.get("interface") if isinstance(data, dict) else None
                if not isinstance(interface, dict):
                    errors.append(f"{agent}: missing interface mapping")
                else:
                    for field in ("display_name", "short_description", "default_prompt"):
                        if not isinstance(interface.get(field), str) or not interface[field].strip():
                            errors.append(f"{agent}: missing interface.{field}")
        except (OSError, ValueError, TypeError, yaml.YAMLError) as exc:
            errors.append(f"{skill}: {exc}")
    if readme.is_file():
        check_links(readme, root, errors)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("OK: skill metadata, resources, links and README catalog are valid.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
