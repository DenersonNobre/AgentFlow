import json, sys, os
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
FLUTTER_DIR = BASE_DIR / "venda_facil"
PIPELINE_DIR = BASE_DIR / "pipeline"
PROJECT_DIR = BASE_DIR / "project"
PROJECT_SETUP_DIR = PROJECT_DIR / "setup"
PROJECT_SPECS_DIR = PROJECT_DIR / "specs"
PROJECT_DOCS_DIR = PROJECT_DIR / "docs"
PROMPTS_DIR = BASE_DIR / "prompts"
STATE_FILE = PIPELINE_DIR / "state.json"
LOG_FILE = PIPELINE_DIR / "logs" / "pipeline.log"
MCP_FILE = PIPELINE_DIR / "mcp.yaml"

os.makedirs(PIPELINE_DIR / "logs", exist_ok=True)

def log(msg, nivel="INFO"):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] [{nivel}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def carregar_json(path):
    if not path.exists():
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def ler_mcp():
    if not MCP_FILE.exists():
        log("mcp.yaml não encontrado", "ERRO")
        return None
    import yaml
    with open(MCP_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_state():
    if STATE_FILE.exists():
        return carregar_json(STATE_FILE)
    return {
        "fase_atual": 0,
        "etapas": {},
        "artefatos": {},
        "iniciado_em": None,
        "concluido_em": None,
        "status": "pendente",
        "etapa_atual": None,
    }

def save_state(state):
    salvar_json(STATE_FILE, state)

def update_etapa(state, nome, status, artefatos=None):
    state["etapas"][nome] = {"status": status, "atualizado_em": datetime.now().isoformat()}
    if artefatos:
        state["artefatos"].update(artefatos)
    save_state(state)

# --- Fase 0: Setup Validator ---
def fase0_setup_validator(state):
    log("=" * 50)
    log("FASE 0 — Setup Validator")
    log("=" * 50)
    setup_path = PROJECT_SETUP_DIR / "SETUP.md"
    if not setup_path.exists():
        log("SETUP.md não encontrado", "ERRO")
        return {"sucesso": False, "erro": "SETUP.md não encontrado"}
    log(f"SETUP.md encontrado: {setup_path}")
    dirs_esperados = ["lib/core", "lib/features", "test", "supabase/migrations"]
    for d in dirs_esperados:
        p = FLUTTER_DIR / d
        if not p.exists():
            log(f"Diretório esperado não existe: {d} (opcional — será criado)", "AVISO")
            p.mkdir(parents=True, exist_ok=True)
    config = {
        "project_name": "venda_fácil",
        "stack": {
            "framework": "flutter",
            "language": "dart",
            "db_local": "sqflite",
            "db_cloud": "supabase",
            "auth": "Supabase Auth",
        },
        "tools": {},
        "env_keys": ["SUPABASE_URL", "SUPABASE_ANON_KEY"],
        "dirs": [{"dir": d, "existe": (BASE_DIR / d).exists()} for d in dirs_esperados],
    }
    config_file = PROJECT_SETUP_DIR / "config_do_projeto.json"
    salvar_json(config_file, config)
    log(f"config_do_projeto.json gerado em {config_file}")
    update_etapa(state, "setup_validator", "concluido", {"config_do_projeto.json": str(config_file)})
    state["fase_atual"] = 0
    save_state(state)
    return {"sucesso": True}

# --- Fase 1a: Spec Reader ---
def fase1a_spec_reader(state):
    log("=" * 50)
    log("FASE 1a — Spec Reader")
    log("=" * 50)
    prd = PROJECT_DOCS_DIR / "PRD.md"
    spec = PROJECT_DOCS_DIR / "SPEC.md"
    specs_dir = PROJECT_SPECS_DIR
    config_file = PROJECT_SETUP_DIR / "config_do_projeto.json"
    if not prd.exists() or not spec.exists():
        log("PRD.md ou SPEC.md ausentes", "ERRO")
        return {"sucesso": False, "erro": "PRD.md ausente"}
    epics = sorted(specs_dir.glob("*.md")) if specs_dir.exists() else []
    config_data = carregar_json(config_file) or {}
    prompt = f"""# Spec Reader Prompt

## Entradas
- PRD.md: {prd}
- SPEC.md: {spec}
- {len(epics)} épico(s) em specs/
- config_do_projeto.json: {config_file}

## Tarefa
Leia todos os documentos, extraia requisitos funcionais e não-funcionais,
critérios de aceitação, tasks, dependências e inconsistências.
Gere pipeline/interpreted_requirements.json com a estrutura definida.

## Épicos encontrados
"""
    for e in epics:
        prompt += f"- {e.name}\n"
    prompt_file = PIPELINE_DIR / "spec_reader_prompt.md"
    prompt_file.write_text(prompt, encoding="utf-8")
    log(f"Prompt do Spec Reader preparado em {prompt_file}")
    log(f"{len(epics)} épico(s) encontrado(s)")
    log("AGUARDANDO: Execute o Spec Reader (IA) e salve o resultado em pipeline/interpreted_requirements.json")
    update_etapa(state, "spec_reader", "aguardando_ia", {"spec_reader_prompt.md": str(prompt_file)})
    state["fase_atual"] = 1
    state["etapa_atual"] = "spec_reader"
    save_state(state)
    return {"sucesso": True}

# --- Fase 1b: Architect ---
def fase1b_architect(state):
    log("=" * 50)
    log("FASE 1b — Architect")
    log("=" * 50)
    req_file = PIPELINE_DIR / "interpreted_requirements.json"
    if not req_file.exists():
        log("interpreted_requirements.json não encontrado", "ERRO")
        return {"sucesso": False, "erro": "Spec Reader não concluído"}
    req_data = carregar_json(req_file)
    prompt = f"""# Architect Prompt

## Entrada
interpreted_requirements.json processado com {len(req_data.get('requisitos_funcionais', []))} RFs.

## Tarefa
1. Analise todos os requisitos.
2. Atualize project/docs/ARCHITECTURE.md com a arquitetura final.
3. Atualize project/docs/TECH_STACK.md com o stack tecnológico.
4. Documente ADRs para decisões críticas.
"""
    prompt_file = PIPELINE_DIR / "architect_prompt.md"
    prompt_file.write_text(prompt, encoding="utf-8")
    log(f"Prompt do Architect preparado em {prompt_file}")
    log("AGUARDANDO: Execute o Architect (IA) e atualize project/docs/ARCHITECTURE.md e project/docs/TECH_STACK.md")
    update_etapa(state, "architect", "aguardando_ia", {"architect_prompt.md": str(prompt_file)})
    state["fase_atual"] = 1
    state["etapa_atual"] = "architect"
    save_state(state)
    return {"sucesso": True}

# --- Fase 1c: Code Generator ---
def fase1c_code_generator(state):
    log("=" * 50)
    log("FASE 1c — Code Generator")
    log("=" * 50)
    req_file = PIPELINE_DIR / "interpreted_requirements.json"
    arch = PROJECT_DOCS_DIR / "ARCHITECTURE.md"
    tech = PROJECT_DOCS_DIR / "TECH_STACK.md"
    if not req_file.exists():
        return {"sucesso": False, "erro": "Spec Reader não concluído"}
    req_data = carregar_json(req_file)
    n_reqs = len(req_data.get("requisitos_funcionais", []))
    n_tasks = len(req_data.get("tasks", []))
    prompt = f"""# Code Generator Prompt

## Entradas
- interpreted_requirements.json: {n_reqs} RFs, {n_tasks} tasks
- ARCHITECTURE.md: {arch if arch.exists() else 'não encontrado'}
- TECH_STACK.md: {tech if tech.exists() else 'não encontrado'}

## Tarefa
Implemente todo o código-fonte em venda_facil/ seguindo a arquitetura Vertical Slice:
- venda_facil/lib/core/ (database, sync, router, theme, di)
- venda_facil/lib/features/auth/
- venda_facil/lib/features/clientes/
- venda_facil/lib/features/produtos/
- venda_facil/lib/features/vendas/
- venda_facil/lib/features/contas_receber/
- venda_facil/lib/features/dashboard/
- venda_facil/test/ (testes unitários para cada slice)

Gere código limpo com tratamento de erros, validações e testes.
"""
    prompt_file = PIPELINE_DIR / "code_generator_prompt.md"
    prompt_file.write_text(prompt, encoding="utf-8")
    log(f"Prompt do Code Generator preparado em {prompt_file}")
    log("AGUARDANDO: Execute o Code Generator (IA) para gerar lib/ e test/")
    update_etapa(state, "code_generator", "aguardando_ia", {"code_generator_prompt.md": str(prompt_file)})
    state["fase_atual"] = 1
    state["etapa_atual"] = "code_generator"
    save_state(state)
    return {"sucesso": True}

# --- Fase 2: Validação Paralela ---
def fase2_execucao_paralela(state):
    log("=" * 50)
    log("FASE 2 — Validação Paralela (fan-out)")
    log("=" * 50)
    src = FLUTTER_DIR / "lib"
    if not src.exists() or not any(src.rglob("*.dart")):
        log("lib/ não encontrado. Code Generator precisa ser executado primeiro.", "ERRO")
        return {"sucesso": False, "erro": "lib/ não encontrado"}
    log("Código encontrado. Preparando prompts para Test Runner e Quality Auditor...")
    prompt_test = f"""# Test Runner Prompt
Execute os testes em test/ e gere pipeline/test-report.json.
Comando: flutter test --machine > pipeline/test-report.json
"""
    (PIPELINE_DIR / "test_runner_prompt.md").write_text(prompt_test, encoding="utf-8")
    prompt_quality = f"""# Quality Auditor Prompt
Analise a qualidade do código em lib/ de forma **rigorosa**:
1. Execute `flutter analyze lib/` — **0 erros, 0 warnings, 0 infos** são exigidos. Qualquer alerta (info, warning, error) em QUALQUER arquivo (lib/, test/, integration_test/) REPROVA a qualidade.
2. Execute `flutter test` — **100% dos testes devem passar**. Testes pulados ou falhos REPROVAM.
3. Verifique padrões arquiteturais (Clean Architecture, BLoC, Repository, injeção de dependência)
4. Gere `pipeline/quality-report.json` com a análise completa, listando cada alerta individualmente.
5. **Regra de ouro**: se houver QUALQUER alerta (error, warning, info) em qualquer arquivo, o status deve ser "reprovado".
"""
    (PIPELINE_DIR / "quality_auditor_prompt.md").write_text(prompt_quality, encoding="utf-8")
    update_etapa(state, "test_runner", "aguardando_ia", {"test_runner_prompt.md": str(PIPELINE_DIR / "test_runner_prompt.md")})
    update_etapa(state, "quality_auditor", "aguardando_ia", {"quality_auditor_prompt.md": str(PIPELINE_DIR / "quality_auditor_prompt.md")})
    state["fase_atual"] = 2
    state["etapa_atual"] = "test_runner"
    save_state(state)
    return {"sucesso": True}

# --- Fase 3: Gate + Release ---
def fase3_gate_release(state):
    log("=" * 50)
    log("FASE 3 — Gate + Release Manager")
    log("=" * 50)
    test_report = PIPELINE_DIR / "test-report.json"
    quality_report = PIPELINE_DIR / "quality-report.json"
    if not test_report.exists() or not quality_report.exists():
        log("Gate bloqueado: relatórios ausentes", "ERRO")
        return {"sucesso": False, "erro": "Gate bloqueado: relatórios ausentes"}
    test_data = carregar_json(test_report) or {}
    quality_data = carregar_json(quality_report) or {}
    changelog = ""
    changelog_file = BASE_DIR / "docs" / "CHANGELOG.md"
    if changelog_file.exists():
        changelog = changelog_file.read_text(encoding="utf-8")
    prompt = f"""# Release Manager Prompt

## Gate Aprovado
- test-report.json: OK
- quality-report.json: OK

## CHANGELOG.md Atual
{changelog}

## Instruções
Analise as mudanças, incremente a versão (SemVer), atualize CHANGELOG.md e gere RELEASE_NOTES.md.
"""
    prompt_file = PIPELINE_DIR / "release_manager_prompt.md"
    prompt_file.write_text(prompt, encoding="utf-8")
    log(f"Prompt do Release Manager preparado em {prompt_file}")
    log("AGUARDANDO: Execute Release Manager (IA)")
    update_etapa(state, "release_manager", "aguardando_ia", {"release_manager_prompt.md": str(prompt_file)})
    state["fase_atual"] = 3
    state["etapa_atual"] = "release_manager"
    save_state(state)
    return {"sucesso": True}

# --- Fase 4: Learning Agent ---
def fase4_learning_agent(state):
    log("=" * 50)
    log("FASE 4 — Learning Agent")
    log("=" * 50)
    learning_path = BASE_DIR / "docs" / "LEARNING.md"
    learning_content = learning_path.read_text(encoding="utf-8") if learning_path.exists() else ""
    metricas = {
        "fases_executadas": list(state["etapas"].keys()),
        "status_etapas": {k: v["status"] for k, v in state["etapas"].items()},
        "artefatos": list(state["artefatos"].keys()),
        "ciclo_iniciado": state.get("iniciado_em"),
        "ciclo_concluido": datetime.now().isoformat(),
    }
    prompt = f"""# Learning Agent — Análise de Ciclo

## Métricas do Ciclo
```json
{json.dumps(metricas, indent=2, ensure_ascii=False)}
```

## LEARNING.md Atual
{learning_content}

## Instruções
Analise o ciclo completo do pipeline e registre lições aprendidas:
1. O que funcionou bem
2. O que pode melhorar
3. Próximos passos
4. Recomendações

Atualize project/docs/LEARNING.md com uma nova entrada.
"""
    prompt_file = PIPELINE_DIR / "learning_agent_prompt.md"
    prompt_file.write_text(prompt, encoding="utf-8")
    log(f"Prompt do Learning Agent preparado em {prompt_file}")
    log("AGUARDANDO: Analise o ciclo e atualize project/docs/LEARNING.md")
    update_etapa(state, "learning_agent", "aguardando_ia", {"learning_agent_prompt.md": str(prompt_file)})
    state["fase_atual"] = 4
    state["etapa_atual"] = "learning_agent"
    save_state(state)
    return {"sucesso": True}

# --- Helpers ---
def _encontrar_base_dir() -> Path:
    for p in [PROJECT_SETUP_DIR, BASE_DIR]:
        if (p / "SETUP.md").exists():
            return p
    return BASE_DIR

base_dir = _encontrar_base_dir()

def mostrar_status(state):
    print("\n" + "=" * 60)
    print("STATUS DO PIPELINE")
    print("=" * 60)
    print(f"Status geral: {state['status']}")
    print(f"Fase atual: {state['fase_atual']}")
    if state.get("etapa_atual"):
        print(f"Etapa atual: {state['etapa_atual']}")
    print(f"Iniciado em: {state.get('iniciado_em', '—')}")
    print()
    print("Etapas:")
    for etapa, dados in state["etapas"].items():
        status = dados["status"]
        icone = "[ok]" if status == "concluido" else "[ia]" if status == "aguardando_ia" else "[fail]" if status == "falha" else "[..]"
        print(f"  {icone} {etapa}: {status}")
    print()
    print("Artefatos gerados:")
    for nome, path in state["artefatos"].items():
        existe = Path(path).exists() if path else False
        print(f"  {'[x]' if existe else '[ ]'} {nome}: {path}")
    print()

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Orquestrador do Pipeline")
    parser.add_argument("--fase", type=int, choices=[0, 1, 2, 3, 4], help="Executar fase específica")
    parser.add_argument("--status", action="store_true", help="Mostrar status atual")
    parser.add_argument("--resume", action="store_true", help="Continuar da fase atual")
    parser.add_argument("--etapa", type=str, help="Executar etapa específica")
    args = parser.parse_args()
    state = load_state()
    if args.status:
        mostrar_status(state)
        return
    try:
        import yaml
    except ImportError:
        log("PyYAML é necessário. Instale: pip install pyyaml", "ERRO")
        sys.exit(1)
    mcp = ler_mcp()
    if not mcp:
        sys.exit(1)
    if not state["iniciado_em"]:
        state["iniciado_em"] = datetime.now().isoformat()
        state["status"] = "executando"
        save_state(state)
    log(f"Pipeline iniciado em {state['iniciado_em']}")
    if args.etapa:
        etapa_map = {
            "setup_validator": fase0_setup_validator,
            "spec_reader": fase1a_spec_reader,
            "architect": fase1b_architect,
            "code_generator": fase1c_code_generator,
            "test_runner": lambda s: fase2_execucao_paralela(s),
            "quality_auditor": lambda s: fase2_execucao_paralela(s),
            "release_manager": fase3_gate_release,
            "learning_agent": fase4_learning_agent,
        }
        func = etapa_map.get(args.etapa)
        if func:
            resultado = func(state)
            if not resultado.get("sucesso"):
                log(f"Etapa {args.etapa} falhou: {resultado.get('erro', 'erro desconhecido')}", "ERRO")
                sys.exit(1)
        else:
            log(f"Etapa desconhecida: {args.etapa}", "ERRO")
            sys.exit(1)
        return
    if args.fase is not None or args.resume:
        inicio = args.fase if args.fase is not None else state["fase_atual"]
    else:
        inicio = 0
    fases = [
        ("Fase 0 — Setup", fase0_setup_validator),
        ("Fase 1a — Spec Reader", fase1a_spec_reader),
        ("Fase 1b — Architect", fase1b_architect),
        ("Fase 1c — Code Generator", fase1c_code_generator),
        ("Fase 2 — Validação Paralela", lambda s: fase2_execucao_paralela(s)),
        ("Fase 3 — Gate + Release", fase3_gate_release),
        ("Fase 4 — Aprendizado", fase4_learning_agent),
    ]
    for i, (nome, func) in enumerate(fases[inicio:], start=inicio):
        log(f"Executando {nome}...")
        resultado = func(state)
        if not resultado.get("sucesso"):
            if resultado.get("erro"):
                log(f"{nome} falhou: {resultado['erro']}", "ERRO")
                if resultado["erro"] in [
                    "SETUP.md não encontrado", "PRD.md ausente",
                    "Spec Reader não concluído", "lib/ não encontrado",
                    "Gate bloqueado: relatórios ausentes",
                ]:
                    sys.exit(1)
            log(f"{nome} concluída. Próximo: aguardando ação da IA.", "INFO")
            break
    state["concluido_em"] = datetime.now().isoformat()
    state["status"] = "concluido"
    save_state(state)
    log("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    main()
