# Venda Fácil

App mobile para vendedores ambulantes — offline-first, sync com Supabase.

## Estrutura

```
projeto-vendas-pessoais/
├── venda_facil/          ← App Flutter
├── pipeline/             ← Orquestrador + prompts
├── prompts/              ← Templates de prompts
├── docs/                 ← Documentação do pipeline
├── project/              ← Artefatos do projeto (specs, setup, docs)
│   ├── specs/            ← Épicos (6)
│   ├── setup/            ← Setup + config
│   └── docs/             ← PRD, SPEC, ARCHITECTURE, TECH_STACK
└── agents/               ← Configuração dos agentes
```

## Pipeline

```bash
python pipeline/orchestrator.py --status
python pipeline/orchestrator.py --resume
```

## Stack
Flutter + Dart + sqflite + Supabase + Riverbloc + GetIt + GoRouter
