# Learning Agent — Análise de Ciclo

## Métricas do Ciclo
```json
{
  "fases_executadas": [
    "setup_validator",
    "spec_reader",
    "architect",
    "code_generator",
    "test_runner",
    "quality_auditor",
    "release_manager",
    "learning_agent"
  ],
  "status_etapas": {
    "setup_validator": "concluido",
    "spec_reader": "concluido",
    "architect": "concluido",
    "code_generator": "concluido",
    "test_runner": "aguardando_ia",
    "quality_auditor": "aguardando_ia",
    "release_manager": "aguardando_ia",
    "learning_agent": "aguardando_ia"
  },
  "artefatos": [
    "config_do_projeto.json",
    "interpreted_requirements.json",
    "test-report.json",
    "quality-report.json",
    "release_manager_prompt.md",
    "learning_agent_prompt.md",
    "test_runner_prompt.md",
    "quality_auditor_prompt.md"
  ],
  "ciclo_iniciado": "2026-05-16T00:21:37.227960",
  "ciclo_concluido": "2026-05-16T12:15:25.790945"
}
```

## LEARNING.md Atual
# Lições Aprendidas

## Propósito
Registrar lições aprendidas durante o desenvolvimento do Venda Fácil para evitar repetição de erros e disseminar boas práticas.

## Quando Registrar
- Ao final de cada ciclo de release (Fase 4 do pipeline)
- Sempre que um bug crítico for identificado e corrigido
- Quando uma decisão técnica se mostrar particularmente acertada ou errada
- Quando o pipeline encontrar um problema de fluxo ou configuração

## Formato do Registro

### [Ciclo/Data] — Título Resumido
- **Categoria**: (processo | tecnologia | arquitetura | pipeline | gestão)
- **O que aconteceu**: Descrição objetiva do fato.
- **O que funcionou bem**: Práticas que trouxeram resultado positivo.
- **O que pode melhorar**: O que não saiu como esperado.
- **Causa raiz**: Por que aconteceu.
- **Mitigação/Correção**: O que foi feito para resolver.
- **Recomendação**: Como evitar no futuro.

---

## Registros

### [Ciclo 1 — 16/05/2026] — Geração de Código com 3 Agentes Paralelos
- **Categoria**: tecnologia
- **O que aconteceu**: O código Flutter das 6 features + core foi gerado por 3 task agents rodando em paralelo, cada um responsável por um subconjunto (core+auth, clientes+produtos, vendas+contas+dashboard).
- **O que funcionou bem**: A divisão por domínio evitou conflitos de merge. Cada agente gerou ~25 arquivos sem sobreposição. Contratos compartilhados (entidades) foram pré-definidos e respeitados por todos.
- **O que pode melhorar**: O `main.dart` ficou como template default — ninguém assumiu a integração. O `app_router.dart` teve placeholders "Em construção" porque cada agente não sabia das páginas dos outros.
- **Causa raiz**: Falta de um agente de integração/orquestração cross-slice no plano de geração.
- **Mitigação/Correção**: Agente UI/UX dedicado refatorou main.dart, router, theme, e conectou as injeções de dependência de todas as features.
- **Recomendação**: Incluir agente de integração (UI/UX) como etapa obrigatória após a geração paralela.

### [Ciclo 1 — 16/05/2026] — Exclusão Acidental de Arquivos do Pipeline
- **Categoria**: processo
- **O que aconteceu**: Ao criar o scaffold Flutter com `flutter create`, o comando sobrescreveu a raiz do projeto, removendo pipeline/, skills/, docs/ e project/.
- **O que funcionou bem**: O diretório `pipeline_modelo/` serviu como backup. Task agents restauraram cada diretório em paralelo.
- **O que pode melhorar**: O `flutter create` foi executado na raiz em vez de em `venda_facil/`.
- **Causa raiz**: O FLUTTER_DIR estava configurado como raiz no início; foi corrigido para `venda_facil/`.
- **Mitigação/Correção**: Restauração via task agents a partir do `pipeline_modelo/`. FLUTTER_DIR corrigido no `orchestrator.py`.
- **Recomendação**: Sempre usar `flutter create <subdir>` dentro de um monorepo. Validar FLUTTER_DIR antes de executar.

