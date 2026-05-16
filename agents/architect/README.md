# Arquiteto (Architect)

## Descrição
Agente responsável por definir a arquitetura do sistema com base nos requisitos interpretados, incluindo padrões arquiteturais, decisões técnicas e definição do stack tecnológico.

## Papel
Definir a arquitetura do sistema com base nos requisitos interpretados.

## Acionamento
**Trigger:** `requisitos_interpretados` — disparado após o Spec Reader concluir a interpretação.

## Entradas
- `interpreted_requirements.json` — Requisitos estruturados vindos do Spec Reader.

## Saídas
- `docs/ARCHITECTURE.md` — Documento de arquitetura com diagramas, padrões e decisões.
- `docs/TECH_STACK.md` — Definição do stack tecnológico.

## Dependências
- **spec_reader** — depende dos requisitos interpretados.

## Exemplo de Uso
```bash
# Execução manual após interpretação:
./scripts/run_agent.sh architect
```

## Configuração
Ver `config.yaml` para detalhes de configuração.
