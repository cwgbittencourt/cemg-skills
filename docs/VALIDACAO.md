# Validação da preparação inicial

Data: 2026-11-02, fuso do usuário America/Sao_Paulo.

## Escopo

Uma skill encontrada: `cemg-task-review` versão `1.2.0`. Os quatro arquivos foram extraídos do pacote original sem alterações de conteúdo. O ZIP e as instruções de instalação originais foram preservados em `packages/cemg-task-review/`.

A preparação não instala skills no perfil pessoal nem modifica os projetos revisados por elas.

## Verificações

Executadas no Windows, com Python 3.11.5:

| Verificação | Resultado |
|---|---|
| Comparação binária com o ZIP original | Os quatro arquivos extraídos são idênticos aos originais. |
| `python scripts/validate_skills.py` | Aprovado: metadados, YAML, recursos, links e catálogo. |
| `python -m unittest discover -s tests -v` | Oito testes aprovados, incluindo recursos ausentes, YAML duplicado, nome divergente, catálogo desatualizado, caminho local e referência externa à skill. |
| `quick_validate.py` da skill-creator instalada | `Skill is valid!`, executado com Python em modo UTF-8. |
| Instalador oficial do Codex com fonte local | Instalação em diretório temporário aprovada; quatro arquivos idênticos, somente a skill escolhida instalada. |
| Instalação repetida no mesmo destino | Recusada pelo instalador; arquivos da primeira instalação preservados. |
| Exclusão de arquivos locais | `.vs/` ignorada pelo Git. |

No ensaio do instalador oficial, somente a obtenção do repositório (`_prepare_repo`) foi substituída pela pasta local. A resolução dos argumentos, a validação da pasta, a cópia e a recusa de sobrescrita usaram o código real do instalador. Esse ensaio não comprova acesso à rede, autenticação, download ou checkout de tags.

O Git foi inicializado na branch `main`. Neste volume, consultas do Git exigiram `-c safe.directory=E:/Projetos/cemg-skills` por ausência de informação de proprietário no sistema de arquivos; nenhuma configuração global foi alterada. Espaços finais em Markdown são preservados para as quebras de linha do modelo original.

A autenticação do GitHub CLI foi confirmada fora do sandbox na conta `cwgbittencourt`. O diagnóstico inicial de credencial inválida era limitado ao ambiente do sandbox.

## Pendências externas

- Escolher licença antes de uma eventual distribuição pública; a preparação para publicação usa repositório privado.
- Criar e publicar `cwgbittencourt/cemg-skills`; a consulta inicial ao conector retornou repositório não encontrado.
- Executar o workflow nas três plataformas depois da publicação.
- Testar download real do GitHub, instalação por tag e geração/listagem em um projeto de exemplo.

Comandos de instalação por GitHub no README ficam utilizáveis depois da publicação. A instalação por cópia da pasta local já pode ser usada.
