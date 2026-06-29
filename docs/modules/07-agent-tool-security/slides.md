# Module 07 Slides — Agent and Tool Security

## Slide 1 — Title

# Agent and Tool Security

Security engineering for AI systems that can act.

---

## Slide 2 — Why this module matters

A chatbot produces text.

An agent can take action.

That action may affect:

- tickets;
- documents;
- email;
- chat;
- code repositories;
- cloud resources;
- customer records;
- operational systems;
- money;
- safety-critical workflows.

Once the AI can act, the system has a new operational actor.

---

## Slide 3 — The key security shift

Traditional LLM application question:

> What can the model say?

Agentic application question:

> What can the model cause the system to do?

That second question is much more dangerous.

---

## Slide 4 — Core thesis

# The model is not the security boundary.

The model may decide what it wants to do.

The application must enforce what it is allowed to do.

---

## Slide 5 — Reference architecture

```text
user
  |
  v
agent interface
  |
  +-- LLM / model gateway
  +-- orchestration layer
  +-- memory service
  +-- retrieval service
  +-- policy layer
  +-- tool broker
  |     +-- email tool
  |     +-- ticket tool
  |     +-- browser tool
  |     +-- shell/code tool
  |     +-- internal API tool
  +-- audit log
  +-- monitoring
  +-- approval workflow
```

---

## Slide 6 — What makes agents different?

Agents combine:

- language understanding;
- planning;
- tool calling;
- memory;
- external data;
- autonomy;
- workflow execution;
- sometimes multi-agent coordination.

Each capability adds an attack surface.

---

## Slide 7 — Capability-to-risk map

| Capability | Security risk |
|---|---|
| Tool calling | Unauthorized or unsafe action |
| Memory | Persistent poisoning |
| Planning | Goal drift or harmful action chain |
| Browsing | Indirect prompt injection |
| Code execution | RCE, sandbox escape, data leakage |
| Email/chat | Social engineering and exfiltration |
| Multi-agent | Spoofing, trust confusion, cascading failures |

---

## Slide 8 — Classic security still applies

| Classic principle | Agent interpretation |
|---|---|
| Least privilege | Give only task-specific tools and scopes. |
| Complete mediation | Authorize every tool call. |
| Fail-safe defaults | Deny unclear or unsafe actions. |
| Separation of duties | Model proposes; policy enforces. |
| Defense in depth | Prompts, policy, validation, approvals, logs. |
| Auditability | Every meaningful action must be attributable. |

---

## Slide 9 — Agent risk categories

Important risk patterns:

- goal hijacking;
- tool misuse;
- identity and privilege abuse;
- agentic supply chain compromise;
- unexpected code execution;
- memory and context poisoning;
- insecure inter-agent communication;
- cascading failures;
- human-agent trust exploitation;
- rogue or misaligned agent behavior.

---

## Slide 10 — Goal hijacking

Goal hijacking occurs when the agent's intended objective is replaced or distorted by attacker-controlled input.

Example pattern:

1. Agent is asked to summarize a ticket.
2. Ticket contains malicious instructions.
3. Agent follows the ticket instead of the user/system goal.
4. Agent leaks information or performs the wrong action.

Root cause: untrusted content is treated as instruction.

---

## Slide 11 — Tool misuse

Tool misuse happens when an agent uses legitimate tools in unsafe ways.

Examples:

- sending an email to the wrong recipient;
- deleting or closing a ticket without approval;
- querying more records than needed;
- using a diagnostic tool to expose secrets;
- chaining harmless tools into harmful workflow impact.

The tool is legitimate. The composition is unsafe.

---

## Slide 12 — Identity and privilege abuse

Agents need identities.

Bad designs use:

- shared service accounts;
- broad API tokens;
- long-lived credentials;
- no per-user delegation;
- no per-action authorization;
- no audit attribution.

Better designs use scoped, short-lived, task-specific credentials with clear attribution.

---

## Slide 13 — Memory poisoning

Memory is useful because it persists context.

Memory is dangerous because it persists attacker influence.

Risk patterns:

- malicious user preference saved as memory;
- poisoned project instructions;
- false facts used in future decisions;
- long-lived hidden instructions;
- cross-user memory contamination.

Memory should have trust levels, provenance, review, and deletion.

---

## Slide 14 — Tool schemas are not enough

A schema tells the model the shape of a call.

It does not automatically enforce:

