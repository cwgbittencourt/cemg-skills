# Exemplo de entrega: cemg-spec

Este documento é uma demonstração escrita para o catálogo. Não é uma especificação de uma funcionalidade deste repositório nem um registro de execução automática da skill. A estrutura foi adaptada do template canônico para uma demanda pequena.

[Voltar ao catálogo](../../README.md)

## Pedido que originaria a especificação

```text
$cemg-spec criar uma função Python para cadastrar tarefas em uma lista em memória.
O título deve ser texto e não pode ficar vazio após remover espaços das extremidades.
Cada tarefa nova começa com concluida=false. Não quero banco nem interface nesta etapa.
Salve a especificação em docs/especificacao-cadastro-tarefas.md.
```

O caminho acima é o destino solicitado no projeto do usuário. O arquivo que você está lendo é uma prévia da entrega. A gravação da spec depende do destino autorizado; a skill também pode entregar a especificação no chat quando nenhum destino estiver definido.

---

# Especificação Técnica: cadastro de tarefas em memória

**Estado:** PRONTA COM SUPOSIÇÕES EXPLÍCITAS  
**Modo:** Criar  
**Data:** 2026-11-02  
**Origem:** exemplo didático do catálogo CEMG Skills

## 1. Problema, objetivo e escopo

O programa precisa adicionar tarefas sem aceitar títulos sem conteúdo. A entrega deve oferecer uma função Python que recebe um título e uma lista, adiciona uma tarefa válida e retorna o registro criado.

Estão no escopo a validação do título, a remoção de espaços das extremidades e o estado inicial `concluida=False`. Banco, interface, identificação por ID, exclusão e conclusão de tarefas ficam fora desta etapa, conforme a delimitação do exemplo.

O sucesso será verificado pelo comportamento de cadastro e pela preservação da lista quando o título for inválido; não foi solicitada uma meta de desempenho.

## 2. Contexto e decisões

Este cenário começa sem aplicação existente. `cadastro_tarefas.py` é o nome proposto para o módulo; não é uma convenção inferida de um projeto real. O pedido confirma armazenamento em memória e ausência de interface.

**Suposições de baixo risco:** títulos iguais são permitidos e não há tamanho máximo nesta etapa. A lista recebida é uma lista Python válida, pertencente ao chamador. Essas premissas ficam explícitas para revisão e precisam ser reconsideradas se o contexto mudar.

## 3. Requisitos e regras

| ID | Requisito ou regra | Origem |
|---|---|---|
| RF-001 | Adicionar uma tarefa com título válido à lista recebida e retornar a tarefa criada. | Pedido e contrato proposto. |
| RF-002 | Recusar títulos inválidos sem modificar a lista. | Regra do pedido; preservação da lista explicitada no contrato. |
| RN-001 | O título deve ser uma string com conteúdo após `strip()`. | Pedido. |
| RN-002 | Armazenar o título sem espaços nas extremidades. | Normalização explicitada para este exemplo. |
| RN-003 | Toda tarefa nova deve começar com `concluida=False`. | Pedido. |

## 4. Contrato, fluxo e erros

Contrato proposto: `adicionar_tarefa(titulo, tarefas)` recebe o título e uma lista mutável de tarefas. Retorna um dicionário com `titulo` e `concluida`, que também é acrescentado à lista. Não há cópia independente do objeto retornado: ele é o mesmo objeto inserido.

O fluxo valida o título antes de alterar a lista. Título inválido levanta `ValueError("Informe um título não vazio.")`. Título válido é normalizado, recebe o estado inicial e é inserido. A validação também recusa valores que não sejam strings, sem chamar `strip()` nesses valores.

O formato dos erros e a divisão em funções são propostas técnicas deste exemplo. Não há requisitos de rede, migração ou permissões de usuários nesta função isolada. Ela não deve ser apresentada como controle de segurança de uma aplicação completa.

## 5. Critérios de aceite

| ID | Dado / Quando / Então |
|---|---|
| CA-001 | Dada uma lista vazia, quando cadastrar `"  Estudar Git  "`, então adicionar exatamente `{"titulo": "Estudar Git", "concluida": False}` e retornar esse registro. |
| CA-002 | Dada uma lista com tarefas, quando cadastrar `"   "` ou `""`, então levantar o erro definido e preservar o conteúdo anterior da lista. |
| CA-003 | Dada uma lista válida, quando cadastrar `None` ou um número como título, então levantar o mesmo erro de validação e preservar a lista. |

## 6. Plano e rastreabilidade

| Task | Objetivo | Requisitos e regras | Aceite | Validação proposta |
|---|---|---|---|---|
| T001 | Implementar cadastro e validação no módulo proposto. | RF-001, RF-002, RN-001 a RN-003 | CA-001 a CA-003 | Casos de cadastro válido, normalização, título vazio e tipo inválido. |

T001 não depende de banco nem de serviços externos. Seu critério de conclusão é entregar o contrato descrito e registrar os resultados dos testes dos três critérios de aceite. Esses testes estão **planejados**, não executados por esta especificação.

## 7. Riscos, conclusão e prontidão

O armazenamento em memória perde dados ao encerrar o programa; isso é coerente com o escopo solicitado. A referência compartilhada entre retorno e lista deve ser compreendida pelo chamador. Persistência e cópia independente exigiriam uma mudança explícita de requisitos.

- [ ] Implementação entregue e revisada.
- [ ] Critérios CA-001 a CA-003 testados, com resultados registrados.
- [ ] Suposições revistas se surgirem regras sobre duplicidade ou tamanho.

**PRONTA COM SUPOSIÇÕES EXPLÍCITAS:** o comportamento principal e os erros estão definidos; as premissas sobre duplicidade e tamanho são de baixo risco neste cenário didático. Esta classificação não declara implementação concluída.

---

## Outros pedidos úteis para esta mesma spec

| Intenção | Pedido no chat | Tipo de resultado |
|---|---|---|
| Encontrar lacunas | `$cemg-spec revisar docs/especificacao-cadastro-tarefas.md` | Achados e propostas de ajuste; não reescreve automaticamente o arquivo. |
| Incorporar uma nova regra | `$cemg-spec atualizar docs/especificacao-cadastro-tarefas.md para limitar títulos a 100 caracteres e preservar os IDs existentes` | Spec atualizada, com impactos nos requisitos, aceite e testes. |
| Avaliar prontidão | `$cemg-spec validar docs/especificacao-cadastro-tarefas.md` | Classificação justificada, lacunas e decisões necessárias. |

Esses pedidos são alternativas de uso, não ações executadas nesta demonstração. A nova regra de 100 caracteres não faz parte da especificação acima nem do código demonstrativo.

Depois de implementar uma task em um projeto com a estrutura de specs e tasks, veja como a [cemg-task-review apresenta o entendimento da entrega](cemg-task-review.md). As duas skills não exigem uma instalação conjunta.
