# Strong Example  -  BrokenPilot Tool Permission Matrix

This is an example of a strong tool permission matrix for the BrokenPilot capstone.

A strong matrix is not just a list of tools. It says who can invoke each tool, under which conditions, what approval is required, what data the tool can access, and what must be logged.

## Context

BrokenPilot supports engineering and operations users across multiple tenants. The risky tool in this example is `update_ticket`, which can modify operational records.

## Tool permission matrix

| Tool | Allowed callers | Required scope | Allowed target objects | Approval required | Deny conditions | Audit events |
|---|---|---|---|---|---|---|
| `search_docs` | `ops`, `engineer` | `docs:read` | Documents in caller tenant only | No | Missing tenant metadata; target document tenant differs from caller tenant | caller, query, tenant, document IDs returned, denied document count |
| `read_ticket` | `ops`, ticket owner, assigned engineer | `tickets:read` | Tickets in caller tenant only | No | Caller tenant differs from ticket tenant | caller, ticket ID, tenant, decision |
| `update_ticket` | `ops` only | `tickets:update` | Tickets in caller tenant only | Yes for `closed`, `deleted`, `escalated`; no for adding non-destructive notes | Caller tenant differs from ticket tenant; caller role not `ops`; model-supplied ticket ID not confirmed by user or policy | caller, ticket ID, old status, new status, approval ID, policy decision, source of ticket ID |
| `create_ticket` | `ops`, `engineer` | `tickets:create` | New ticket in caller tenant only | No unless priority is `critical` | Tenant field differs from caller tenant; missing owner; missing business justification for critical priority | caller, created ticket ID, tenant, priority, justification |
| `store_memory` | authenticated users | `memory:write` | User-scoped memory only by default | Yes for global or tenant-wide memory | Request attempts global memory; content contains imperative instruction; content references credentials, secrets, or authorization bypass | caller, memory scope, review status, detected risk flags |

## Concrete policy rule examples

```text
Rule TICKET-UPDATE-001:
Allow update_ticket only if:
- caller.role == "ops"
- caller.tenant == ticket.tenant
- caller has scope "tickets:update"
- requested status transition is allowed
- if status in ["closed", "deleted", "escalated"], approval.status == "approved"
```

```text
Rule TOOL-SOURCE-002:
If a tool argument was derived from model output, retrieved content, or memory,
then require policy validation before execution.
The model's selection of a tool argument is never authorization evidence.
```

```text
Rule MEMORY-001:
Global memory is disabled by default.
Tenant-wide memory requires review.
User-scoped memory must not be used as instruction authority for tool execution.
```

## Why this is strong

This is strong because it is implementable. An engineer can translate these rules into middleware, policy checks, tests, and audit events.

It also separates three things that are often confused:

1. The user's request.
2. The model's interpretation of the request.
3. The system's authorization decision.

Only the third one should decide whether a tool action is allowed.
