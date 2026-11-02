# Publicação e manutenção

Destino publicado: `cwgbittencourt/cemg-skills`, privado. A tag e a release `cemg-task-review-v1.2.0` foram publicadas em 2026-11-02. Os procedimentos abaixo documentam como reproduzir a preparação em outro repositório e manter futuras versões; não execute novamente os comandos de criação para este repositório.

## Primeira publicação

1. Defina a licença com o titular e adicione `LICENSE`. Defina se o repositório será público ou privado.
2. Execute a validação e os testes descritos no README.
3. Confira `git status --short` e `git diff --check`. A pasta `.vs/` deve estar ignorada.
4. Autentique o GitHub CLI, caso necessário, com `gh auth login`.
5. Crie o primeiro commit com os arquivos revisados.
6. Crie o repositório na conta `cwgbittencourt`. Os exemplos abaixo usam acesso privado para preparação; publicar abertamente exige definir a licença e a visibilidade desejadas.

```text
git add .
git commit -m "Prepare installable skill catalog"
gh repo create cwgbittencourt/cemg-skills --private --source . --remote origin --push
```

Esses comandos são uma sequência de publicação, não um registro de comandos já executados. Se o repositório ou o remoto já existirem, inspecione o histórico e a configuração antes de usar o procedimento; não force o push nem substitua conteúdo existente.

7. Confira a execução do workflow `Validate skills` nas três plataformas.
8. Teste o instalador real com `--dest` apontando para uma pasta temporária vazia, primeiro em `main` e depois na tag publicada.
9. Atualize o aviso inicial e o registro de validação com os resultados reais.

## Release de uma skill

Use uma tag específica por skill. Para a versão inicial preservada:

```text
git tag -a cemg-task-review-v1.2.0 -m "cemg-task-review 1.2.0"
git push origin cemg-task-review-v1.2.0
gh release create cemg-task-review-v1.2.0 packages/cemg-task-review/cemg-task-review-1.2.0.zip --title "cemg-task-review 1.2.0" --notes "Skill original preservada; instalação individual documentada no README."
```

Antes de publicar o ZIP original, confira que os quatro arquivos ainda são idênticos aos da tag. Para versões futuras, gere um novo pacote contendo somente `<nome-da-skill>/` e seus recursos, a partir do commit da release, e não reutilize o ZIP antigo. Registre mudanças de comportamento nas notas da release.

## Política de versão

- Correção compatível: incremente o patch (`1.2.0` → `1.2.1`).
- Nova capacidade compatível: incremente o minor (`1.2.0` → `1.3.0`).
- Mudança incompatível de comandos ou contrato: incremente o major (`1.2.0` → `2.0.0`).
- Atualize a tabela do README no mesmo commit do metadado da skill.
- Não mova tags já publicadas para outro commit.

## Validação funcional pendente

Em um projeto de exemplo com `specs/<spec>/tasks.md`, requisitos e código, peça uma geração e confira o destino, as evidências e os campos humanos iniciais. Edite manualmente os campos humanos, faça commit e peça a listagem. Confira se uma edição posterior somente no corpo preserva a atribuição da decisão anterior e se uma alteração humana não commitada aparece como local. Isso verifica comportamento do agente; os testes do catálogo não substituem esse ensaio.
