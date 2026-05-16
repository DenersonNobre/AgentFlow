# Epic: Dashboard Financeiro

## Descrição
O vendedor precisa de uma visão rápida do seu negócio: quanto vendeu hoje, quanto tem a receber, desempenho recente.

## Requisitos Funcionais (RF)
| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF001 | Vendedor visualiza total vendido no dia | Alta |
| RF002 | Vendedor visualiza quantidade de vendas no dia | Alta |
| RF003 | Vendedor visualiza total recebido no dia | Alta |
| RF004 | Vendedor visualiza total a receber geral | Alta |
| RF005 | Vendedor visualiza vendas dos últimos 7 dias em lista | Média |
| RF006 | Vendedor visualiza gráfico de barras (últimos 7 dias) | Média |
| RF007 | Vendedor visualiza ranking de clientes | Baixa |
| RF008 | Vendedor visualiza forma de pagamento mais usada | Baixa |

## Critérios de Aceitação
| ID | Critério | Condição de Sucesso |
|----|----------|---------------------|
| CA001 | Abre o app e vê "Vendas hoje: R$ 350 — 5 vendas" | Valores conferem com SQLite |
| CA002 | Vê "A receber: R$ 120" | Soma correta das pendências |
| CA003 | Navega para últimos 7 dias | Lista com 7 linhas |
| CA004 | Gráfico de barras com 7 colunas | Altura proporcional ao valor |
| CA005 | Registra venda e volta ao dashboard | Números atualizados |
| CA006 | Dashboard é a primeira tela após login | Rota inicial /dashboard |

## Tasks
- [ ] T01: Criar feature slice dashboard/
- [ ] T02: Implementar DashboardRepository (agregações SQLite)
- [ ] T03: Criar DashboardBloc
- [ ] T04: Criar tela com cards (Vendas Hoje, Recebido Hoje, A Receber)
- [ ] T05: Criar seção "Últimos 7 dias"
- [ ] T06: Implementar gráfico de barras (fl_chart)
- [ ] T07: Adicionar pull-to-refresh
- [ ] T08: Implementar refresh automático ao voltar
- [ ] T09: Registrar dependências no GetIt
- [ ] T10: Configurar GoRouter para rota inicial /dashboard

## Dependências
- Epic "Gestão de Vendas"
- Epic "Contas a Receber"
