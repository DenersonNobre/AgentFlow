# Epic: Contas a Receber

## Descrição
Nem todo cliente paga na hora. O vendedor precisa controlar quem ainda deve, quanto e desde quando.

## Requisitos Funcionais (RF)
| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF001 | Vendedor visualiza lista de vendas com status "pendente" | Alta |
| RF002 | Vendedor filtra contas a receber por cliente | Média |
| RF003 | Vendedor ordena contas por data (mais antigas primeiro) | Média |
| RF004 | Vendedor marca uma venda como "paga" (baixa total) | Alta |
| RF005 | Vendedor registra pagamento parcial | Alta |
| RF006 | Vendedor visualiza valor total em aberto | Alta |
| RF007 | Vendedor visualiza valor total em aberto por cliente | Média |
| RF008 | Vendedor visualiza histórico de pagamentos de cada venda | Baixa |

## Critérios de Aceitação
| ID | Critério | Condição de Sucesso |
|----|----------|---------------------|
| CA001 | Acessa contas a receber | Apenas vendas pendentes aparecem |
| CA002 | Marca venda de R$ 50 como paga | Venda some da lista, total diminui |
| CA003 | Pagamento parcial de R$ 30 em venda de R$ 100 | "Recebido: R$ 30 — Restante: R$ 70" |
| CA004 | Duas baixas parciais (R$ 30 + R$ 70) | Venda marcada como paga |
| CA005 | Total em aberto | Soma correta das pendências |
| CA006 | Filtro por cliente "Maria" | Apenas vendas da Maria |

## Tasks
- [ ] T01: Criar feature slice contas_receber/
- [ ] T02: Implementar repositório filtrando VendasRepository
- [ ] T03: Criar ContasReceberBloc
- [ ] T04: Criar tela de listagem com totalizador
- [ ] T05: Implementar filtro por cliente
- [ ] T06: Criar bottom sheet de baixa de pagamento
- [ ] T07: Criar tela de detalhe com histórico
- [ ] T08: Implementar atualização de status_pagamento
- [ ] T09: Implementar cálculo de valor restante
- [ ] T10: Registrar dependências no GetIt

## Dependências
- Epic "Gestão de Vendas"
- Epic "Gestão de Clientes"
