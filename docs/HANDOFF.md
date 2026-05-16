# Handoff Document — Venda Fácil

## Propósito
Este documento é o **ponto de entrada** para qualquer IA (ou humano) assumir o projeto Venda Fácil. Ele contém o estado atual, os próximos passos e as regras para dar continuidade.

## Estado Atual do Projeto
- **Projeto**: Venda Fácil — app mobile para vendedores ambulantes
- **Pipeline**: Orquestrador Python em `pipeline/orchestrator.py` — 10 agentes catalogados
- **Fase Atual**: Fase 2 (Testes + Qualidade) concluída — Gate `validacao_completa` liberado
- **Stack**: Flutter/Dart + sqflite + Supabase + flutter_bloc + GetIt + GoRouter + FlexColorScheme + Google Fonts + brasil_fields
- **Arquitetura**: Vertical Slice + Flutter Team Architecture + SOLID + Clean Code + Offline-First
- **Código Gerado**: 73 arquivos Dart (6 features + core/infra)
- **Cobertura de Pacotes**: flutter_bloc, get_it, go_router, sqflite, supabase_flutter, connectivity_plus, flutter_secure_storage, equatable, uuid, intl, fl_chart, flex_color_scheme, google_fonts, brasil_fields, mocktail
- **Testes**: 140 testes unitários passando (flutter test), 4 testes de integração em `integration_test/`
- **Qualidade**: flutter analyze — 0 erros em lib/ (apenas infos/warnings em testes/integração)
- **Pipeline**: `test-report.json` e `quality-report.json` gerados — gate `validacao_completa` liberado para Release Manager

## Fluxo de Execução
Cada fase do pipeline gera um prompt em `pipeline/` que deve ser executado por uma IA.

### Fase 0 — Setup Validator
Valida ambiente e gera `project/setup/config_do_projeto.json`.

```bash
python pipeline/orchestrator.py --fase 0
```

**Ação da IA**: Verifique se o ambiente está pronto (Flutter, Dart, Supabase).

### Fase 1a — Spec Reader
Lê PRD, SPEC e épicos em `project/specs/` e gera `pipeline/interpreted_requirements.json`.

```bash
python pipeline/orchestrator.py --resume
```

**Ação da IA**: Analise todos os documentos de especificação e produza o JSON consolidado.

### Fase 1b — Architect
Define arquitetura com base nos requisitos interpretados.

```bash
python pipeline/orchestrator.py --resume
```

**Ação da IA**: Atualize `project/docs/ARCHITECTURE.md` e `project/docs/TECH_STACK.md`.

### Fase 1c — Code Generator
Gera código-fonte seguindo a arquitetura definida.

```bash
python pipeline/orchestrator.py --resume
```

**Ação da IA**: Implemente venda_facil/lib/ e venda_facil/test/ com todas as features.

### Fase 1d — UI/UX Designer
Refatora interface com tema, shared widgets, navegação e formatação localizada.

```bash
python pipeline/orchestrator.py --resume
```

**Ação da IA**: Aplique `skills/design_ui_ux.skill`: temas claro+escuro (FlexColorScheme), shared widgets (AppShell, Loading, Error, Empty, Responsive), converta navegação para GoRouter, conecte DI de todas as features.

### Fase 2 — Validação (paralela)
Test Runner + Quality Auditor executam em paralelo.

```bash
python pipeline/orchestrator.py --resume
```

**Ação da IA**: Execute testes, verifique lint e qualidade.

### Fase 3 — Gate + Release Manager
Valida relatórios e prepara release.

```bash
python pipeline/orchestrator.py --resume
```

**Ação da IA**: Atualize versionamento, changelog e release notes.

### Fase 4 — Aprendizado
Learning Agent captura lições do ciclo.

```bash
python pipeline/orchestrator.py --resume
```

   **Ação da IA**: Analise o ciclo, registre lições em `docs/LEARNING.md`.

