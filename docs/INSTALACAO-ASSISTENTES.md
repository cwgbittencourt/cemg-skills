# Instalação da cemg-task-review por assistente

A versão `1.2.1` incorpora a adaptação encontrada nas quatro instalações locais. A fonte de manutenção é única; não é necessário manter cópias específicas por assistente no catálogo.

```text
skills/
  cemg-spec/                       # skill independente, mantida sem alterações
  cemg-task-review/
    SKILL.md
    agents/openai.yaml             # metadados de interface do Codex
    assets/task-review-template.md
    references/decisao-git.md
packages/cemg-task-review/          # pacote histórico 1.2.0, preservado
```

Copie sempre a pasta completa da skill. `agents/openai.yaml` é específico do Codex; sua presença não configura comandos nos demais assistentes. O template e as referências não dependem desse arquivo.

## Destinos globais

`~` representa a pasta pessoal do usuário. Instale apenas nos assistentes desejados.

| Assistente | Pasta que recebe `cemg-task-review/` | Acionamento |
|---|---|---|
| Codex | `$CODEX_HOME/skills` ou `~/.codex/skills` | `$cemg-task-review [001] T002` |
| Claude Code | `~/.claude/skills` | `/cemg-task-review [001] T002` |
| Google Antigravity | `~/.gemini/config/skills` | Pedido em linguagem natural mencionando a skill |
| Kiro IDE e CLI | `~/.kiro/skills` | Pedido em linguagem natural mencionando a skill |

Os destinos seguem as documentações oficiais de [Claude Code](https://code.claude.com/docs/en/skills), [Antigravity](https://antigravity.google/docs/skills) e [Kiro](https://kiro.dev/docs/skills/). No Kiro, agentes personalizados podem precisar incluir `skill://~/.kiro/skills/*/SKILL.md` em `resources`, conforme a documentação. Não altere configurações de agentes que não utiliza.

## Obter a fonte

Com acesso autenticado ao repositório:

```text
git clone https://github.com/cwgbittencourt/cemg-skills.git
cd cemg-skills
```

Se o clone já existe, use-o. Para atualizar, com a árvore de trabalho limpa, execute `git pull --ff-only`. As instruções abaixo copiam a versão desse clone; a adaptação precisa estar publicada para chegar por download a outra máquina. A tag `cemg-task-review-v1.2.0` permanece histórica.

## Windows — PowerShell

Execute na raiz do clone. Escolha um destino por execução:

```powershell
$skillName = 'cemg-task-review'
$assistantName = 'claude' # codex, claude, antigravity ou kiro
$codexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$destinations = @{
    codex = Join-Path $codexDir 'skills'
    claude = Join-Path $HOME '.claude/skills'
    antigravity = Join-Path $HOME '.gemini/config/skills'
    kiro = Join-Path $HOME '.kiro/skills'
}
if (-not $destinations.ContainsKey($assistantName)) { throw 'Assistente inválido.' }
$source = Join-Path (Get-Location) "skills/$skillName"
if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md'))) { throw 'Execute na raiz do catálogo.' }
$skillsDir = $destinations[$assistantName]
$destination = Join-Path $skillsDir $skillName
if (Test-Path -LiteralPath $destination) { throw 'A skill já existe. Preserve um backup antes de atualizar.' }
New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null
Copy-Item -LiteralPath $source -Destination $destination -Recurse
Get-ChildItem -LiteralPath $destination -Recurse -File
```

Repita alterando `$assistantName` para instalar nos demais assistentes. A operação não instala o catálogo inteiro.

## macOS e Linux — Bash/Zsh

Execute na raiz do clone e escolha o assistente:

```bash
install_cemg_review() {
  assistant_name="$1"
  case "$assistant_name" in
    codex) skills_dir="${CODEX_HOME:-$HOME/.codex}/skills" ;;
    claude) skills_dir="$HOME/.claude/skills" ;;
    antigravity) skills_dir="$HOME/.gemini/config/skills" ;;
    kiro) skills_dir="$HOME/.kiro/skills" ;;
    *) printf '%s\n' 'Assistente inválido.'; return 1 ;;
  esac
  source_dir='./skills/cemg-task-review'
  destination="$skills_dir/cemg-task-review"
  if [ ! -f "$source_dir/SKILL.md" ]; then
    printf '%s\n' 'Execute na raiz do catálogo.'; return 1
  fi
  if [ -e "$destination" ] || [ -L "$destination" ]; then
    printf '%s\n' 'A skill já existe. Preserve um backup antes de atualizar.'; return 1
  fi
  mkdir -p "$skills_dir" || return 1
  cp -R "$source_dir" "$destination" || return 1
  printf 'Instalada em %s\n' "$destination"
}
install_cemg_review claude
```

Troque `claude` por `codex`, `antigravity` ou `kiro` conforme necessário.

## Atualizar ou remover

Compare personalizações antes de atualizar. Mova a instalação antiga para uma pasta de backup fora dos diretórios de descoberta de skills, preservando todos os arquivos; depois repita a instalação. Não mescle as versões. Para remover de forma reversível, mantenha somente o backup. O README contém exemplos de backup para Codex; para os demais, use a raiz pessoal do respectivo assistente e uma pasta `skill-backups` fora de `skills`.

## Conferir e usar

Abra uma nova sessão no assistente, no projeto que contém `specs/<spec>/tasks.md`. Confira a descoberta da skill na interface disponível. No Antigravity, a documentação indica o menu Customizations; no Claude Code, confira `/cemg-task-review`. A existência dos quatro arquivos confirma a cópia, mas não comprova ativação ou execução funcional.

No Codex:

```text
$cemg-task-review [001] T002
$cemg-task-review listar
$cemg-task-review listar [001]
```

No Claude Code:

```text
/cemg-task-review [001] T002
/cemg-task-review listar
/cemg-task-review listar [001]
```

No Antigravity e no Kiro, ou como alternativa nos demais:

```text
Use a skill cemg-task-review para revisar a task T002 da spec 001.
Use a skill cemg-task-review para listar as revisões existentes.
Use a skill cemg-task-review para listar as revisões da spec 001.
```

Os identificadores são exemplos; use uma spec e uma task reais do projeto. A geração salva o roteiro em `docs/validacao_humana/<spec>/T002.md`, preservando `Docs` quando aplicável. A listagem consulta os documentos e o Git local. A skill não aprova a task nem executa testes do projeto sem autorização.

Não foi executado um ensaio funcional dentro dos quatro assistentes durante esta integração. Os comandos com barra e `$ARGUMENTS` dependem do cliente; copiar a pasta não garante menus ou atalhos em todos eles.
