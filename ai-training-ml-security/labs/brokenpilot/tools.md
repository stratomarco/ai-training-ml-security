# BrokenPilot Tool Inventory

BrokenPilot is risky because it can act. This file defines the intended tool model for the capstone.

## Tool design principle

The model may request a tool call, but deterministic backend code must decide whether the action is allowed.

Authorization must be based on the real user, target object, action, risk tier, and approval state. The model's explanation is useful context, not an authorization decision.

## Tool inventory

| Tool | Example action | Risk tier | Notes |
|---|---|---:|---|
| `docs.search` | Search documents | Low/Medium | Risk depends on authorization and classification. |
| `docs.read` | Read document by ID | Medium | Must enforce document-level access. |
| `tickets.search` | Search tickets | Medium | May expose sensitive tickets. |
| `tickets.read` | Read ticket | Medium | Must enforce team/customer/security access. |
| `tickets.create` | Create ticket | Medium | Can cause workflow spam or social engineering. |
| `tickets.update` | Change title/body/status/priority/owner | Medium/High | High risk when changing priority/status/owner. |
| `incidents.search` | Search incidents | Medium | Active incidents are sensitive. |
| `incidents.summarize` | Generate summary | Medium/High | Wrong summaries can affect decisions. |
| `config.lookup` | Read service configuration | Medium/High | May expose topology or secrets if not filtered. |
| `memory.read` | Read user/team memory | Medium | Scope and provenance required. |
| `memory.write` | Store memory | Medium/High | Persistent poisoning risk. |
| `notify.send` | Send Slack/email-style notification | High | Can amplify malicious or wrong content. |
| `postmortem.draft` | Draft postmortem | Medium | Must be clearly marked as draft. |

## Risk tiers

| Tier | Description | Examples | Required control |
|---|---|---|---|
| Low | Read-only, non-sensitive, reversible | Search public internal docs | Log only. |
| Medium | Read sensitive data or create low-impact artifacts | Read team ticket, create internal task | Authorization and audit. |
| High | Modify workflow, notify others, affect incident handling | Change priority, send notification, write team memory | Explicit confirmation or approval. |
| Critical | Destructive, broad, production-impacting, or secret-bearing | Delete data, rotate secrets, deploy code | Not available to BrokenPilot in this capstone. |

## Expected safe behavior

| Operation | Expected safe behavior |
|---|---|
| Read document | Apply document-level authorization before retrieval and before final answer. |
| Retrieve vector chunks | Filter by metadata before similarity ranking when possible; enforce post-retrieval checks too. |
| Create ticket | Require clear user intent and show preview. |
| Update ticket priority | Require confirmation for medium impact and approval for high/critical priority. |
| Send notification | Require approval and display exact message before sending. |
| Write memory | Require explicit user confirmation, provenance, scope, and expiry. |
| Use config lookup | Redact secrets and restrict production details by role/team. |

## Intentionally vulnerable tool behaviors

The vulnerable design may include:

1. `tickets.update` trusts a model-proposed action without checking whether the user can perform the update directly.
2. `docs.search` retrieves chunks by semantic similarity without applying team/classification metadata.
3. `memory.write` stores model-inferred instructions without user confirmation.
4. `notify.send` accepts generated text without human approval.
5. `config.lookup` returns too much detail for production services.
6. `tickets.create` allows untrusted ticket content to become future RAG instructions.
7. Tool-call logs record that BrokenPilot performed an action but not the real user or source prompt.

## Tool permission matrix

| Tool | Engineer | SRE | Security | Support | Manager | Admin |
|---|---|---|---|---|---|---|
| `docs.search` | Own team + public | Ops + own team + public | Security + relevant docs | Support + public | Team summaries | All public/admin docs |
| `docs.read` | Own team + public | Ops + own team | Security + relevant docs | Support docs | Team docs | Configurable |
| `tickets.search` | Own team | Ops tickets | Security tickets + relevant | Support tickets | Team metadata | Configurable |
| `tickets.read` | Own team | Ops tickets | Security tickets + relevant | Support tickets | Team metadata | Configurable |
| `tickets.create` | Yes | Yes | Yes | Yes | Yes | Yes |
| `tickets.update` | Own team, limited fields | Ops tickets, controlled | Security tickets, controlled | Support tickets, limited | No direct update | Admin config only |
| `incidents.search` | Limited | Yes | Relevant | Limited | Summary only | Configurable |
| `incidents.summarize` | Limited | Yes | Relevant | Limited | Summary only | Configurable |
| `config.lookup` | Own team non-secret | Ops non-secret | Relevant non-secret | No | Summary only | Admin view without secrets |
| `memory.read` | Own memory | Own/team memory | Own/team memory | Own memory | Own memory | Policy only |
| `memory.write` | Own memory with confirmation | Own/team memory with approval | Own/team memory with approval | Own memory with confirmation | Own memory with confirmation | Policy only |
| `notify.send` | Approval required | Approval required | Approval required | Approval required | Approval required | Approval required |

## Student task

Students should review the tool inventory and answer:

1. Which tools can change system state?
2. Which tools can expose sensitive information?
3. Which tools need approval gates?
4. Which tools should not exist in the first version?
5. Which tool arguments need validation?
6. What should be logged for each tool call?
7. What rollback is possible?
