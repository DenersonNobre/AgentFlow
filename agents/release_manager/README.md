# Release Manager Agent

## Descrição
Agente responsável por preparar e publicar a release do projeto após o gate de validação (testes + qualidade aprovados).

## Papel
Preparar e publicar a release do projeto.

## Acionamento
**Trigger:** `gate:validacao_completa` — acionado **após** Test Runner e Quality Auditor concluírem com sucesso.

## Entradas
- `quality-report.json` — Relatório de qualidade estática.
- `test-report.json` — Relatório de execução dos testes.
- `coverage-report.json` — Relatório de cobertura.
- `src/` — Código-fonte final.
- `docs/CHANGELOG.md` — Histórico de mudanças.

## Saídas
- `docs/CHANGELOG.md` (atualizado) — Histórico de mudanças.
- `docs/RELEASE_NOTES.md` — Notas de release.
- `artefatos/` — Pacote de release compilado/empacotado + checksum.

## Dependências
- **quality_auditor** — depende da aprovação de qualidade.
- **test_runner** — depende da aprovação dos testes.

## Exemplo de Uso
```bash
./scripts/run_agent.sh release_manager
```

## Configuração
Ver `config.yaml` para detalhes de configuração.
