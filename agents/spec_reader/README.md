# Leitor de Especificações (Spec Reader)

## Descrição
Agente responsável por interpretar os documentos de especificação do projeto (PRD e SPEC) e extrair requisitos estruturados para os demais agentes do pipeline.

## Papel
Interpretar requisitos a partir dos documentos de especificação.

## Acionamento
**Trigger:** `spec_disponivel` — disparado quando novos arquivos de especificação são adicionados ou alterados.

## Entradas
- `docs/PRD.md` — Documento de Requisitos do Produto
- `docs/SPEC.md` — Especificações Técnicas

## Saídas
- `interpreted_requirements.json` — Requisitos funcionais, não-funcionais e critérios de aceitação em formato estruturado.

## Dependências
Nenhuma. É o primeiro agente do pipeline.

## Exemplo de Uso
```bash
# O pipeline inicia automaticamente quando spec_disponivel é disparado.
# Alternativamente, execute manualmente:
./scripts/run_agent.sh spec_reader
```

## Configuração
Ver `config.yaml` para detalhes de configuração.
