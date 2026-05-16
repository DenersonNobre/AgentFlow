# Epic: Gestão de Produtos

## Descrição
O vendedor ambulante trabalha com um catálogo de produtos. Esta epic cobre o cadastro, edição, exclusão e busca de produtos.

## Requisitos Funcionais (RF)
| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF001 | Vendedor cadastra produto com nome e preço | Alta |
| RF002 | Vendedor edita nome e/ou preço de um produto existente | Alta |
| RF003 | Vendedor remove um produto do catálogo | Média |
| RF004 | Vendedor busca produto pelo nome com autocomplete | Alta |
| RF005 | Vendedor visualiza lista de produtos ordenada por nome | Alta |
| RF006 | Vendedor duplica um produto existente | Baixa |

## Critérios de Aceitação
| ID | Critério | Condição de Sucesso |
|----|----------|---------------------|
| CA001 | Vendedor cadastra produto "Camiseta" por R$ 49,90 | Produto aparece no catálogo |
| CA002 | Vendedor altera preço de "Camiseta" para R$ 39,90 | Preço atualizado na lista |
| CA003 | Vendedor busca por "cam" e encontra "Camiseta" e "Camisa" | Lista filtrada em < 1s |
| CA004 | Vendedor tenta cadastrar produto sem nome | Campo exibe "Nome é obrigatório" |
| CA005 | Vendedor tenta cadastrar preço negativo | Campo exibe "Preço deve ser maior que zero" |

## Tasks
- [ ] T01: Criar feature slice produtos/
- [ ] T02: Implementar model Produto
- [ ] T03: Implementar ProdutosLocalDataSource
- [ ] T04: Implementar ProdutosRemoteDataSource
- [ ] T05: Implementar ProdutosRepository
- [ ] T06: Criar ProdutosBloc
- [ ] T07: Criar tela de listagem com search bar
- [ ] T08: Criar formulário de cadastro/edição
- [ ] T09: Implementar validações (nome obrigatório, preço > 0, duplicidade)
- [ ] T10: Registrar dependências no GetIt

## Dependências
- Epic "Autenticação e Sincronização"
