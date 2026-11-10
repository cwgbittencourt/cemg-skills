"""Exercise failures that would make a published skill unusable."""

from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_skills import validate


ROOT = Path(__file__).resolve().parents[1]


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "skills", self.root / "skills")
        shutil.copy2(ROOT / "README.md", self.root / "README.md")
        for directory in ("docs", "packages"):
            shutil.copytree(ROOT / directory, self.root / directory)
        self.entry = self.root / "skills/cemg-task-review/SKILL.md"

    def test_catalog_is_valid(self):
        self.assertEqual([], validate(self.root))

    def test_missing_resource_fails(self):
        (self.entry.parent / "assets/task-review-template.md").unlink()
        self.assertTrue(any("broken link" in e for e in validate(self.root)))

    def test_name_mismatch_fails(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8").replace(
            "name: cemg-task-review", "name: wrong-name", 1), encoding="utf-8")
        self.assertTrue(any("directory mismatch" in e for e in validate(self.root)))

    def test_duplicate_yaml_keys_fail(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8").replace(
            "name: cemg-task-review", "name: cemg-task-review\nname: duplicate", 1), encoding="utf-8")
        self.assertTrue(any("duplicate YAML key" in e for e in validate(self.root)))

    def test_unlisted_skill_fails(self):
        shutil.copytree(self.entry.parent, self.root / "skills/another-skill")
        self.assertTrue(any("catalog mismatch" in e for e in validate(self.root)))

    def test_machine_path_fails(self):
        with self.entry.open("a", encoding="utf-8") as stream:
            stream.write("\nRequired: C:\\Users\\someone\\template.md\n")
        self.assertTrue(any("machine-specific" in e for e in validate(self.root)))

    def test_resource_outside_skill_fails(self):
        with self.entry.open("a", encoding="utf-8") as stream:
            stream.write("\n[External resource](../../README.md)\n")
        self.assertTrue(any("leaves distribution" in e for e in validate(self.root)))

    def test_outdated_catalog_version_fails(self):
        readme = self.root / "README.md"
        readme.write_text(readme.read_text(encoding="utf-8").replace(
            "| 1.2.1 |", "| 0.0.1 |"), encoding="utf-8")
        self.assertTrue(any("version is missing or outdated" in e for e in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
