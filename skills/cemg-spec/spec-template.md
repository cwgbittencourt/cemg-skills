# Especificação Técnica: [Nome do Projeto / Módulo / Funcionalidade]

> **Estado:** `[PRONTA PARA IMPLEMENTAÇÃO | PRONTA COM SUPOSIÇÕES EXPLÍCITAS | BLOQUEADA POR DECISÕES ESSENCIAIS]`  
> **Modo de Operação:** `[Criar | Revisar | Atualizar | Validar]`  
> **Data:** AAAA-MM-DD  
> **Autor/Agente:** [Nome do Autor ou Agente]

Este é o modelo canônico CEMG. Adapte as seções à demanda. Os campos entre colchetes devem ser preenchidos com evidências ou propostas identificadas; não são requisitos predefinidos. As pendências essenciais impedem a classificação de prontidão.

---

## 1. Resumo da Mudança e Problema
- **Contexto & Problema:** [Descrição concisa da dor do usuário ou limitação do sistema atual].
- **Resultado Desejado:** [Visão geral do comportamento final esperado].

## 2. Objetivos e Indicadores de Sucesso
- **Objetivo 1:** [Descrição do objetivo].
- **Métrica de Sucesso:** [Indicador quantitativo ou qualitativo verificável].

## 3. Escopo
### Dentro do Escopo
- [ ] Item 1
- [ ] Item 2

### Fora do Escopo
- [ ] Item explicitamente excluído 1

## 4. Contexto Atual e Evidências
- **Arquivos/Rotinas Relevantes:** [Caminhos de arquivos do projeto ou rotinas afetadas].
- **Evidências/Logs:** [Trecho de erro, stack trace ou comportamento atual verificado].

## 5. Usuários e Fluxos Principais
- **Atores:** [Ex: Usuário Autenticado, Administrador, Sistema Externo].
- **Fluxo Principal:**
  1. O usuário acessa...
  2. O sistema valida...
  3. A resposta é retornada...

## 6. Requisitos Funcionais (RF)
| ID | Descrição do Requisito | Prioridade |
|---|---|---|
| `RF-001` | O sistema deve [ação clara e verificável]. | Alta |
| `RF-002` | O sistema deve permitir [ação]. | Média |

## 7. Regras de Negócio
- **RN-001:** [Regra de negócio obrigatória].
- **RN-002:** [Restrição operacional].

## 8. Estados, Exceções e Mensagens de Erro
- **Fluxo de Exceção 1:** Caso [condição de falha], o sistema deve [comportamento] e retornar a mensagem `[CÓDIGO_ERRO]: "Mensagem amigável"`.

## 9. Requisitos Não Funcionais (RNF)
| ID | Categoria | Criterio Mensurável |
|---|---|---|
| `RNF-001` | Desempenho | [Meta de desempenho, carga e método de medição confirmados ou propostos para validação]. |
| `RNF-002` | Segurança | [Controle de acesso e condições de autorização aplicáveis ao projeto]. |

## 10. Dados, Persistência e Validações
- **Estrutura de Dados:** [Tabela / Coleção / Entidade].
- **Regras de Validação de Campos:**
  - `[campo]`: [obrigatoriedade, formato e validação definidos pelo domínio].
  - `[estado]`: [valores permitidos e transições confirmados].

## 11. Interfaces e Contratos de Integração
Endpoint e método: [confirmar contrato ou identificar como proposta].

```json
{
  "campo_entrada": "string",
  "valor": 100
}
```

## 12. Abordagem Técnica e Justificativa
- **Solução Proposta:** [Descrição da abordagem arquitetural].
- **Alternativas Consideradas:** [Por que outra solução foi descartada].

## 13. Impacto nos Componentes Existentes
- **Módulos Afetados:** [Lista de componentes que sofrerão alteração].
- **Risco de Regressão:** [Baixo/Médio/Alto] - [Estratégia para mitigar].

## 14. Segurança e Permissões
- **Permissões Necessárias:** [Papeis / Roles necessários].
- **Proteção de Dados:** [Tratamento de PII / Senhas / Tokens].

## 15. Compatibilidade, Migração e Reversão
- **Migração de Dados:** [Script de migration necessário / Não aplicável].
- **Plano de Rollback:** [Passos para reverter a alteração caso ocorra falha].

## 16. Critérios de Aceite (CA)
- **`CA-001` (Relacionado ao `RF-001`):**
  - **Dado** que o usuário está autenticado com papel `Admin`
  - **Quando** solicita a exportação do relatório
  - **Então** o sistema gera um arquivo CSV contendo os registros do período filtrado.

## 17. Estratégia de Testes
- **Testes Unitários:** [Casos a cobrir].
- **Testes de Integração:** [Cenários de API / Banco].
- **Testes de Borda:** [Valores limites, concorrência, payloads vazios].

## 18. Plano de Implementação (Focado em Agentes de IA)

### Etapa 1: [Nome da Etapa]
- **Objetivo:** [O que será construído].
- **ID da Tarefa:** `T-001`.
- **Requisitos Atendidos:** [IDs aplicáveis].
- **Dependências:** [Etapas ou condições anteriores].
- **Componentes:** [Caminhos confirmados ou módulos propostos, identificados como tal].
- **Instruções:** [Orientações específicas sem incluir código de produção integral].
- **Validação:** [Comando de teste ou verificação manual].
- **Critério de Conclusão:** [Condição para avançar].

## 19. Riscos, Suposições e Questões em Aberto
- **Suposição Explícita 01:** [Premissa de baixo risco assumida na ausência de definição do usuário].
- **Questão em Aberto 01:** [Apenas se houver bloqueio essencial].

## 20. Critérios de Conclusão (Definition of Done)
- [ ] Testes aplicáveis executados e aprovados durante a implementação; registrar resultados e limitações.
- [ ] Critérios de aceite `CA-001` a `CA-00N` validados.
- [ ] Documentação de API / Código atualizada.


## Rastreabilidade e Revisão da Spec

| Requisito | Critério de aceite | Teste proposto | Tarefa |
|---|---|---|---|
| [RF/RNF] | [CA] | [Cenário] | [T] |

- **Fatos confirmados:** [evidências].
- **Propostas e suposições:** [justificativa e impacto].
- **Pendências essenciais:** [decisões necessárias].
- **Estado final e justificativa:** [pronta, pronta com suposições ou bloqueada].
- **Histórico de atualização:** [mudanças relevantes e IDs afetados, quando aplicável].

Os itens de conclusão da implementação são critérios futuros; não os marque como cumpridos apenas porque a spec foi escrita.
