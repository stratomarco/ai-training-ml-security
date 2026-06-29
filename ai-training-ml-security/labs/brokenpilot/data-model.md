# BrokenPilot Data Model

This file defines the fake data concepts used by the BrokenPilot capstone. The paper design does not require real production data.

## Entity overview

```text
User
Team
Document
DocumentChunk
Ticket
Incident
ServiceConfig
MemoryEntry
ToolCall
AuditEvent
ApprovalRequest
```

## User

| Field | Example | Notes |
|---|---|---|
| user_id | `u-1042` | Stable internal ID. |
| email | `alex@northwind.example` | Fake address only. |
| display_name | `Alex Rivera` | Student-facing examples may use fake names. |
| role | `engineer`, `sre`, `security`, `support`, `manager`, `admin` | Used for policy. |
| teams | `payments`, `platform` | Used for document and ticket authorization. |
| risk_flags | `contractor`, `oncall`, `break_glass` | Optional policy attributes. |

## Team

| Field | Example | Notes |
|---|---|---|
| team_id | `payments` | Team identifier. |
| name | `Payments Platform` | Display name. |
| data_scope | `payments-*` | Used for simple authorization examples. |

## Document

| Field | Example | Notes |
|---|---|---|
| doc_id | `doc-2001` | Stable document ID. |
| title | `Payments Runbook` | Display title. |
| owner_team | `payments` | Important for authorization. |
| classification | `public-internal`, `team-confidential`, `security-confidential` | Used for access control. |
| source | `wiki`, `ticket`, `email`, `manual-upload` | Trust and provenance. |
| created_by | `u-1042` | Provenance. |
| last_reviewed | `2026-06-01` | Staleness indicator. |
| content | Markdown text | May contain malicious instructions in vulnerable lab. |

## DocumentChunk

| Field | Example | Notes |
|---|---|---|
| chunk_id | `chunk-2001-03` | Chunk ID. |
| doc_id | `doc-2001` | Must preserve link to source document. |
| text | Chunk text | Retrieved into model context. |
| embedding_id | `emb-7781` | Vector DB reference. |
| metadata | owner, classification, source, allowed_teams | Required for secure retrieval. |

## Ticket

| Field | Example | Notes |
|---|---|---|
| ticket_id | `TCK-8842` | Ticket ID. |
| title | `Payment API latency` | User-visible title. |
| body | Markdown text | May contain malicious instructions. |
| status | `open`, `investigating`, `blocked`, `resolved` | Update requires permission. |
| priority | `low`, `medium`, `high`, `critical` | High-risk update. |
| owner_team | `payments` | Authorization boundary. |
| customer_visible | `true` / `false` | Sensitive output risk. |
| created_by | `u-1042` | Provenance. |
| last_updated_by | `brokenpilot-service` or user | Audit concern. |

## Incident

| Field | Example | Notes |
|---|---|---|
| incident_id | `INC-2026-0017` | Incident ID. |
| severity | `sev1`, `sev2`, `sev3` | Determines approval and notification risk. |
| affected_services | `payments-api`, `ledger-worker` | Sensitive operational metadata. |
| status | `active`, `mitigated`, `resolved` | Updates are high-impact. |
| commander | `u-2048` | Responsible person. |
| timeline | Event list | Used for summaries. |
| postmortem_draft | Markdown | Model-generated draft may be wrong. |

## ServiceConfig

| Field | Example | Notes |
|---|---|---|
| service_id | `payments-api` | Service name. |
| owner_team | `payments` | Authorization boundary. |
| environment | `dev`, `staging`, `prod` | Production config is sensitive. |
| dependencies | `auth-service`, `ledger-db` | Internal topology disclosure. |
| secrets_present | `false` | Secrets should never be returned. |
| deployment_strategy | `blue-green` | Useful operational context. |

## MemoryEntry

| Field | Example | Notes |
|---|---|---|
| memory_id | `mem-4409` | Memory ID. |
| scope | `user`, `team`, `workspace` | Higher scope is higher risk. |
| owner | `u-1042` or `payments` | Authorization boundary. |
| text | `Alex prefers concise incident summaries.` | Could be poisoned. |
| source | `explicit-user-confirmation`, `model-inferred`, `imported` | Trust level. |
| created_at | timestamp | For expiry. |
| expires_at | timestamp | Required for safe memory. |
| reviewed | `true` / `false` | Whether user approved. |

## ToolCall

| Field | Example | Notes |
|---|---|---|
| tool_call_id | `tc-9001` | ID. |
| user_id | `u-1042` | Real user. |
| tool_name | `ticket.update` | Tool. |
| action | `set_priority` | Specific action. |
| target_object | `TCK-8842` | Object. |
| arguments | JSON | Must be validated. |
| model_reason | text | Helpful but not authoritative. |
| policy_decision | `allow`, `deny`, `approval_required` | Deterministic decision. |
| approval_id | `apr-1221` | If needed. |

## AuditEvent

| Field | Example | Notes |
|---|---|---|
| event_id | `evt-7001` | ID. |
| timestamp | ISO timestamp | Required. |
| actor_user_id | `u-1042` | Real user. |
| actor_service | `brokenpilot-api` | Calling service. |
| event_type | `tool_call`, `retrieval`, `policy_denial`, `memory_write` | Security signal. |
| target | object ID | What changed or was accessed. |
| result | `success`, `blocked`, `failed` | Useful for detection. |
| correlation_id | request/session ID | Investigation support. |

## Data classification

| Classification | Examples | Expected treatment |
|---|---|---|
| Public internal | General engineering docs | Accessible to all employees. |
| Team confidential | Runbooks, team tickets | Restricted by team. |
| Security confidential | Vulnerability reports, security tickets | Restricted to security and relevant owners. |
| Incident sensitive | Active incident details | Restricted and time-sensitive. |
| Customer sensitive | Customer escalations | Access controlled and minimized. |
| Secret | API keys, tokens, passwords | Never exposed to model or users. |

## Common data-model flaws to look for

Students should look for:

- Chunks that lose document-level authorization metadata.
- Tickets indexed into RAG without sanitization or classification.
- Memories without scope, provenance, review, or expiry.
- Audit logs that omit the real user behind a model action.
- Config records that contain secrets or sensitive topology.
- Model-generated summaries stored as if they were authoritative facts.
