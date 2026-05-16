# Catálogo de Agentes e Seus Papéis

## Visão Geral
Este documento descreve todos os agentes disponíveis no pipeline, suas responsabilidades e como se integram.

---

## Agentes

### 1. Leitor de Especificações (Spec Reader)
- **Função**: Interpretar documentos de especificação (PRD e SPEC).
- **Responsabilidades**:
  - Extrair requisitos funcionais e não-funcionais
  - Validar consistência entre documentos
  - Estruturar saída em JSON
- **Trigger**: `spec_disponivel`
- **Config**: `agents/spec_reader/config.yaml`
- **Prompt**: `prompts/prompt_spec_reader.md`

### 2. Arquiteto (Architect)
- **Função**: Projetar a arquitetura do sistema.
- **Responsabilidades**:
  - Definir padrões arquiteturais
  - Selecionar stack tecnológico
  - Documentar decisões técnicas (ADRs)
- **Trigger**: `requisitos_interpretados`
- **Config**: `agents/architect/config.yaml`
- **Prompt**: `prompts/prompt_architect.md`

### 3. Gerador de Código (Code Generator)
- **Função**: Implementar o código-fonte.
- **Responsabilidades**:
  - Gerar código seguindo a arquitetura definida
  - Aplicar princípios SOLID, DRY
  - Gerar testes unitários
- **Trigger**: `arquitetura_definida`
- **Config**: `agents/code_generator/config.yaml`
- **Prompt**: `prompts/prompt_code_generator.md`

### 4. Executor de Testes (Test Runner)
- **Função**: Executar a suíte de testes automatizados.
- **Responsabilidades**:
  - Executar unitários, integração e e2e
  - Medir cobertura de código
  - Gerar relatórios de teste
- **Trigger**: `codigo_gerado`
- **Config**: `agents/test_runner/config.yaml`
- **Prompt**: `prompts/prompt_test_runner.md`

### 5. Auditor de Qualidade (Quality Auditor)
- **Função**: Revisar qualidade e segurança do código.
- **Responsabilidades**:
  - Análise estática (lint, code smells)
  - Análise de segurança (OWASP)
  - Verificar conformidade arquitetural
- **Trigger**: `testes_executados`
- **Config**: `agents/quality_auditor/config.yaml`
- **Prompt**: `prompts/prompt_quality_auditor.md`

### 6. Gerenciador de Release (Release Manager)
- **Função**: Preparar e publicar releases.
- **Responsabilidades**:
  - Versionamento semântico (SemVer)
  - Atualizar changelog e release notes
  - Gerar artefatos de release
- **Trigger**: `qualidade_aprovada`
- **Config**: `agents/release_manager/config.yaml`
- **Prompt**: `prompts/prompt_release_manager.md`

---

## Fluxo de Integração

```
FASE 1 — Análise (sequencial)
spec_disponivel
  → Spec Reader → requisitos_interpretados
    → Architect → arquitetura_definida
      → Code Generator → codigo_gerado + src/tests/

FASE 2 — Validação paralela (fan-out)
codigo_gerado ──┬──→ Test Runner → testes_executados
                 └──→ Quality Auditor → qualidade_aprovada

FASE 3 — Gate (sincronização)
[testes_executados + qualidade_aprovada]
  → Release Manager → release_concluida
```

## Artefatos Compartilhados
- **Entrada/Saída**: Arquivos JSON trafegados entre agentes.
- **Logs**: `pipeline/logs/` com rotação.
- **Código**: `src/` gerado pelo Code Generator.

---

*Última atualização: {{DATA_ULTIMA_ATUALIZACAO}}*
