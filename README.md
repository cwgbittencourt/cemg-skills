# CEMG Skills

Catálogo pessoal de skills para o Codex. Instale somente as skills que quiser, em Windows, macOS ou Linux, sem copiar configurações de uma máquina para outra.

**Estado inicial:** estrutura preparada localmente para `cwgbittencourt/cemg-skills`. Os comandos de download abaixo dependem da publicação desse repositório no GitHub. Consulte [validação e pendências](docs/VALIDACAO.md).

## Catálogo

| Skill | Versão | Finalidade |
|---|---|---|
| [cemg-spec](skills/cemg-spec/SKILL.md) | 1.0.0 | Criar, revisar, atualizar e validar especificações de software usando o template CEMG. |
| [cemg-task-review](skills/cemg-task-review/SKILL.md) | 1.2.0 | Gerar roteiros de revisão de tasks e listar decisões humanas com rastreabilidade no Git. |

Cada pasta em `skills/` é uma unidade de instalação independente. Não é necessário instalar o catálogo inteiro.

## Requisitos

- Codex com suporte a skills pessoais.
- Acesso ao repositório no GitHub; se privado, autenticação com permissão de leitura.
- Python 3.11 ou superior para os comandos de terminal e para a validação deste catálogo.
- Git para a alternativa por clone e para a rastreabilidade de decisões da `cemg-task-review`.

O destino é `$CODEX_HOME/skills` quando `CODEX_HOME` está definido; caso contrário, `~/.codex/skills`. A instalação é feita por usuário e por máquina. Alterar arquivos no clone do catálogo não atualiza automaticamente uma cópia já instalada.

## Instalar uma skill pelo chat do Codex

Depois da publicação, envie no chat:

```text
$skill-installer instale a skill cemg-task-review do repositório cwgbittencourt/cemg-skills, caminho skills/cemg-task-review, branch main.
```

Essa é uma instrução para o Codex usar o instalador disponível no ambiente. Não é um comando de terminal. Se o instalador não estiver disponível, use a instalação manual abaixo.

## Instalar uma skill pelo terminal

Os exemplos usam o instalador que acompanha o Codex em `skills/.system/skill-installer`. Se esse arquivo não existir na sua distribuição, use a alternativa por clone.

### Windows — PowerShell

```powershell
$codexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$installer = Join-Path $codexDir 'skills/.system/skill-installer/scripts/install-skill-from-github.py'
python $installer --repo cwgbittencourt/cemg-skills --path skills/cemg-task-review
```

### macOS e Linux — Bash/Zsh

```bash
codex_dir="${CODEX_HOME:-$HOME/.codex}"
installer="$codex_dir/skills/.system/skill-installer/scripts/install-skill-from-github.py"
python3 "$installer" --repo cwgbittencourt/cemg-skills --path skills/cemg-task-review
```

### O que cada argumento faz

| Argumento | Função |
|---|---|
| `--repo cwgbittencourt/cemg-skills` | Seleciona o repositório de origem. |
| `--path skills/cemg-task-review` | Instala somente essa pasta e seus recursos. |
| `--ref main` | Seleciona a branch; `main` é o padrão. Também aceita tag ou commit. |
| `--dest CAMINHO` | Define outra pasta de destino; útil para testar sem alterar a instalação pessoal. |
| `--method auto` | Tenta download e, em situações de autenticação compatíveis, recorre ao Git. |
| `--method git` | Usa Git; útil quando o acesso ao repositório privado já está configurado no Git. |

Para fixar uma versão, acrescente `--ref cemg-task-review-v1.2.0` **somente depois que essa tag for publicada**. Hoje a versão `1.2.0` está declarada na skill; isso não significa que uma tag já exista no GitHub.

O instalador recusa um destino já existente. Para atualizar, siga a seção de atualização. A skill deve ficar disponível no próximo turno; se não aparecer, reinicie o Codex e confira o diretório de instalação.

## Instalação manual a partir de um clone

Depois da publicação:

```text
git clone https://github.com/cwgbittencourt/cemg-skills.git
cd cemg-skills
```

Se você já possui esta pasta local, execute os comandos de cópia a partir da raiz dela, sem clonar novamente.

### Windows — PowerShell

```powershell
$codexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$skillsDir = Join-Path $codexDir 'skills'
$destination = Join-Path $skillsDir 'cemg-task-review'
if (Test-Path -LiteralPath $destination) { throw 'A skill já existe. Siga a seção Atualizar.' }
New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null
Copy-Item -LiteralPath './skills/cemg-task-review' -Destination $destination -Recurse
```

