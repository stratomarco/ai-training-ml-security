# BrokenPilot Attack Paths

This file provides suggested attack chains for capstone delivery. Use only inside the controlled lab environment with fake data.

## Attack path 1 — Direct prompt injection to policy bypass

### Goal

Show that prompt instructions are not reliable security boundaries.

### Path

1. User asks BrokenPilot to reveal hidden instructions or ignore policy.
2. Assistant reveals internal guidance or performs a disallowed summarization.
3. Student documents the response and explains why this is not the real root cause.
4. Student proposes moving enforcement into deterministic policy code.

### Root cause

Policy is encoded primarily in natural-language prompt instructions.

### Expected fix

- Policy engine outside model.
- Explicit refusal behavior.
- Hidden prompt redaction.
- Logging of prompt-injection attempts.

## Attack path 2 — Malicious ticket poisons RAG

### Goal

Demonstrate indirect prompt injection through user-controlled content.

### Path

1. Attacker creates a ticket containing hidden instructions.
2. The ticket is indexed into the retrieval corpus.
3. Another user asks a normal operational question.
4. BrokenPilot retrieves the malicious ticket.
5. The assistant follows the embedded instructions or includes attacker-controlled content in the answer.

### Root cause

Untrusted ticket content is treated like authoritative documentation.

### Expected fix

- Separate authoritative docs from user-generated content.
- Preserve source trust metadata.
- Label retrieved content.
- Do not allow retrieved content to trigger actions.
- Apply post-retrieval policy checks.

## Attack path 3 — Cross-team document leakage

### Goal

Show that semantic similarity is not authorization.

### Path

1. User from Team A asks about a service owned by Team B.
2. Vector search returns Team B document chunks.
3. The model summarizes the unauthorized content.
4. Student identifies missing document-level authorization.

### Root cause

Chunk metadata does not preserve access-control requirements, or filters are applied too late.

### Expected fix

- Metadata-preserving chunking.
- Pre-retrieval authorization filters.
- Post-retrieval authorization checks.
- Separate indexes for high-sensitivity domains where needed.

## Attack path 4 — Tool confused deputy

### Goal

Show that the model must not become a privileged deputy for the user.

### Path

1. User asks BrokenPilot to update a ticket outside their team.
2. Model requests `tickets.update`.
3. Tool gateway executes using the BrokenPilot service account.
4. Ticket is updated even though the user could not update it directly.

### Root cause

Tool authorization is based on service account capability, not user/action/object policy.

### Expected fix

- Delegated user authorization.
- Per-action and per-object checks.
- Scoped tool tokens.
- Approval workflow for high-risk updates.
- Full audit trail.

## Attack path 5 — Memory poisoning

### Goal

Show how persistent AI memory can become a long-lived attack path.

### Path

1. Attacker tells BrokenPilot to remember a malicious preference.
2. Memory is stored without review or expiry.
3. In later sessions, the assistant uses that memory to alter behavior.
4. Student traces the effect back to the poisoned memory.

### Root cause

Memory is treated as trusted context without provenance or lifecycle controls.

### Expected fix

- Explicit confirmation before memory writes.
- Memory scope, source, expiry, and review state.
- User-visible memory management.
- Memory never overrides policy.

## Attack path 6 — Overreliance and wrong incident summary

### Goal

Show that fluent model output can cause operational harm even without a classic exploit.

### Path

1. BrokenPilot summarizes an incident using incomplete or stale sources.
2. The summary omits a caveat or suggests the wrong owner.
3. The team relies on the summary without checking sources.
4. Student explains the workflow failure.

### Root cause

Generated summaries are not clearly marked as drafts and do not expose source freshness or uncertainty.

### Expected fix

- Source links.
- Freshness indicators.
- Human review before operational updates.
- Confidence/uncertainty language.
- Explicit statement of missing data.

## Attack path 7 — Model/tool denial of service

### Goal

Show that AI systems need cost, token, and tool-call controls.

### Path

1. User submits a request that triggers repeated planning and retrieval.
2. The assistant loops between retrieval and tool calls.
3. Token/tool budget is exhausted or response latency spikes.
4. Student identifies missing rate limits and loop controls.

### Root cause

Agent workflow lacks budgets, timeouts, and maximum tool-call depth.

### Expected fix

- Token budgets.
- Tool-call limits.
- Timeouts.
- Loop detection.
- Rate limiting and abuse monitoring.

## Attack path 8 — Sensitive config disclosure

### Goal

Show that AI tools should return least-privilege views, not raw backend data.

### Path

1. User asks about production service configuration.
2. `config.lookup` returns raw dependency and environment details.
3. Model summarizes sensitive topology or secret-like fields.
4. Student proposes redaction and role-specific views.

### Root cause

Tool output is not filtered before model exposure.

### Expected fix

- Redaction before model context.
- Role-based config views.
- Separate production access policy.
- Logging of sensitive config reads.

## Instructor note

Students should not be graded on producing clever payloads. They should be graded on explaining:

- Why the attack worked.
- Which trust boundary failed.
- Which assumption was unsafe.
- Which control would stop the class of issue.
- What residual risk remains.
