# Fluxo de Versionamento (Git Flow + SemVer)

## Branch Strategy (Git Flow)

```
main ───────────────────────────────────►
  \                                  /
   \── develop ──────────────────►──
        \          \          /
         \── feature/*  release/*
          \── hotfix/*

```

### Branches
| Branch | Origem | Destino do Merge | Finalidade |
|--------|--------|-----------------|------------|
| `main` | — | — | Produção estável |
| `develop` | `main` | `main` | Desenvolvimento contínuo |
| `feature/<nome>` | `develop` | `develop` | Nova funcionalidade |
| `release/<versao>` | `develop` | `main` + `develop` | Preparação de release |
| `hotfix/<descricao>` | `main` | `main` + `develop` | Correção urgente |

## Versionamento Semântico (SemVer 2.0)
Formato: `MAJOR.MINOR.PATCH`

| Incremento | Quando aplicar | Exemplo |
|-----------|---------------|---------|
| **MAJOR** | Mudanças que quebram compatibilidade | `v1.0.0` → `v2.0.0` |
| **MINOR** | Novas funcionalidades compatíveis | `v1.0.0` → `v1.1.0` |
| **PATCH** | Correções de bugs | `v1.0.0` → `v1.0.1` |

Tags de release: `v1.0.0`, `v1.2.3`, `v2.0.0-hotfix1`

## Convenção de Commits (Conventional Commits)

Formato: `<tipo>(<escopo>): <descrição>`

| Tipo | Uso |
|------|-----|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Documentação |
| `refactor` | Refatoração sem mudança de comportamento |
| `test` | Testes |
| `chore` | Tarefas de manutenção |
| `build` | Build ou dependências |
| `ci` | Pipeline de CI/CD |

**Exemplos:**
- `feat(auth): implementar login OAuth2`
- `fix(api): tratar resposta nula no endpoint /users`
- `docs(readme): atualizar instruções de instalação`

## Pull Request Workflow
1. Criar branch `feature/<descricao>` a partir de `develop`.
2. Desenvolver com commits convencionais.
3. Abrir PR para `develop` com descrição clara.
4. Code Review obrigatório (mín. 1 aprovação).
5. CI deve passar (lint, testes, qualidade).
6. Merge com `--no-ff`.
7. Deletar branch após merge.

## Release Process
1. Criar `release/<versao>` a partir de `develop`.
2. Atualizar versão e gerar changelog.
3. Merge em `main` e `develop`.
4. Criar tag `vMAJOR.MINOR.PATCH`.
5. Publicar release notes.

## Hotfix Process
1. Criar `hotfix/<descricao>` a partir de `main`.
2. Aplicar correção, commit com `fix:`.
3. Merge em `main` e `develop`.
4. Criar tag `vMAJOR.MINOR.PATCH-hotfixN`.

---

*Última atualização: {{DATA_ULTIMA_ATUALIZACAO}}*
