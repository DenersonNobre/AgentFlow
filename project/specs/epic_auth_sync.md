# Epic: Autenticação e Sincronização

## Descrição
Todo vendedor precisa de uma conta segura para proteger seus dados e da capacidade de sincronizar automaticamente com a nuvem para nunca perder informações.

## Requisitos Funcionais (RF)
| ID | Requisito | Prioridade |
|----|-----------|------------|
| RF001 | Vendedor cria conta com email e senha | Alta |
| RF002 | Vendedor faz login na conta existente | Alta |
| RF003 | Sistema mantém sessão ativa mesmo após fechar o app | Alta |
| RF004 | Vendedor recupera dados da nuvem ao fazer login em novo dispositivo | Alta |
| RF005 | Sistema sincroniza dados automaticamente quando detecta internet | Alta |
| RF006 | Sistema mantém fila de operações pendentes (sync_log) | Alta |
| RF007 | Sistema exibe indicador visual de status da sincronização | Média |
| RF008 | Vendedor força sincronização manualmente (botão sync) | Média |
| RF009 | Sistema faz retry automático com backoff exponencial em caso de falha | Alta |

## Requisitos Não-Funcionais (RNF)
| ID | Requisito | Critério |
|----|-----------|----------|
| RNF001 | Autenticação com timeout de 10s e feedback visual | Usabilidade |
| RNF002 | Sincronização não bloqueia a UI (executa em isolate separado) | Performance |
| RNF003 | Sync engine não consome > 5% bateria por sessão | Eficiência |
| RNF004 | Dados do usuário isolados por RLS no Supabase | Segurança |
| RNF005 | Sessão persistente usando flutter_secure_storage | Segurança |

## Critérios de Aceitação
| ID | Critério | Condição de Sucesso |
|----|----------|---------------------|
| CA001 | Vendedor cria conta com email válido e senha > 6 caracteres | Conta criada, redirecionado para home |
| CA002 | Vendedor faz login em novo celular | Todos os dados são restaurados |
| CA003 | Vendedor registra venda offline, depois volta à internet | Venda aparece no Supabase em < 30s |
| CA004 | Indicador de sync mostra "pendente" quando há operações na fila | Bolinha vermelha visível no topo |
| CA005 | Vendedor tenta login com senha errada 3x | App exibe "Credenciais inválidas" |
| CA006 | App fechado e reaberto sem internet | Sessão mantida, app funcional offline |

## Tasks
- [ ] T01: Criar feature slice auth/ (data, domain, presentation, di)
- [ ] T02: Implementar AuthRemoteDataSource (Supabase Auth)
- [ ] T03: Implementar AuthRepository com session persistente
- [ ] T04: Criar AuthBloc (login, cadastro, logout, verificar sessão)
- [ ] T05: Criar tela de login
- [ ] T06: Criar tela de cadastro
- [ ] T07: Implementar splash screen que verifica sessão
- [ ] T08: Implementar fluxo de restauração de dados pós-login
- [ ] T09: Criar serviço SyncEngine em core/sync/
- [ ] T10: Implementar tabela sync_log no SQLite
- [ ] T11: Implementar push (local → Supabase) por lote
- [ ] T12: Implementar pull (Supabase → local) incremental
- [ ] T13: Implementar monitor de conectividade (connectivity_plus)
- [ ] T14: Implementar retry automático com backoff exponencial
- [ ] T15: Criar widget SyncIndicator (AppBar)
- [ ] T16: Implementar sync manual (botão "Sincronizar agora")
- [ ] T17: Registrar dependências no GetIt

## Dependências
- Projeto Flutter inicializado com GetIt, GoRouter, sqflite
- Supabase Auth configurado
