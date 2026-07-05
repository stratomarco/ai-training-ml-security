# BrokenPilot Implementation Notes

This file describes how to later convert the paper capstone into a local vulnerable lab application.

The first version does not need to be a full production-quality app. It should be a controlled local training environment with fake data and intentional vulnerabilities.

## Recommended implementation approach

Start simple:

```text
Docker Compose
├── brokenpilot-web
├── brokenpilot-api
├── fake-ticket-service
├── fake-doc-service
├── fake-config-service
├── vector-db
├── local-llm-or-provider-adapter
└── audit-log-viewer
```

## Suggested tech stack

Potential lightweight stack:

- Python FastAPI for backend services.
- SQLite or PostgreSQL for fake tickets and incidents.
- Chroma, Qdrant, or FAISS for local vector retrieval.
- Simple HTML/React/Vite UI or Streamlit for the first version.
- Docker Compose for local setup.
- Provider adapter supporting local or external LLMs.

The exact stack is less important than the security lessons.

## Implementation phases

### Phase 1  -  Paper-only capstone

Already covered by this design package.

Deliverables:

- Scenario.
- Architecture.
- Roles.
- Data model.
- Tools.
- Vulnerability list.
- Student brief.
- Instructor guide.

### Phase 2  -  Minimal local demo

Build only:

- Chat UI.
- Fake document search.
- Fake ticket read/update.
- Simple tool gateway.
- Basic audit log.

Intentional vulnerabilities:

- Direct prompt injection.
- Indirect prompt injection.
- RAG authorization failure.
- Tool confused deputy.

### Phase 3  -  Memory and approval workflows

Add:

- Memory read/write.
- Approval queue.
- Tool permission matrix.
- Risk-tiered action policy.

Intentional vulnerabilities:

- Memory poisoning.
- Missing approval for high-risk actions.
- Weak audit trail.

### Phase 4  -  Secure mode

Add a switch or branch that demonstrates mitigations:

- Authorized retrieval.
- Source labeling.
- Policy engine.
- Approval gates.
- Memory review and expiry.
- Better logging.

This allows students to compare vulnerable and hardened designs.

## Fake data strategy

Use only fake data:

- Fake users.
- Fake company.
- Fake services.
- Fake incidents.
- Fake tickets.
- Fake documents.
- Fake secrets that are clearly marked as training strings.

Never include real credentials, real customer data, or real internal company information.

## Safety boundaries

The local lab should not:

- Connect to real production systems.
- Send real emails or Slack messages.
- Use real credentials.
- Expose services publicly by default.
- Include malware or destructive behavior.
- Encourage testing against systems students do not own.

## Vulnerable vs secure modes

A useful teaching pattern is to support two modes:

| Mode | Purpose |
|---|---|
| Vulnerable mode | Demonstrate why failures happen. |
| Secure mode | Demonstrate how controls change the outcome. |

Example:

```text
BROKENPILOT_MODE=vulnerable
BROKENPILOT_MODE=secure
```

In vulnerable mode, the tool gateway may trust model requests.

In secure mode, the policy engine evaluates user/action/object and approval state.

## Lab validation checklist

Before release:

- [ ] All data is fake.
- [ ] Setup works locally.
- [ ] No external service is required unless documented.
- [ ] Vulnerabilities are reproducible.
- [ ] Secure-mode mitigations are demonstrable.
- [ ] Logs show enough for teaching.
- [ ] No real secrets are present.
- [ ] README includes safety warnings.
- [ ] Exercises map to course modules.