### [Ciclo 1 — 16/05/2026] — UI/UX: Temas, Responsividade e Shared Widgets
- **Categoria**: arquitetura
- **O que aconteceu**: App gerado sem tema escuro, sem suporte a orientação, com `Navigator.of(context)` conflitando com GoRouter.
- **O que funcionou bem**: FlexColorScheme + Google Fonts entregou tema claro/escuro elegante com pouco código. ShellRoute do GoRouter integrou bottom nav perfeitamente.
- **O que pode melhorar**: A formatação de dados brasileiros (telefone, CPF, moeda) não foi planejada na spec inicial.
- **Causa raiz**: Packages de tema e formatação não estavam no TECH_STACK.md nem no pubspec.yaml inicial.
- **Mitigação/Correção**: Adicionados `flex_color_scheme`, `google_fonts`, `brasil_fields`. Criado `Formatters` utility class. Criados 5 widgets compartilhados.
- **Recomendação**: Incluir UI/UX como agente fixo no pipeline (design_ui_ux.skill). Listar packages de formatação localizada no TECH_STACK.md.

### [Ciclo 1 — 16/05/2026] — Container de Testes de Integração com Supabase Local
- **Categoria**: infraestrutura
- **O que aconteceu**: Não havia ambiente para testes de integração com Supabase. O app dependia de uma instância remota para testar autenticação e sync.
- **O que funcionou bem**: Docker Compose com Postgres 16 + GoTrue + PostgREST rodou sem problemas. Schema SQL espelha o SQLite local.
- **O que pode melhorar**: Seed data precisa ser mantida em sincronia com o schema SQLite.
- **Causa raiz**: Ausência de configuração de ambiente de teste local no setup inicial.
- **Mitigação/Correção**: Criado `supabase/` com docker-compose.yaml, schema.sql, seed.sql, .env.local, setup.ps1. Criado `EnvConfig` para alternar entre local/remoto via --dart-define.
- **Recomendação**: Manter schema.sql sempre espelhando local_database.dart. Rodar `setup.ps1` como pré-requisito dos testes de integração.

### [Ciclo 1 — 16/05/2026] — Skills do Pipeline e .agents/skills/
- **Categoria**: pipeline
- **O que aconteceu**: Skills técnicas (Dart, Flutter, Supabase) em `.agents/skills/` foram importadas do GitHub via `skills-lock.json`. Skills do pipeline em `skills/` são markdown descritivo.
- **O que funcionou bem**: A separação entre skills de pipeline (orquestração) e skills técnicas (implementação) é clara e funcional.
- **O que pode melhorar**: A skill `design_ui_ux.skill` foi adicionada tardiamente, depois da geração de código.
- **Causa raiz**: UI/UX não foi planejado como etapa separada no pipeline inicial.
- **Mitigação/Correção**: Criada `skills/design_ui_ux.skill` e adicionada ao catálogo de agentes.
- **Recomendação**: A skill de UI/UX deve ser acionada imediatamente após a geração de código, antes dos testes.

### [Ciclo 1 — 16/05/2026] — Testes, Qualidade e Liberação do Gate
- **Categoria**: pipeline
- **O que aconteceu**: Pipeline estava bloqueado no gate `validacao_completa` porque `test-report.json` e `quality-report.json` não haviam sido gerados. Havia 139 testes passando + 1 widget_test falhando.
- **O que funcionou bem**: 139 testes unitários já passavam com mocktail puro (sem GetIt/Supabase). A separação entre testes unitários e de integração facilitou o debug.
- **O que pode melhorar**: Três bugs impediam a bateria completa: (1) `BlocProvider<AuthBloc>` faltando em main.dart, (2) rota `:id` de produtos sem builder em GoRouter 14.x, (3) Supabase.initialize() crashava em teste por causa de SharedPreferences não mockado.
- **Causa raiz**: App nunca foi testado com `flutter test` — códigos gerados por IA não foram validados end-to-end até este ciclo.
- **Mitigação/Correção**: Adicionado BlocProvider, fixado router, mockado SharedPreferences em setUpAll, movido integration_test para diretório separado.
- **Recomendação**: Executar `flutter test` e `flutter analyze` imediatamente após cada geração de código, antes de avançar no pipeline.

