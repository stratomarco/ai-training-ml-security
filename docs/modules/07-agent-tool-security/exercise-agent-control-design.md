# Exercise — Agent Control Design

## Scenario

You are reviewing **OpsAgent**, an internal AI agent used by engineering and operations.

OpsAgent can help with incidents and operational tickets.

It can:

- summarize incidents;
- search internal documentation;
- read tickets;
- add ticket comments;
- update ticket status;
- notify an internal team channel;
- save memory about user/team preferences;
- run approved diagnostic checks against fake services;
- draft follow-up tasks.

The company wants OpsAgent to reduce operational toil without creating unacceptable security risk.

## Current design

```text
engineer
  |
  v
OpsAgent chat UI
  |
  +-- LLM gateway
  +-- retrieval service over internal docs
  +-- memory service
  +-- tool broker
        +-- read_ticket(ticket_id)
        +-- update_ticket(ticket_id, fields)
        +-- search_docs(query)
        +-- send_channel_message(channel, message)
        +-- run_diagnostic(command, target)
        +-- save_memory(key, value)
```

## Known weaknesses

The current implementation has several intentional weaknesses:

1. The agent uses one shared service account.
2. The `update_ticket` tool can change any field.
3. The `send_channel_message` tool can send to any channel.
4. The `run_diagnostic` tool accepts free-form command text.
5. The `save_memory` tool can store information from any conversation or retrieved document.
6. Retrieved documents are not labeled as untrusted data.
7. There is no approval flow.
8. Logs record that a tool was used, but not why it was used.
9. There is no emergency way to disable one tool without disabling the whole agent.

## Task 1 — Architecture and trust boundaries

Draw or describe the system architecture.

Identify:

- users;
- model;
- orchestrator;
- tools;
- data stores;
- memory;
- retrieval content;
- external systems;
- policy enforcement points;
- audit logs.

Then mark the trust boundaries.

## Task 2 — Tool inventory

Create a tool inventory table.

| Tool | Read/write | Asset affected | Risk level | Notes |
|---|---|---|---|---|
| read_ticket | Read | Tickets | Medium | May expose sensitive incident data. |
| update_ticket | Write | Tickets | High | Can modify operational history. |
| search_docs | Read | Internal docs | Medium | May retrieve poisoned or unauthorized content. |
| send_channel_message | Write | Chat | High | Externally visible inside company. |
| run_diagnostic | Execute | Services | Critical | Free-form command-like behavior. |
| save_memory | Write | Agent memory | High | Persistent influence. |

Add or modify rows as needed.

## Task 3 — Abuse cases

Write at least five abuse cases.

Use this format:

```text
As an attacker, I want to [action] so that [impact].
```

Examples:

- As an attacker, I want to place instructions in a ticket so that OpsAgent sends sensitive information to a channel I control.
- As an attacker, I want OpsAgent to save malicious memory so that future sessions follow my instruction.
- As an attacker, I want to trigger a diagnostic command so that internal configuration is exposed.

## Task 4 — Permission matrix

Design a permission matrix for each tool.

Include:

- who can request it;
- which agent identity can execute it;
- target restrictions;
- argument validation;
- rate limits;
- approval requirement;
- logging requirement.

## Task 5 — Approval policy

Define which actions are:

| Risk tier | Example | Control |
|---|---|---|
| Low | summarize ticket | allow and log |
| Medium | add internal ticket comment | authorize and log |
| High | notify team channel | require approval or allowlist |
| Critical | run diagnostic | approval + sandbox + allowlisted checks |

Add your own tiers.

## Task 6 — Redesign the tools

Replace dangerous tools with narrower tools.

Example:

Current:

```text
run_diagnostic(command, target)
```

Safer:

```text
run_approved_diagnostic(check_name, target_id)
```

Current:

```text
send_channel_message(channel, message)
```

Safer:

```text
send_approved_incident_update(incident_id, channel_id, template_id, variables)
```

## Task 7 — Memory policy

Define how memory should work.

Answer:

1. What can be saved?
2. Who can save it?
3. Can retrieved documents write memory?
4. How is memory reviewed?
5. How does memory expire?
6. How can a user or admin delete it?
7. What memory changes require approval?

## Task 8 — Logging and monitoring

Define what gets logged.

At minimum:

- user identity;
- agent identity;
- tool name;
- target object;
- arguments or safe argument summary;
- policy decision;
- approval decision;
- result;
- timestamp;
- correlation ID.

Define at least five alerts.

Examples:

- high number of denied tool calls;
- repeated memory writes;
- unexpected channel target;
- diagnostic tool requested from retrieved context;
- cross-team ticket access.

## Task 9 — Kill switch and rollback

Design operational controls.

Include:

- disable one tool;
- disable one agent;
- freeze memory writes;
- revoke credentials;
- stop scheduled actions;
- undo agent-created ticket changes;
- preserve forensic logs.

## Task 10 — Residual risk

Write a short residual risk statement.

Include:

- what risk remains;
- why it remains;
- who accepts it;
- what monitoring or review is required;
- when the decision should be revisited.

## Expected deliverable

Submit an **agent control design** using the template:

`../../templates/agent-control-design-template.md`

Your design should include:

1. Architecture summary
2. Trust boundaries
3. Tool inventory
4. Abuse cases
5. Permission matrix
6. Approval policy
7. Memory policy
8. Logging and monitoring
9. Kill switch and rollback
10. Residual risk

## Validated hands-on extension — BrokenPilot tool authorization

After completing the design exercise, run the BrokenPilot prototype tool-calling lab and compare your design against the implemented control.

Use:

- `brokenpilot-tool-validation.md` for the validated Module 07 scenario;
- `../../labs/brokenpilot/prototype-app/TOOL_CALLING_LAB.md` for hands-on steps.

The required validation question is:

> Does the same cross-tenant ticket update succeed in vulnerable mode and fail after `ENABLE_TOOL_AUTHZ=true`?

Students should add both observations to their deliverable. A complete answer must include the vulnerable result, the controlled result, and the security property enforced by the control.