### macOS e Linux — Bash/Zsh

```bash
codex_dir="${CODEX_HOME:-$HOME/.codex}"
destination="$codex_dir/skills/cemg-task-review"
if [ -e "$destination" ]; then
  printf '%s\n' 'A skill já existe. Siga a seção Atualizar.'
else
  mkdir -p "$codex_dir/skills"
  cp -R ./skills/cemg-task-review "$destination"
fi
```

Copie a pasta completa, incluindo `agents/`, `assets/` e `references/`. Não copie `packages/`, `.git/` nem o README para dentro da skill.

## Comandos da cemg-spec

Envie os comandos no **chat do Codex**, no projeto que será especificado:

| Comando | Finalidade |
|---|---|
| `$cemg-spec criar <demanda>` | Investigar a demanda e produzir uma especificação. |
| `$cemg-spec revisar <arquivo ou conteúdo>` | Apontar lacunas, contradições e correções propostas. |
| `$cemg-spec atualizar <spec> <mudanças>` | Incorporar mudanças preservando IDs e registrando impactos. |
| `$cemg-spec validar <spec>` | Avaliar a prontidão para implementação; aceita também “verificar prontidão”. |

A skill utiliza o modelo canônico incluído em sua pasta e classifica a spec como pronta, pronta com suposições explícitas ou bloqueada por decisões essenciais. Sua função é investigar e documentar; prontidão não significa implementação concluída.

Para instalar pelo chat após a publicação:

```text
$skill-installer instale a skill cemg-spec do repositório cwgbittencourt/cemg-skills, caminho skills/cemg-spec, branch main.
```

Nos exemplos de instalação pelo terminal, cópia manual e atualização deste README, substitua `cemg-task-review` por `cemg-spec` para selecionar esta skill.

## Comandos da cemg-task-review

Os comandos desta seção são enviados no **chat do Codex**, aberto no projeto que será revisado. Não os execute no terminal.

### Gerar e salvar uma revisão

```text
$cemg-task-review [001] T015
```

- `001`: prefixo da especificação em `specs/`, preservando zeros; colchetes são opcionais.
- `T015`: identificador da task em `tasks.md` daquela especificação.
- Também aceita o nome completo da pasta: `$cemg-task-review 001-entrega-validada T015`.

A skill analisa requisitos e implementação e salva o roteiro em `docs/validacao_humana/<pasta-da-spec>/T015.md`, preservando `Docs` quando esse for o padrão existente. Se já houver revisão, cria outra com data e hora, preservando a anterior.

O documento inicia com `PENDENTE DE REVISÃO HUMANA` e observações humanas vazias. A pessoa revisora altera manualmente `status` e `observacoes_humanas` e faz commit. A skill não aprova a task nem altera seu planejamento.

### Listar todas as revisões do projeto

```text
$cemg-task-review listar
```

Consulta os documentos existentes e o histórico local do Git. Mostra status, arquivo e, quando comprováveis no histórico, autor declarado, data e commit da última alteração dos campos humanos. Não cria uma nova revisão.

### Listar as revisões de uma especificação

```text
$cemg-task-review listar [001]
```

Filtra pelo prefixo ou nome da especificação. Não exige que a pasta original em `specs/` continue existindo.

### Aliases textuais

```text
/CEMG-task-review [001] T015
/CEMG-task-review listar
/CEMG-task-review listar [001]
```

Essas formas expressam a mesma intenção no chat. Não registram comandos nativos, atalhos de terminal ou itens de menu.

### Pré-requisitos e limites da revisão

A geração usa `specs/<spec>/tasks.md`, os requisitos e a implementação do projeto atual. Uma identificação ambígua exige esclarecimento. A listagem usa os documentos já salvos e o Git local; histórico ausente ou incompleto limita a atribuição da decisão. Autor declarado no Git não comprova identidade nem edição manual. Testes do projeto só são executados quando autorizados no pedido.

## Atualizar ou remover

Antes de atualizar, compare personalizações locais com a nova versão. Mova a instalação existente para um backup **fora de `skills/`**, e então instale a nova versão usando um dos métodos acima. O backup externo evita que duas cópias da skill sejam descobertas pelo Codex.

