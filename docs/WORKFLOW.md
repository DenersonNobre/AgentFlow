# Gestão Visual (Kanban + Git Flow)

## Quadro Kanban

| Backlog | To Do | In Progress | Code Review | Testing | Done |
|---------|-------|-------------|-------------|---------|------|
| Ideias priorizadas | Pronto para iniciar | Em desenvolvimento | Aguardando revisão | Em teste | Concluído |

### Swimlanes
- **Feature** — Novas funcionalidades
- **Bug** — Correções
- **Tech Debt** — Refatoração e melhorias
- **Release** — Tarefas de release

## Etiquetas (Labels)
| Label | Descrição |
|-------|-----------|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `enhancement` | Melhoria |
| `docs` | Documentação |
| `urgent` | Prioridade máxima |
| `high` | Prioridade alta |
| `medium` | Prioridade média |
| `low` | Prioridade baixa |
| `tech-debt` | Dívida técnica |

## Workflow de Desenvolvimento

### 1. Planejamento
- Issue criada no backlog com descrição e critérios de aceitação.
- Priorizada e movida para "To Do".

### 2. Desenvolvimento
```bash
git checkout develop
git pull origin develop
git checkout -b feature/<descricao>
```
- Commits com mensagens convencionais.
- Mover card para "In Progress".

### 3. Code Review
- Abrir PR para `develop`.
- Mover card para "Code Review".
- Checklist obrigatório:
  - [ ] Lint passou
  - [ ] Testes passaram
  - [ ] Cobertura ≥ 80%
  - [ ] Código segue padrões do projeto

### 4. Testes
- CI executa testes automaticamente.
- Mover card para "Testing".
- Se falhar, retornar para "In Progress".

### 5. Conclusão
- Merge aprovado e branch deletada.
- Mover card para "Done".

## Revisão de Código (Code Review)
### Critérios
- **Funcionalidade**: O código resolve o problema proposto?
- **Qualidade**: Código limpo, legível, seguindo padrões?
- **Testes**: Testes adequados e cobrindo os cenários?
- **Segurança**: Há vulnerabilidades ou dados expostos?
- **Performance**: Há gargalos evidentes?

### Boas Práticas
- Revise no máximo 400 linhas por sessão.
- Seja construtivo: critique o código, não a pessoa.
- Use "nit:" para sugestões não críticas.
- Aprove apenas quando todos os critérios forem atendidos.

---

*Última atualização: {{DATA_ULTIMA_ATUALIZACAO}}*