### [Ciclo 1 — 16/05/2026] — Fechamento do Ciclo: Release + Learning + Kanban + Commit
- **Categoria**: pipeline
- **O que aconteceu**: Pipeline retomado via `--resume` e os 4 passos finais executados sequencialmente: Release Manager, Learning Agent, Kanban Manager e Commit+PR.
- **O que funcionou bem**: O `docs/RESUME.md` forneceu contexto claro e checklist exato. O `state.json` já registrava corretamente a fase e etapa. O orquestrador `--resume` carregou do checkpoint certo. A geração de prompts (release_manager_prompt.md, learning_agent_prompt.md) pelo pipeline facilitou a execução automatizada.
- **O que pode melhorar**: O Learning Agent e o Kanban Manager não são agentes automáticos — dependem de IA externa para executar. O RESUME.md menciona `python pipeline/orchestrator.py --resume` mas o comando pula da fase 4 em diante, exigindo execução manual da Fase 3 (Release Manager) primeiro.
- **Causa raiz**: O pipeline foi projetado com `--resume` continuando da `fase_atual` (4), mas a ordem correta exige executar Fase 3 antes. A Fase 3 (gate) foi aprovada mas o Release Manager ficou como "aguardando_ia".
- **Mitigação/Correção**: Release Manager executado manualmente (bump versão, CHANGELOG, RELEASE_NOTES, tag). Learning Agent executado manualmente (entrada no LEARNING.md). Kanban atualizado manualmente. Commit+PR preparados.
- **Recomendação**: Rever a lógica do `--resume` para tratar corretamente fases com status `aguardando_ia` — deve retroceder à primeira fase não concluída em vez de pular para `fase_atual`. Ou alternativamente, o state.json de retomada deve ter `fase_atual: 3` quando o Release Manager está pendente.

### [Ciclo 1 — 16/05/2026] — QA Rigoroso: Política de 0 Alertas
- **Categoria**: pipeline
- **O que aconteceu**: O Quality Auditor aprovava o código mesmo com 4 warnings e 17 infos, desde que estivessem apenas em arquivos de teste. Isso gerava poluição visual no VS Code (16 problemas no painel).
- **O que funcionou bem**: Após endurecer a política para 0 erros, 0 warnings, 0 infos em QUALQUER arquivo, todos os 16 problemas foram corrigidos: unused imports removidos, `print` substituídos, `__` simplificados para `_`, `shared_preferences` adicionado como dev_dependency, `!` desnecessário removido.
- **O que pode melhorar**: O report antigo no quality-report.json dizia "aprovado" mesmo com alertas, o que era enganoso.
- **Causa raiz**: O prompt do Quality Auditor não especificava tolerância zero.
- **Mitigação/Correção**: Prompt do QA atualizado com regra explícita de 0 alertas. `quality_auditor_prompt.md` e geração dinâmica no `orchestrator.py` atualizados. `quality-report.json` refeito.
- **Recomendação**: Todo ajuste de workflow deve ser propagado para os docs apropriados (AGENTS.md, HANDOFF.md, WORKFLOW.md).

### [Ciclo 1 — 16/05/2026] — Documento de Retomada (RESUME.md)
- **Categoria**: processo
- **O que aconteceu**: Ao encerrar a sessão, não havia um ponto de retomada claro para a próxima IA. Era necessário reler todo o HANDOFF.md + pipeline state + logs para entender onde parou.
- **O que funcionou bem**: `state.json` já registrava a fase atual. Os prompts na pasta `pipeline/` já estavam preparados.
- **O que pode melhorar**: Faltava uma mensagem direta da IA anterior para a próxima, com o contexto exato do que fazer primeiro.
- **Causa raiz**: O pipeline não prevê uma etapa de "encerramento de sessão" com documentação de retomada.
- **Mitigação/Correção**: Criado `docs/RESUME.md` como ponto de retomada dedicado, com checklist e comandos exatos. Adicionada seção "Retomada" no HANDOFF.md.
- **Recomendação**: Incorporar a geração automática de RESUME.md como etapa opcional ao final de cada ciclo no pipeline (ex: `--generate-resume`).


## Instruções
Analise o ciclo completo do pipeline e registre lições aprendidas:
1. O que funcionou bem
2. O que pode melhorar
3. Próximos passos
4. Recomendações

Atualize project/docs/LEARNING.md com uma nova entrada.
