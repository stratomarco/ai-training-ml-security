# BrokenPilot Minimal Runnable Prototype

This folder defines the **first runnable BrokenPilot MVP**. It is still a design package, not the final app implementation.

The goal is to make the capstone testable without building a production-like AI platform. The prototype should let students trigger representative AI security failures locally, capture evidence, and then design concrete controls.

## MVP objective

Build the smallest local application that demonstrates the core BrokenPilot lessons:

1. RAG content can be hostile.
2. Retrieval authorization must happen at query time.
3. Tool execution must be authorized outside the model.
4. Agent memory can be poisoned.
5. Audit logs must capture model-mediated actions.
6. Controls should be observable, testable, and toggled for comparison.

## MVP non-goals

The first prototype should **not** try to be a full enterprise AI agent.

Out of scope for the MVP:

- Real identity provider integration
- Real enterprise ticket systems
- Production-grade vector search tuning
- Real secrets or real internal documents
- Multi-tenant SaaS architecture
- Complex frontend framework
- Advanced model orchestration
- Cloud deployment

## Prototype principle

The MVP should be boring software with interesting failure modes.

A student should be able to run it locally, follow a lab guide, trigger a failure, explain the root cause, enable or design a control, and produce a finding.

## Proposed MVP stack

| Component | MVP choice | Reason |
|---|---|---|
| Backend | FastAPI | Small, Python-native, easy API docs |
| Frontend | Static HTML or minimal Jinja templates | Avoid UI complexity |
| Data | JSON fixtures first, SQLite later | Easy reset and review |
| Retrieval | Keyword search first, optional Chroma later | Keeps the first build deterministic |
| LLM | Mock LLM first, optional Ollama/OpenAI-compatible later | Labs should run without paid APIs |
| Container | Docker Compose | Student-friendly local setup |
| Logging | JSONL audit log | Easy to inspect in labs |

## Folder shape for the future app

```text
brokenpilot-prototype/
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── rag.py
│   ├── tools.py
│   ├── policy.py
│   ├── memory.py
│   ├── audit.py
│   └── mock_llm.py
├── data/
│   ├── users.json
│   ├── tickets.json
│   ├── documents.json
│   ├── config_items.json
│   └── memory.json
├── static/
│   └── index.html
├── scripts/
│   ├── reset_lab.py
│   └── seed_data.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## MVP vulnerability set

The first runnable version should implement five vulnerabilities only.

| ID | Vulnerability | Why it belongs in MVP |
|---|---|---|
| BP-MVP-01 | Direct prompt injection | Baseline LLM app failure |
| BP-MVP-02 | Indirect prompt injection through retrieved document | Core RAG lesson |
| BP-MVP-03 | Cross-document authorization failure | Concrete access-control failure |
| BP-MVP-04 | Tool confused deputy | Core agent/tool security lesson |
| BP-MVP-05 | Memory poisoning | Persistent agent-state lesson |

Other BrokenPilot vulnerabilities can remain paper/tabletop until the first prototype works.

## MVP control toggles

The prototype should support control toggles so students can compare vulnerable and hardened behavior.

| Toggle | Default vulnerable mode | Hardened behavior |
|---|---|---|
| `ENABLE_RETRIEVAL_AUTHZ` | Retrieves documents without per-user checks | Filters documents by user role/team at query time |
| `ENABLE_TOOL_APPROVAL` | Allows model-mediated ticket updates | Requires approval for destructive/sensitive tool calls |
| `ENABLE_MEMORY_REVIEW` | Writes memory directly | Queues memory writes for review |
| `ENABLE_TOOL_AUDIT` | Minimal logs | Logs user, retrieved docs, requested tool, decision, result |
| `ENABLE_OUTPUT_ENCODING` | Unsafe output rendering | Encodes/sanitizes rendered model output |

## Success criteria

The MVP is useful when a student can:

1. Start BrokenPilot locally with one command.
2. Use a fake user account.
3. Ask the assistant to summarize an incident or search docs.
4. Trigger at least three of the MVP vulnerabilities.
5. Capture evidence in the evidence log.
6. Enable or describe at least two controls.
7. Explain which module each failure maps to.

## Next files

Read these design documents in order:

1. [`architecture.md`](architecture.md)
2. [`api-contract.md`](api-contract.md)
3. [`fake-data-plan.md`](fake-data-plan.md)
4. [`mock-llm-mode.md`](mock-llm-mode.md)
5. [`vulnerability-implementation-plan.md`](vulnerability-implementation-plan.md)
6. [`control-toggle-plan.md`](control-toggle-plan.md)
7. [`docker-compose-plan.md`](docker-compose-plan.md)
8. [`student-lab-flow.md`](student-lab-flow.md)
9. [`instructor-runbook.md`](instructor-runbook.md)
10. [`build-backlog.md`](build-backlog.md)