## Kanban — Acompanhamento Visual
3 boards mantidos pelo **Kanban Manager** (agente #9):
- `project/board_epics.md` — visão por épico
- `project/board_features.md` — visão por caso de uso
- `project/board_tasks.md` — visão por task (com status e pendências)

Os boards são atualizados ao final de cada fase do pipeline.

## Ambiente de Testes Local
Para testes de integração com Supabase:

```bash
# Subir containers (Postgres + GoTrue + PostgREST com seed data)
powershell -File supabase\setup.ps1

# Rodar app apontando para local
flutter run --dart-define=SUPABASE_URL=http://localhost:3001 --dart-define=SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIiLCJleHAiOjk5OTk5OTk5OTl9.anonymously-signed

# Derrubar containers
docker compose -f supabase\docker-compose.yaml down
```

## Correções Realizadas (Ciclo Atual)
1. **main.dart**: Adicionado `BlocProvider<AuthBloc>` ausente — SplashPage usava `context.read<AuthBloc>()` sem provider na árvore de widgets, causando crash em runtime.
2. **widget_test.dart**: Corrigido para inicializar `Supabase.initialize()` + `SharedPreferences.setMockInitialValues()` + registro mínimo em GetIt (`AppRouter`, `AuthRepository` mock, `AuthBloc` real). Avança timer do SplashPage (500ms) para evitar "Timer still pending".
3. **app_router.dart**: Rota `:id` de Produtos não tinha `builder`/`redirect` — GoRouter 14.x exige um dos três. Adicionado redirect para `/produtos/$id/editar`.
4. **Testes de integração**: Movidos de `test/integration/` para `integration_test/` (convenção Flutter). Adicionado `SharedPreferences.setMockInitialValues({})` para evitar `MissingPluginException` em ambiente de teste.
5. **Flutter analyze**: 0 erros em `lib/`. Apenas info/warning em arquivos de teste (print, unused imports de teste, dependências de teste).
6. **Pipeline**: `test-report.json` (flutter test --machine) e `quality-report.json` gerados — gate `validacao_completa` liberado.

## Sessão 16/05 (pós-PR)
1. **QA mais rigoroso**: Política alterada para **0 erros, 0 warnings, 0 infos** em QUALQUER arquivo. `quality_auditor_prompt.md` e `orchestrator.py` atualizados.
2. **16 issues do flutter analyze corrigidas**: unused imports removidos, `print` → removido, `__` → `_`, `shared_preferences` add como dev_dependency, `!` desnecessário removido.
3. **`integration_test/` movido para `test/integration/`**: Ajuste de localização dos testes de integração.

## Regras (CRÍTICAS)
1. **Commit/Push só após testes bem-sucedidos.** Nenhum código vai para `develop` ou `main` sem passar pelo gate `validacao_completa` (testes aprovados + qualidade aprovada).
2. Sempre verifique `pipeline/state.json` antes de começar.
3. Nunca modifique arquivos de pipeline manualmente (exceto state.json para marcar etapas).
4. Após cada ação da IA, atualize state.json executando o orquestrador.
5. Documente decisões técnicas em ADRs em `project/docs/ARCHITECTURE.md`.
6. Se encontrar um erro, registre em `docs/LEARNING.md` e corrija antes de prosseguir.
7. Após gerar código, execute a Fase 1d (UI/UX Designer) antes da Fase 2 (testes).
8. **Propague ajustes para todos os artefatos do fluxo.** Qualquer mudança feita no código, pipeline, política ou estrutura deve ser refletida nos arquivos de documentação do workflow (HANDOFF.md, AGENTS.md, WORKFLOW.md, LEARNING.md, RESUME.md, prompts e state.json). O orquestrador lê esses artefatos para tomar decisões — manter tudo sincronizado garante continuidade entre sessões.

## Retomada
Para retomar o projeto exatamente de onde parou, leia `docs/RESUME.md`.

## Contato
Projeto 100% IA-driven. Para reportar issues, consulte `docs/LEARNING.md`.
