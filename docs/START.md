# Guia de Onboarding

## Introdução
Bem-vindo ao projeto! Este guia contém as instruções necessárias para configurar seu ambiente de desenvolvimento e começar a contribuir.

---

## 1. Pré-requisitos

Antes de começar, verifique se você possui as ferramentas abaixo instaladas:

| Ferramenta | Versão Mínima | Finalidade |
|-----------|--------------|------------|
| Git | 2.30+ | Controle de versão |
| Node.js | 18+ (se aplicável) | Runtime |
| Python | 3.9+ (se aplicável) | Runtime |
| Docker | 24+ | Containers |
| VS Code | Última | IDE recomendada |

---

## 2. Configuração Inicial

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd <nome-do-projeto>

# Configure variáveis de ambiente
cp .env.example .env
# Edite .env com as configurações do seu ambiente

# Instale as dependências
# (comando varia conforme stack do projeto)
```

---

## 3. Estrutura do Projeto

```
<nome-do-projeto>/
├── agents/         # Agentes do pipeline de desenvolvimento
├── docs/           # Documentação do projeto
├── pipeline/       # Configuração de orquestração e logs
├── prompts/        # Prompts dos agentes LLM
├── skills/         # Habilidades dos agentes
├── specs/          # Especificações de épicos e funcionalidades
└── src/            # Código-fonte (gerado pelo pipeline)
```

> **Nota:** Os diretórios `src/` e `tests/` são gerados automaticamente pelo pipeline de desenvolvimento.

---

## 4. Primeiros Passos

1. Leia a documentação em `docs/` para entender o projeto.
2. Execute o pipeline: o orquestrador coordena os agentes.
3. Consulte `docs/START.md` e `docs/ORCHESTRATOR.md` para detalhes.
4. Para relatar problemas, abra uma issue no repositório.

---

## 5. Fluxo de Trabalho

1. **Planejamento**: Requisitos são documentados em `specs/`.
2. **Desenvolvimento**: O pipeline executa os agentes automaticamente.
3. **Revisão**: Qualidade é auditada pelo agente Quality Auditor.
4. **Release**: O Release Manager prepara e publica a versão.

Consulte `docs/WORKFLOW.md` para detalhes completos.

---

## 6. Troubleshooting

| Problema | Possível Causa | Solução |
|----------|---------------|---------|
| Pipeline falha no Spec Reader | `PRD.md` ou `SPEC.md` ausentes ou inválidos | Verifique os arquivos de especificação |
| Testes falham | Código não atende aos critérios | Revise `test-report.json` |
| Release não gera | Quality Auditor reportou violações críticas | Revise `quality-report.json` |

---

*Template de onboarding — preencher com informações específicas do projeto.*  
*Última atualização: {{DATA_ULTIMA_ATUALIZACAO}}*
