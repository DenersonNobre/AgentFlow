# Epic: Gestão de Vendas

## Descrição
O momento da venda é o centro do negócio. O vendedor precisa registrar rápida e precisamente o que foi vendido, para quem e por quanto.

## Requisitos Funcionais (RF)
| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF001 | Vendedor inicia nova venda selecionando um cliente (ou venda avulsa) | Alta |
| RF002 | Vendedor adiciona produtos à venda com quantidade | Alta |
| RF003 | Vendedor ajusta quantidade e preço unitário de cada item | Alta |
| RF004 | Vendedor remove produtos da venda antes de finalizar | Alta |
| RF005 | Sistema calcula subtotal por item e total geral automaticamente | Alta |
| RF006 | Vendedor seleciona forma de pagamento (dinheiro/Pix/cartão/pendente) | Alta |
| RF007 | Vendedor finaliza a venda com confirmação | Alta |
| RF008 | Sistema persiste a venda e seus itens no SQLite | Alta |
| RF009 | Vendedor visualiza resumo da venda após finalizar | Média |
| RF010 | Vendedor cancela uma venda em andamento | Média |

## Critérios de Aceitação
| ID | Critério | Condição de Sucesso |
|----|----------|---------------------|
| CA001 | Venda sem cliente selecionado | Criada como "Consumidor Final" |
| CA002 | Adiciona 3 camisetas a R$ 29,90 | Subtotal R$ 89,70 |
| CA003 | Altera quantidade de 3 para 5 | Total recalculado |
| CA004 | Finaliza com forma "pendente" | status_pagamento = 'pendente' |
| CA005 | Finaliza sem internet | sync_status = 'pending' |
| CA006 | Cancela venda em andamento | Nada persistido |
| CA007 | Resumo exibe itens, valores e total | Dados conferem com o registrado |

## Tasks
- [ ] T01: Criar feature slice vendas/
- [ ] T02: Implementar models Venda e ItemVenda
- [ ] T03: Implementar VendasLocalDataSource (transação atômica)
- [ ] T04: Implementar VendasRemoteDataSource
- [ ] T05: Implementar VendasRepository
- [ ] T06: Criar VendasBloc (iniciar, adicionar, remover, ajustar, finalizar, cancelar)
- [ ] T07: Criar tela de seleção de cliente
- [ ] T08: Criar tela de itens da venda
- [ ] T09: Criar bottom sheet de seleção de produto
- [ ] T10: Criar bottom sheet de forma de pagamento
- [ ] T11: Criar tela de confirmação/resumo
- [ ] T12: Criar tela de venda finalizada
- [ ] T13: Implementar cálculo de totais em tempo real
- [ ] T14: Implementar rascunho automático
- [ ] T15: Registrar dependências no GetIt

## Dependências
- Epic "Gestão de Clientes"
- Epic "Gestão de Produtos"
- Epic "Autenticação e Sincronização"