Para atualizar o clone do catálogo, use `git pull --ff-only` com a árvore de trabalho limpa. Isso não atualiza as skills pessoais: depois, repita a cópia ou o instalador.

Para remover de forma reversível, use o mesmo procedimento de mover para backup e não reinstale:

### Windows — PowerShell

```powershell
$codexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$source = Join-Path $codexDir 'skills/cemg-task-review'
$backupRoot = Join-Path $codexDir 'skill-backups'
$backup = Join-Path $backupRoot ('cemg-task-review-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff'))
if (-not (Test-Path -LiteralPath $source)) { throw 'Skill não instalada nesse destino.' }
if (Test-Path -LiteralPath $backup) { throw 'Backup já existe; escolha outro nome.' }
New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
Move-Item -LiteralPath $source -Destination $backup
```

### macOS e Linux — Bash/Zsh

```bash
codex_dir="${CODEX_HOME:-$HOME/.codex}"
source_dir="$codex_dir/skills/cemg-task-review"
if [ -d "$source_dir" ]; then
  mkdir -p "$codex_dir/skill-backups"
  backup_container="$(mktemp -d "$codex_dir/skill-backups/cemg-task-review.XXXXXX")"
  mv "$source_dir" "$backup_container/cemg-task-review"
else
  printf '%s\n' 'Skill não instalada nesse destino.'
fi
```

Se a nova instalação falhar, restaure a pasta do backup para o caminho original, desde que ele esteja livre. Não mescle versões automaticamente. Reinicie o Codex se a descoberta não refletir a alteração. As revisões em `docs/validacao_humana` pertencem aos projetos e permanecem disponíveis.

## Solução de problemas

| Problema | O que conferir |
|---|---|
| `Destination already exists` | Preserve a instalação existente conforme a seção de atualização. |
| Skill não aparece | Confira `CODEX_HOME`, a existência de `skills/cemg-task-review/SKILL.md` e se houve uma pasta extra ao extrair o ZIP. |
| Repositório não encontrado | Confirme a publicação, a URL e a permissão de leitura. |
| Repositório privado | Configure as credenciais Git da sua conta e tente `--method git`; o instalador também aceita `GH_TOKEN` ou `GITHUB_TOKEN` no ambiente. Não salve tokens neste repositório. |
| `python` não encontrado | Instale Python 3.11+ ou use `py -3` no Windows / `python3` no macOS e Linux. |
| Histórico de decisão insuficiente | Consulte a revisão em um clone com o histórico necessário; a skill não faz `fetch` automaticamente. |

## Adicionar e validar novas skills

1. Crie `skills/<nome-da-skill>/SKILL.md` com `name`, `description` e `metadata.version` entre delimitadores YAML `---`.
2. Use nome em minúsculas, números e hífens, igual ao da pasta, com menos de 64 caracteres.
3. Inclua recursos com links relativos internos à própria skill. Não dependa de caminhos da máquina de origem.
4. Adicione a skill e a versão à tabela do catálogo e documente cada comando nesta página.
5. Execute a validação e os testes antes de publicar.

```text
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

No macOS/Linux, substitua `python` por `python3` se necessário. A dependência PyYAML é usada apenas na manutenção; instalar a skill não exige instalar as dependências deste catálogo.

O GitHub Actions executa essas verificações em Windows, macOS e Linux. A validação cobre metadados, YAML, recursos, links, caminhos locais e o catálogo. Ela não comprova o julgamento da skill durante uma revisão real.

## Versões, pacotes e publicação

Cada skill mantém sua versão em `metadata.version`; o catálogo deve mostrar o mesmo valor. Use tags como `cemg-task-review-v1.2.0` para versões imutáveis publicadas de uma skill. Mudanças somente na documentação do catálogo não exigem mudar a versão da skill.

O pacote original foi preservado em [packages/cemg-task-review](packages/cemg-task-review), incluindo as instruções originais. A fonte de manutenção passa a ser a pasta descompactada em `skills/`; o ZIP original é histórico e não é atualizado automaticamente. Novos ZIPs de releases devem ser gerados a partir da fonte correspondente à tag.

Consulte o [procedimento de publicação](docs/PUBLICACAO.md) e o [registro de validação](docs/VALIDACAO.md).

## Licença

A licença de distribuição ainda não foi escolhida pelo titular. Este catálogo não concede, por enquanto, uma licença aberta de redistribuição. Defina a licença antes de disponibilizar o projeto publicamente.
