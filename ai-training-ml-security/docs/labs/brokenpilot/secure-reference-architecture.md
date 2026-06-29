# BrokenPilot Secure Reference Architecture

## Design goal

BrokenPilot should remain useful while ensuring that model behavior does not become the security control.

The secure architecture should allow the assistant to help with search, summarization, drafting, and low-risk workflow actions while keeping data access, authorization, approval, and audit decisions in deterministic backend services.

## Reference flow

```text
user request
  |
  v
identity/session validation
  |
  v
request risk classification
  |
  v
retrieval policy decision
  |
  v
authorized retrieval only
  |
  v
context builder with source labels
  |
  v
model gateway
  |
  v
structured answer and proposed actions
  |
  v
policy engine evaluates proposed actions
  |
  +-- deny
  +-- answer only
  +-- ask user confirmation
  +-- create approval request
  +-- execute low-risk action
  |
  v
audit, monitoring, and user-visible result
```

## Required controls

### 1. Identity-bound tool execution

Every tool call must be bound to:

- Real user identity.
- User role.
- Team membership.
- Requested action.
- Target object.
- Risk tier.
- Approval state.

Do not execute actions only because the model requested them.

### 2. Policy engine outside the model

The model can propose actions. The policy engine decides whether the action is allowed.

Policy should cover:

- Tool availability.
- Object access.
- Action risk tier.
- Approval requirement.
- Rate limits.
- Data classification.
- Environment restrictions.

### 3. Retrieval authorization

Retrieval must enforce access before sensitive content reaches the model.

Required design:

- Preserve document metadata on chunks.
- Filter retrieval by user/team/classification.
- Re-check retrieved chunks before prompt construction.
- Keep high-sensitivity corpora separate where useful.
- Log retrieval access decisions.

### 4. Source-labeled context

The model context should clearly separate:

- System/developer instructions.
- User request.
- Retrieved documents.
- Tool outputs.
- Memory.
- Policy notices.

Retrieved content should be labeled as untrusted data, not instruction.

### 5. Risk-tiered approval gates

| Risk tier | Examples | Required behavior |
|---|---|---|
| Low | Search public docs, summarize own notes | Execute and log. |
| Medium | Read team ticket, create internal ticket | Confirm intent and log. |
| High | Update priority/status, send notification, write team memory | Require explicit approval. |
| Critical | Delete data, deploy code, rotate secrets, production changes | Not available to BrokenPilot. |

### 6. Safe memory design

Memory must be:

- Explicitly confirmed.
- Scoped to user/team/workspace.
- Source-labeled.
- Expiring by default.
- Inspectable and deletable.
- Unable to override policy.

### 7. Tool schema validation

Tools must validate:

- Required fields.
- Allowed values.
- Target object existence.
- User authorization.
- Argument length.
- Dangerous strings.
- Environment restrictions.

### 8. Sandboxing and egress control

If tools can execute code, fetch URLs, or transform files, they require:

- Sandboxed execution.
- No default network egress.
- File system isolation.
- Timeouts.
- Resource limits.
- Malware scanning where appropriate.

For the first BrokenPilot design, production-affecting code execution should not be available.

### 9. Audit logging

Audit events should record:

- Real user.
- Session/request ID.
- Model and prompt version.
- Retrieval index version.
- Retrieved document IDs.
- Tool name and arguments.
- Target object.
- Policy decision.
- Approval decision.
- Result.
- Timestamp.

Do not store raw sensitive prompts forever. Apply minimization, redaction, access control, and retention.

### 10. Monitoring and detection

Monitor for:

- Repeated policy denials.
- Cross-team retrieval attempts.
- Tool-call spikes.
- Unusual memory writes.
- High-risk action attempts.
- Prompt-injection patterns.
- Expensive token/tool loops.
- Sensitive config access.

## Secure UI requirements

The UI should:

- Clearly mark generated content.
- Show source references for factual claims.
- Mark incident summaries as drafts.
- Show exact diffs before updates.
- Explain when approval is required.
- Let users inspect and delete memory.
- Warn before using generated commands.

## Usability and velocity trade-offs

Security controls should be proportional:

- Do not require approval for every read-only search.
- Require confirmation for medium-risk actions.
- Require approval for high-risk workflow changes.
- Block critical production-impacting actions entirely in early versions.
- Use good defaults so developers do not need to design policy from scratch each time.

## Residual risk

Even with this design:

- Prompt injection can still influence text output.
- Retrieved content may still be stale or misleading.
- Human approvers may rubber-stamp actions.
- Logs may still create privacy risk if over-collected.
- Attackers may find new ways to phrase indirect instructions.
- The model may hallucinate or omit important caveats.

The purpose of the secure architecture is not to eliminate all AI risk. The purpose is to reduce high-impact failure paths and make remaining risk visible, monitored, and governable.
