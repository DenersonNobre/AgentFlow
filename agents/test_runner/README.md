# Executor de Testes (Test Runner)

## Descrição
Agente responsável por executar a suíte de testes automatizados e medir cobertura de código.

## Papel
Executar testes automatizados e medir cobertura.

## Acionamento
**Trigger:** `codigo_gerado` — disparado em **paralelo** com o Quality Auditor.

## Entradas
- `src/` — Código-fonte gerado.
- `src/tests/` — Testes unitários gerados pelo Code Generator.

## Saídas
- `test-report.json` — Relatório de execução dos testes.
- `coverage-report.json` — Relatório de cobertura de código.

## Dependências
- **code_generator** — depende do código e testes gerados.

## Exemplo de Uso
```bash
./scripts/run_agent.sh test_runner
```

## Configuração
Ver `config.yaml` para detalhes de configuração.
