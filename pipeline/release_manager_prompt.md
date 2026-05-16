# Release Manager Prompt

## Gate Aprovado
- test-report.json: OK
- quality-report.json: OK

## CHANGELOG.md Atual
# Histórico de Mudanças

## Convenções
- Formato baseado em [Keep a Changelog](https://keepachangelog.com/).
- Versionamento segue [SemVer 2.0](https://semver.org/).
- Commits seguem [Conventional Commits](https://www.conventionalcommits.org/).

## Registros

### [1.1.0] - 2026-05-16
### Adicionado
- 140 testes unitários passando (mocktail, sem dependências externas)
- Testes de widget para SplashPage, LoginPage e widget_test principal
- `BlocProvider<AuthBloc>` em main.dart corrigindo crash do SplashPage
- Pipeline de CI: `python pipeline/orchestrator.py --resume`
- `docs/RESUME.md` como ponto de retomada entre sessões
- Gate `validacao_completa` com aprovação automática (testes OK + qualidade OK)

### Alterado
- Versão bumpada de `1.0.0` para `1.1.0` (release menor com funcionalidades completas)
- `app_router.dart`: rota `:id` de produtos recebeu builder/redirect para GoRouter 14.x
- Testes de integração movidos de `test/integration/` para `integration_test/` (convenção Flutter)
- `widget_test.dart`: inicializa Supabase + SharedPreferences mock + GetIt mínimo; avança timer 500ms do SplashPage

### Corrigido
- `flutter analyze` agora com 0 erros em lib/
- SplashPage crashava sem `BlocProvider<AuthBloc>`
- GoRouter 14.x exigia builder explícito para rotas com parâmetro `:id`
- `Supabase.initialize()` crashava em teste por SharedPreferences não mockado
- Pipeline bloqueado no gate por falta de `test-report.json` e `quality-report.json`

### [0.1.0] - 2026-05-16
### Adicionado
- Geração de código completa: 73 arquivos Dart (6 features + core)
- Tema claro/escuro com FlexColorScheme (seed verde) + Google Fonts Inter
- 5 widgets compartilhados: AppShell, LoadingWidget, ErrorWidgetCustom, EmptyStateWidget, ResponsiveLayout
- Utilitário de formatação brasileira: `Formatters` (moeda, telefone, CPF, CNPJ, CEP, data)
- Skill `design_ui_ux.skill` para agente de interface
- Docker Compose para testes de integração local (Postgres + GoTrue + PostgREST)
- Schema SQL e seed data para Supabase local
- `EnvConfig` para alternar entre local/remoto via `--dart-define`
- Pacotes: `flex_color_scheme`, `google_fonts`, `brasil_fields`

### Alterado
- `main.dart` reescrito com `MaterialApp.router`, temas, DI completo
- `app_router.dart` reescrito com `ShellRoute` + `AppShell` e páginas reais
- `app_theme.dart` com darkTheme usando FlexColorScheme
- `injection_container.dart` conecta todas as 6 features
- Navegação de todas as páginas convertida de `Navigator.of(context)` para GoRouter
- Path do LEARNING.md corrigido de `project/docs/` para `docs/`

### Corrigido
- `main.dart` estava como template default do Flutter (counter app)
- Rotas tinham placeholders "Em construção"
- Navegação usava Navigator nativo conflitando com GoRouter
- FLUTTER_DIR apontava para raiz em vez de `venda_facil/`
- Learning Agent referenciava caminho errado do LEARNING.md

---

*Última atualização: 2026-05-16*


## Instruções
Analise as mudanças, incremente a versão (SemVer), atualize CHANGELOG.md e gere RELEASE_NOTES.md.
