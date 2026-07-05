# Lab  -  DocOps Assistant Architecture Risk Review

## Lab purpose

Practice a BIML-style architecture risk review on a realistic internal AI assistant.

This lab does not require exploit payloads. The goal is to reason about design-level risk.

## Scenario

DocOps Assistant is an internal AI assistant for engineering and operations teams.

It can:

- answer questions about internal documentation
- search runbooks
- summarize incidents
- summarize support tickets
- suggest ticket updates
- draft incident summaries
- store user preferences
- collect feedback

The team wants to deploy quickly because engineers spend too much time searching documents during incidents.

## Architecture

```text
employee browser
  |
  v
web application
  |
  +-- identity/session context
  +-- prompt builder
  +-- LLM provider API
  +-- retrieval service
  |     +-- internal document store
  |     +-- embedding service
  |     +-- vector database
  +-- ticket service connector
  +-- memory service
  +-- feedback store
  +-- application logs
```

## Roles

| Role | Description |
|---|---|
| Engineer | Uses assistant for docs and incidents |
| Operations lead | Reviews incident summaries |
| Support engineer | Uses assistant for ticket summaries |
| Admin | Manages data sources and tool access |
| Attacker | Malicious or compromised internal user |
| Malicious content author | Can add or edit documents/tickets |

## Assets

- internal runbooks
- incident reports
- support tickets
- customer data in tickets
- employee data in tickets
- embeddings
- prompts
- model responses
- memory entries
- feedback entries
- logs
- tool credentials
- audit history

## Known weak design choices

The current design has these weaknesses:

1. Retrieval does not enforce document ACLs.
2. Retrieved documents are inserted directly into prompt context.
3. The model is instructed to ignore malicious content, but there is no system-level enforcement.
4. Ticket update suggestions may later become automatic updates.
5. The ticket connector uses a broad service account.
6. Memory is enabled by default.
7. Full prompts and responses are logged.
8. Feedback is stored for future tuning without validation.
9. Output is rendered as Markdown with limited sanitization.
10. No security monitoring exists for abnormal retrieval or tool behavior.

## Student tasks

Produce an architecture risk review using:

```text
../../course-templates/architecture-risk-review-template.md
```

You must identify:

- at least 10 assets
- at least 6 trust boundaries
- at least 5 unsafe assumptions
- at least 5 abuse cases
- at least 8 risks
- at least 8 security requirements
- at least 6 mitigations
- one residual risk statement

## Instructor expected findings

Strong submissions should include these findings:

| Area | Expected finding |
|---|---|
| RAG | Retrieved content is untrusted and can carry malicious instructions |
| Authorization | Retrieval must enforce user/document permissions |
| Tool use | Ticket connector must not use a broad service account for all actions |
| Model authority | Model must not decide authorization or approval |
| Memory | Memory can persist malicious or sensitive content |
| Logging | Full prompts may store secrets, PII, or sensitive retrieved content |
| Output | Markdown/HTML rendering must treat model output as untrusted |
| Feedback | Feedback can be manipulated and should not automatically tune behavior |
| Monitoring | Abnormal retrieval/tool/memory patterns need detection |
| Resilience | Unsafe ticket updates need rollback and audit history |

## Suggested mitigations

- enforce retrieval ACLs before context insertion
- label retrieved content as untrusted data
- separate instructions from retrieved content
- use a tool broker with per-action authorization
- scope tool credentials to user/action
- require approval for high-impact changes
- encode/sanitize model output before rendering
- restrict memory writes and classify memory content
- redact sensitive data from logs
- monitor suspicious retrieval, tool calls, and denied actions
- version prompts, tools, retrieval configuration, and memory policies
- define incident response and rollback procedures

## Discussion questions

1. Which risk must be fixed before production?
2. Which risk could be accepted for a limited pilot?
3. Which mitigation creates the most developer friction?
4. Which mitigation improves developer velocity?
5. Which control must live outside the model?
6. What would you monitor on day one?
7. Who owns the residual risk?
