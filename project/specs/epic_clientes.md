# Epic: Gestão de Clientes

## Descrição
O vendedor precisa registrar seus clientes de forma rápida para associar vendas e controlar contas a receber.

## Requisitos Funcionais (RF)
| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF001 | Vendedor cadastra cliente com nome e telefone | Alta |
| RF002 | Vendedor adiciona observações ao cliente (opcional) | Média |
| RF003 | Vendedor edita dados de um cliente existente | Alta |
| RF004 | Vendedor remove um cliente | Média |
| RF005 | Vendedor busca cliente pelo nome ou telefone com autocomplete | Alta |
| RF006 | Vendedor visualiza lista de clientes ordenada por nome | Alta |
| RF007 | Vendedor visualiza histórico de vendas de um cliente específico | Média |
| RF008 | Vendedor visualiza total devido por cliente | Média |

## Critérios de Aceitação
| ID | Critério | Condição de Sucesso |
|----|----------|---------------------|
| CA001 | Vendedor cadastra cliente apenas com nome | Cliente salvo e aparece na lista |
| CA002 | Vendedor cadastra cliente com nome e telefone | Cliente salvo com ambos os campos |
| CA003 | Vendedor busca por "jo" e encontra "João" e "José" | Lista filtrada instantaneamente |
| CA004 | Vendedor tenta cadastrar cliente sem nome | Campo exibe "Nome é obrigatório" |
| CA005 | Vendedor tenta cadastrar cliente com telefone já existente | Alerta "Telefone já cadastrado" |
| CA006 | Vendedor acessa histórico de vendas de um cliente | Lista exibe últimas vendas com data, valor e status |

## Tasks
- [ ] T01: Criar feature slice clientes/
- [ ] T02: Implementar model Cliente com fromMap/toMap e toJson
- [ ] T03: Implementar ClientesLocalDataSource (CRUD sqflite + LIKE)
- [ ] T04: Implementar ClientesRemoteDataSource (CRUD Supabase)
- [ ] T05: Implementar ClientesRepository (local-first)
- [ ] T06: Criar ClientesBloc
- [ ] T07: Criar tela de listagem com search bar
- [ ] T08: Criar formulário de cadastro/edição
- [ ] T09: Criar tela de detalhe com histórico e total devido
- [ ] T10: Implementar validação de telefone duplicado
- [ ] T11: Registrar dependências no GetIt

## Dependências
- Epic "Autenticação e Sincronização" (sessão + sync engine)
