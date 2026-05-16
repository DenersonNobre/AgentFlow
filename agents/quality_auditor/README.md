# Auditor de Qualidade (Quality Auditor)

## Descrição
Agente responsável por realizar **análise estática** do código-fonte: lint, segurança, boas práticas e conformidade arquitetural.

## Papel
Realizar análise estática do código (lint, segurança, boas práticas).

## Acionamento
**Trigger:** `codigo_gerado` — disparado em **paralelo** com o Test Runner após o código ser gerado.

## Entradas
- `src/` — Código-fonte gerado.

## Saídas
- `quality-report.json` — Relatório de qualidade com violações estáticas, severidades e sugestões.

## Dependências
- **code_generator** — depende do código gerado (estático, **não depende de testes**).

## Exemplo de Uso
```bash
./scripts/run_agent.sh quality_auditor
```

## Configuração
Ver `config.yaml` para detalhes de configuração.
