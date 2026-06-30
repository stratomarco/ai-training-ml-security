# Module 07 Student Handout — Agent and Tool Security

## Core idea

A chatbot answers.

An agent acts.

That means an agent has a bigger attack surface because it may use tools, hold memory, make plans, interact with systems, and trigger business workflows.

## Main lesson

> The model can propose actions. The system must enforce policy.

Do not rely on the model alone to decide what is safe, authorized, or appropriate.

## Agent components

| Component | Security question |
|---|---|
| User interface | Who is asking and what are they allowed to request? |
| Model | What instructions and context influence the model? |
| Orchestrator | How are plans, steps, and tool calls selected? |
| Tool broker | Which tools exist and how are calls enforced? |
| Tools | What can each tool actually do? |
| Memory | What persists and who can influence it? |
| Retrieval | What external content can affect decisions? |
| Policy layer | What security rules are enforced outside the model? |
| Approval workflow | Which actions require human review? |
| Audit logs | Can actions be reconstructed later? |

## Common agent risks

| Risk | Short explanation |
|---|---|
| Goal hijacking | Attacker changes what the agent is trying to achieve. |
| Tool misuse | Agent uses a legitimate tool in an unsafe way. |
| Identity abuse | Agent has broad or poorly attributed privileges. |
| Memory poisoning | Malicious or false context persists across sessions. |
| Unexpected code execution | Agent triggers unsafe code, shell, or script behavior. |
| Insecure inter-agent communication | Agents trust messages from other agents too much. |
| Cascading failures | One bad action triggers more automated bad actions. |
| Human-agent trust exploitation | Human approves harmful action because the agent sounds confident. |
| Excessive agency | Agent has too much autonomy or too few constraints. |

## Secure tool design

Prefer narrow tools over broad tools.

Bad pattern:

```text
run_shell(command)
send_email(to, body)
query_database(sql)
update_any_record(table, id, fields)
```

Better pattern:

```text
run_approved_diagnostic(check_name, target_id)
send_internal_notification(group_id, approved_template_id, variables)
search_allowed_docs(query, source_scope)
add_ticket_comment(ticket_id, comment)
```

## Tool permission matrix

For each tool, define:

- allowed users;
- allowed agent roles;
- allowed targets;
- read/write scope;
- allowed arguments;
- rate limits;
- approval requirement;
- logging requirement;
- rollback support.

## Approval gates

Require approval for actions that are:

- destructive;
- externally visible;
- privileged;
- expensive;
- sensitive;
- irreversible;
- compliance-relevant;
- cross-tenant;
- high-volume.

A good approval prompt should show the exact action, target, arguments, evidence, risk tier, and rollback path.

## Memory policy

Memory should not blindly store everything.

For each memory item, track:

- source;
- owner;
- scope;
- trust level;
- creation time;
- expiry;
- review status;
- deletion path.

Do not allow untrusted retrieved content to silently create durable agent memory.

## Logging checklist

Log enough to reconstruct what happened:

- user;
- agent;
- action;
- target;
- arguments;
- policy decision;
- approval decision;
- tool result;
- timestamp;
- correlation ID.

Do not log unnecessary secrets, personal data, or full sensitive context.

## Design principle

A safe agent design should answer:

1. Who requested the action?
2. Which identity will perform it?
3. What object is affected?
4. Are the arguments valid?
5. Is approval needed?
6. What gets logged?
7. Can it be undone?
8. What happens if the agent is wrong?

## Deliverable for this module

You will produce an **agent control design** with:

- architecture diagram;
- tool inventory;
- permission matrix;
- approval policy;
- memory policy;
- monitoring plan;
- incident response plan;
- residual risk statement.


## Reading path for this module

Use the new deepening files before the hands-on BrokenPilot validation:

1. Read `deep-dive.md` to understand why agents change the security model.
2. Read `attack-anatomy.md` to map agent inputs to unsafe actions.
3. Read `controls-and-remediations.md` to understand what engineers should implement.
4. Review `common-mistakes.md` before doing the exercise.
5. Use `worked-example.md` as a model for strong findings.

## Key lesson from BrokenPilot validation

BrokenPilot validates two important Module 07 lessons:

- Missing tool authorization allows an `alpha` tenant user to update a `beta` tenant ticket.
- Memory poisoning can influence an agent's attempted action, but independent tool authorization can still block unsafe execution.

That is the core agent security pattern: the model and memory may be influenced, but the tool layer must still enforce policy.
