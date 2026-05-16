# Gerador de Código (Code Generator)

## Descrição
Agente responsável por implementar o código-fonte e seus respectivos testes unitários, seguindo a arquitetura definida e os requisitos interpretados.

## Papel
Implementar o código-fonte e testes unitários com base na arquitetura e requisitos.

## Acionamento
**Trigger:** `arquitetura_definida` — disparado após o Arquiteto concluir.

## Entradas
- `interpreted_requirements.json` — Requisitos estruturados.
- `docs/ARCHITECTURE.md` — Documento de arquitetura.
- `docs/TECH_STACK.md` — Stack tecnológico definido.

## Saídas
- `src/` — Código-fonte gerado seguindo os padrões definidos.
- `src/tests/` — Testes unitários gerados para cada funcionalidade.

## Dependências
- **architect** — depende da arquitetura definida.

## Exemplo de Uso
```bash
./scripts/run_agent.sh code_generator
```

## Configuração
Ver `config.yaml` para detalhes de configuração.
