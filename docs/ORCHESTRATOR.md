# Manual do Orquestrador

## Visão Geral
O orquestrador coordena a execução dos agentes no pipeline, gerenciando fluxos paralelos (fan-out) e pontos de sincronização (gates).

## Agentes e Triggers

| Agente | Trigger | Execução | Depende de |
|--------|---------|----------|------------|
| Spec Reader | `spec_disponivel` | Sequencial | — |
| Architect | `requisitos_interpretados` | Sequencial | Spec Reader |
| Code Generator | `arquitetura_definida` | Sequencial | Architect |
| Test Runner | `codigo_gerado` | **Paralela** | Code Generator |
| Quality Auditor | `codigo_gerado` | **Paralela** | Code Generator |
| Release Manager | *(gate)* | **Gate** | Test Runner + Quality Auditor |

## Fluxo de Execução

```
FASE 1 — Análise (sequencial)
  [Início] spec_disponivel
    → Spec Reader → requisitos_interpretados
      → Architect → arquitetura_definida
        → Code Generator → codigo_gerado + src/tests/

FASE 2 — Validação paralela (fan-out)
  codigo_gerado ──┬──→ Test Runner → testes_executados
                   └──→ Quality Auditor → qualidade_aprovada

FASE 3 — Gate (sincronização)
  [Aguardar: testes_executados E qualidade_aprovada]
    → Release Manager → release_concluida
```

## Regras de Execução

### 1. Sequencial
Um agente por vez. O próximo só inicia quando o anterior termina com sucesso.

### 2. Fan-Out (paralelo)
- Um evento pode acionar **múltiplos agentes** simultaneamente.
- Condição: os agentes **não podem depender um do outro**.
- No nosso pipeline: `test_runner` (testes) e `quality_auditor` (análise estática) são independentes.

### 3. Gate (sincronização)
- Um agente pode depender de **múltiplos eventos** antes de executar.
- Sintaxe:
  ```yaml
  gates:
    - nome: validacao_completa
      aguardar:
        - evento: testes_executados
        - evento: qualidade_aprovada
      entao:
        agente: release_manager
  ```
- O gate só libera quando **todos** os eventos forem recebidos.
- Se qualquer evento falhar, o pipeline é interrompido.

## Monitoramento
- **Fan-out**: logs de cada ramo paralelo são independentes e identificados.
- **Gate**: o orquestrador verifica status de cada evento pendente.
- **Timeout**: se um dos agentes paralelos exceder o tempo limite, o pipeline falha.
- **Logs**: `pipeline/logs/pipeline-YYYYMMDD-HHmmss.log`

## Tratamento de Erros

| Situação | Ação |
|----------|------|
| Um ramo paralelo falha | Cancelar todos os ramos ativos, interromper pipeline |
| Gate incompleto | Aguardar até timeout, depois reportar erro |
| Artefato de entrada ausente | Validar antes de iniciar cada agente |

---

*Última atualização: {{DATA_ULTIMA_ATUALIZACAO}}*
