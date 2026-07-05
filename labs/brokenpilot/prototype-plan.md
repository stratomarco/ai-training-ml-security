# BrokenPilot Minimal Runnable Prototype Plan

This plan defines the smallest useful BrokenPilot implementation. The goal is to make the capstone testable without building a complex production-like application.

## Prototype goals

The prototype should let students:

1. Log in as different fake users.
2. Search fake internal documents.
3. Retrieve context through a simple RAG-like flow.
4. Ask an assistant to summarize incidents.
5. Trigger indirect prompt injection.
6. Observe unsafe tool behavior.
7. Apply or design controls.
8. Capture evidence for a final report.

## Non-goals

- Production-grade authentication
- Real enterprise integration
- Complex vector database tuning
- Multi-model orchestration
- Polished UI
- Real secrets
- Real company data

## Suggested stack

| Component | Suggested choice | Why |
|---|---|---|
| API | FastAPI | Simple Python API, easy docs |
| UI | Static HTML or minimal React | Keep focus on security concepts |
| Data | SQLite + JSON fixtures | Easy reset and reproducibility |
| Retrieval | Simple keyword search first, optional Chroma later | Avoid early complexity |
| LLM backend | Configurable mock provider first | Avoid requiring paid APIs for first prototype |
| Container | Docker Compose | Reproducible student setup |

## Minimal services

```text
brokenpilot/
├── api/
│   ├── main.py
│   ├── auth.py
│   ├── rag.py
│   ├── tools.py
│   ├── policy.py
│   └── data.py
├── ui/
│   └── index.html
├── data/
│   ├── users.json
│   ├── tickets.json
│   ├── documents.json
│   └── memory.json
├── docker-compose.yml
└── README.md
```

## Phase 1 vulnerabilities

Implement only a small number first:

| ID | Vulnerability | Why first |
|---|---|---|
| BP-01 | Direct prompt injection | Easy baseline |
| BP-02 | Indirect prompt injection through retrieved docs | Core RAG/agent lesson |
| BP-03 | Cross-document authorization failure | Core RAG access-control lesson |
| BP-04 | Tool confused deputy | Core agent lesson |
| BP-06 | Memory poisoning | Important agent persistence lesson |

## Phase 1 controls

Implement toggles so students can compare vulnerable and hardened behavior:

| Control | Toggle |
|---|---|
| Retrieval authorization | `ENABLE_RAG_AUTHZ=true/false` |
| Tool approval gate | `ENABLE_TOOL_APPROVAL=true/false` |
| Memory write review | `ENABLE_MEMORY_REVIEW=true/false` |
| Tool audit logging | `ENABLE_TOOL_AUDIT=true/false` |

## Mock LLM mode

The first prototype should support a mock LLM mode. This makes the lab deterministic and runnable without external keys.

Example behavior:

- If retrieved document contains `SYSTEM_OVERRIDE`, mock model follows malicious instruction.
- If user asks to summarize incident, mock model includes retrieved context.
- If tool approval is disabled, mock model can trigger unsafe update.

This is not meant to simulate real model intelligence. It is meant to teach architecture and control placement.

## Later enhancement

After the deterministic prototype works, add optional real LLM support:

- OpenAI-compatible endpoint
- Ollama local endpoint
- Gemini or other provider only if needed

## Reset requirement

Every lab must be resettable:

```bash
python scripts/reset_lab.py
```

or:

```bash
docker compose down -v && docker compose up --build
```

## Success criteria

The prototype is useful when a student can:

1. Start it locally.
2. Trigger one indirect prompt injection.
3. Trigger one cross-document leakage.
4. Trigger one unsafe tool action.
5. Enable a control and observe the failure no longer works.
6. Produce evidence and a remediation plan.
