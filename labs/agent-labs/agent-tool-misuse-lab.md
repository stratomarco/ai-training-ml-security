# Lab — Agent Tool Misuse and Excessive Agency

## Module

Module 07 — Agent and Tool Security

## Lab goal

Demonstrate how a tool-using agent can misuse legitimate tools when permissions, authorization, validation, and approval gates are weak.

The lab is conceptual and can be implemented using DVAIA, a local toy agent, or the future BrokenPilot capstone. It should use only fake data and simulated tools.

## Scenario

OpsAgent helps engineers manage internal incidents.

Available tools:

```text
read_ticket(ticket_id)
update_ticket(ticket_id, fields)
search_docs(query)
send_channel_message(channel, message)
run_diagnostic(command, target)
save_memory(key, value)
```

The tools are intentionally over-broad.

## Fake assets

- Fake incident tickets
- Fake internal documents
- Fake team channels
- Fake service targets
- Fake diagnostic outputs
- Fake memory store

## Vulnerabilities demonstrated

| Vulnerability | Description |
|---|---|
| Excessive agency | Agent can perform actions without approval. |
| Tool misuse | Legitimate tools can be used in unsafe ways. |
| Weak authorization | Tool calls are not checked per user/action/object. |
| Dangerous tool design | Free-form diagnostic command accepts unsafe input. |
| Indirect prompt injection | Retrieved docs or tickets can influence tool use. |
| Weak audit | Logs do not explain why an action occurred. |

## Student tasks

### Task 1 — Map tool risk

Create a table:

| Tool | Asset | Risk | Abuse case | Control |
|---|---|---|---|---|
| update_ticket | Incident integrity | High | Close incident incorrectly | Approval + field allowlist |
| send_channel_message | Internal comms | High | Send false alert | Approval + channel allowlist |
| run_diagnostic | Service config | Critical | Expose sensitive output | Allowlisted diagnostics + sandbox |

### Task 2 — Identify unsafe tool calls

Students review a set of proposed agent actions and mark them:

- allow;
- deny;
- require approval;
- require narrower tool;
- require additional evidence.

### Task 3 — Redesign tools

Replace broad tools with narrower tools.

Examples:

```text
update_ticket(ticket_id, fields)
```

becomes:

```text
add_ticket_comment(ticket_id, comment)
set_ticket_status(ticket_id, status, reason)
assign_ticket(ticket_id, assignee_id)
```

and:

```text
run_diagnostic(command, target)
```

becomes:

```text
run_approved_diagnostic(check_name, target_id)
```

### Task 4 — Add approval gates

Define which actions require approval.

| Action | Approval? | Why |
|---|---|---|
| Summarize ticket | No | Read-only low impact |
| Add internal comment | Maybe | Depends on ticket severity |
| Close incident | Yes | Operational impact |
| Send channel message | Yes for broad channels | Can mislead teams |
| Run diagnostic | Yes for high-risk checks | Execution and data exposure risk |

### Task 5 — Define audit logs

Define the minimum audit event.

```json
{
  "event_type": "agent_tool_call",
  "user_id": "fake-user",
  "agent_id": "opsagent-training",
  "tool": "set_ticket_status",
  "target": "INC-1001",
  "arguments_summary": "status=resolved",
  "policy_decision": "approval_required",
  "approval_id": "APP-2001",
  "result": "not_executed_pending_approval",
  "correlation_id": "training-123"
}
```

Do not include real secrets or sensitive data in logs.

## Expected mitigation design

A good solution includes:

- scoped agent identity;
- user delegation where appropriate;
- per-action authorization;
- object-level authorization;
- narrow tools;
- strict schemas;
- allowlisted targets;
- approval gates;
- safe audit logs;
- sandboxing;
- kill switch;
- rollback plan.

## Debrief questions

1. Which tool created the largest blast radius?
2. Which tool should be removed entirely?
3. Which tool can be saved by narrowing its interface?
4. Which actions need approval?
5. What should be monitored in production?
6. What residual risk remains after your design?