- authorization;
- business rules;
- target ownership;
- safe recipient lists;
- rate limits;
- approval requirements;
- data classification;
- audit requirements.

Schemas help. Policy enforces.

---

## Slide 15 — Bad tool design

Dangerous tool examples:

```text
run_shell(command: string)
query_database(sql: string)
send_email(to: string, body: string)
update_any_ticket(id: string, fields: object)
read_any_document(path: string)
```

These tools are broad, ambiguous, and hard to authorize safely.

---

## Slide 16 — Better tool design

Prefer narrow tools:

```text
get_ticket_summary(ticket_id)
add_internal_ticket_comment(ticket_id, comment)
create_low_priority_followup_ticket(title, description)
search_docs(query, allowed_sources)
run_approved_diagnostic(check_name, target_id)
```

Specific tools are easier to validate, authorize, monitor, and explain.

---

## Slide 17 — Per-action authorization

Do not ask only:

> Can this user use the agent?

Ask:

> Can this user, through this agent, perform this exact action on this exact object with these exact arguments right now?

That is complete mediation for agent systems.

---

## Slide 18 — Approval gates

Require human approval for actions that are:

- destructive;
- externally visible;
- expensive;
- privileged;
- irreversible;
- sensitive;
- high-volume;
- cross-tenant;
- compliance-relevant.

The agent can prepare. Humans approve.

---

## Slide 19 — Human-agent trust exploitation

Agents can sound confident even when wrong.

Risk:

- operator approves harmful action;
- agent invents justification;
- agent hides uncertainty;
- agent compresses risk away in summaries;
- agent makes dangerous action look routine.

Mitigation: show evidence, uncertainty, source links, and action diffs.

---

## Slide 20 — Logging and audit

Log:

- user request;
- retrieved context references;
- model decision summary;
- tool selected;
- tool arguments;
- policy decision;
- approval decision;
- action result;
- actor identity;
- target object;
- timestamps;
- correlation IDs.

Avoid logging unnecessary sensitive content.

---

## Slide 21 — Sandboxing and egress control

For code, shell, browser, or file tools:

- isolate execution;
- remove secrets;
- restrict filesystem access;
- restrict network egress;
- set time and cost limits;
- capture artifacts;
- reset state after execution;
- monitor abuse.

Never give the agent a production shell because it is convenient.

---

## Slide 22 — Detection ideas

Monitor for:

- unusual tool sequences;
- repeated approval requests;
- unexpected recipients;
- cross-tenant access;
- high-volume retrieval;
- memory updates from untrusted input;
- policy denials;
- loops and runaway execution;
- tool arguments containing instructions or secrets;
- unusual cost or token spikes.

---

## Slide 23 — Kill switch and rollback

Agents need operational controls.

Include:

- disable all tools;
- disable one tool;
- disable one agent;
- revoke credentials;
- freeze memory writes;
- stop scheduled tasks;
- revert agent-created changes;
- preserve forensic logs.

Incident response must be designed before the incident.

---

## Slide 24 — Secure reference pattern

```text
model suggests action
  |
  v
policy checks user + agent + object + action + args
  |
  +-- deny -> explain safely
  |
  +-- needs approval -> human review with evidence
  |
  +-- allow -> execute via narrow scoped tool
                      |
                      v
                audit + monitor + rollback metadata
```

---

## Slide 25 — Practical balance

Too much friction kills adoption.

Too little control creates incidents.

Good agent security uses risk tiers:

| Tier | Example | Control |
|---|---|---|
| Low | summarize public doc | allow and log |
| Medium | comment on internal ticket | scoped authorization |
| High | email customer | approval gate |
| Critical | delete resource | approval + break-glass + rollback |

---

## Slide 26 — Exercise

Design controls for an internal operations agent.

The agent can:

- read incidents;
- search docs;
- update tickets;
- notify teams;
- save memory;
- run diagnostics.

Your job:

1. Map tools and permissions.
2. Identify abuse cases.
3. Define approval gates.
4. Define memory policy.
5. Define audit and rollback.

---

## Slide 27 — What good looks like

A good answer includes:

- clear trust boundaries;
- tool inventory;
- scoped permissions;
- per-action authorization;
- validation of tool arguments;
- human approval for sensitive actions;
- memory provenance;
- monitoring;
- incident response;
- residual risk.

---

## Slide 28 — Closing message

Agent security is not solved by better prompts.

Agent security is solved by secure workflow design.

The model can plan.

The system must govern.
