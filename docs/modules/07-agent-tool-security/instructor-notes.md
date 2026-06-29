# Module 07 Instructor Notes — Agent and Tool Security

## Teaching intent

This module should shift students from “LLM says bad thing” to “LLM causes system action.” The instructor should repeatedly bring the class back to architecture, identity, tool boundaries, authorization, approval, logging, and incident response.

The strongest mental model is:

> Treat agents as semi-autonomous operational actors with tools, credentials, memory, and workflow impact.

## Suggested timing

| Section | Time |
|---|---:|
| Why agents are different | 10 min |
| Agent architecture | 10 min |
| Risk categories | 20 min |
| Tool and identity design | 20 min |
| Memory, approval, and audit | 20 min |
| Exercise setup | 10 min |
| Group work | 35 min |
| Debrief | 25 min |

Total: approximately 2.5 hours.

## Instructor framing

Start with a simple contrast:

- A chatbot can produce a misleading answer.
- An agent can produce a misleading answer and then act on it.

That difference changes the security model. The model output is no longer the only concern. The action taken by the system is the concern.

## Key teaching points

### 1. The model is not an authorization engine

Students may suggest asking the model whether an action is safe. Push back. The model can provide context, but authorization must be enforced outside the model.

Good wording:

> The model can recommend. The policy layer decides. The tool broker enforces.

### 2. Tool scope matters more than prompt wording

A strong prompt around a dangerous tool is still a weak control.

A weaker prompt around a narrow, well-authorized tool may be safer.

### 3. Broad tools are dangerous

Examples to challenge:

- `run_shell(command)`
- `query_database(sql)`
- `send_email(to, subject, body)`
- `read_file(path)`
- `update_record(table, id, fields)`

Ask:

- Can this be authorized safely?
- Can the arguments be validated?
- Can the blast radius be limited?
- Can the result be rolled back?

### 4. Memory must have trust levels

Memory should not be a magic notebook where anything can persist forever.

Memory controls should include:

- source;
- owner;
- scope;
- timestamp;
- confidence;
- trust level;
- review status;
- expiration;
- deletion path.

### 5. Approval gates must show evidence

A bad approval gate says:

> The agent wants to do this. Approve?

A good approval gate shows:

- action;
- target;
- exact arguments;
- reason;
- evidence;
- risk tier;
- diff from current state;
- rollback path;
- who requested it;
- what policy was applied.

### 6. Audit logs are product features

Agents need explainability for operational accountability. Security logs are not only for compliance. They help debug unsafe automation and restore trust.

## Discussion prompts

Use these when students jump too quickly to solutions:

1. What identity is the agent using?
2. Is the action being performed as the user, as the agent, or as a shared service account?
3. Who owns the target object?
4. Could a malicious document cause this action?
5. Can this tool be safely exposed to a model?
6. What is the smallest tool that would satisfy the use case?
7. What would an audit reviewer need to understand later?
8. How would you stop this agent during an incident?
9. What happens if the agent is correct but the user is unauthorized?
10. What happens if the user is authorized but the retrieved context is malicious?

## Common student mistakes

| Mistake | How to correct it |
|---|---|
| “Improve the system prompt.” | Ask what enforces the rule if the model ignores it. |
| “Let the model decide if approval is needed.” | Move approval policy outside the model. |
| “Use one service account for everything.” | Introduce scoped, attributable credentials. |
| “Log the whole prompt and context.” | Discuss sensitive logging and minimization. |
| “Disable all tools.” | Balance security and usefulness with risk tiers. |
| “Require approval for everything.” | Discuss friction and developer velocity. |
| “Trust internal documents.” | Remind them indirect prompt injection can come from internal content. |
| “Memory is just personalization.” | Treat memory as persistence and therefore an attack surface. |

## Debrief structure

During the exercise debrief, ask each group to present:

1. Their highest-risk tool.
2. Their worst abuse case.
3. Their permission model.
4. Their approval policy.
5. Their memory policy.
6. Their logging strategy.
7. One residual risk they accept.

## Instructor answer pattern

A strong solution should include:

- user identity and agent identity separation;
- narrow tools;
- per-action authorization;
- object-level authorization;
- argument validation;
- read/write separation;
- risk-tiered approval;
- memory provenance and expiry;
- sandboxing for diagnostics;
- egress restrictions;
- audit logs;
- monitoring for tool abuse;
- kill switch;
- rollback plan;
- residual risk explanation.

## Optional advanced discussion

For senior students, extend the exercise into:

- multi-agent communication;
- MCP/A2A-style tool ecosystems;
- agent supply chain;
- agent identity lifecycle;
- delegated authorization;
- policy-as-code;
- AI incident response;
- red-team test plans for agentic workflows.

## Instructor caution

Keep the lab local and fake-data only. Students can safely explore goal hijacking, tool misuse, and memory poisoning without touching real systems.

The goal is not to teach students to attack production agents. The goal is to teach them how to design, review, and test agentic systems responsibly.

## Validated BrokenPilot tool authorization demo

Use `brokenpilot-tool-validation.md` as the validated demo anchor for this module.

Recommended delivery flow:

1. Explain the confused-deputy pattern before showing the app.
2. Show Alice's tenant and the target ticket's tenant.
3. Run the vulnerable request with `ENABLE_TOOL_AUTHZ=false`.
4. Ask students which security property was violated.
5. Restart with `ENABLE_TOOL_AUTHZ=true`.
6. Repeat the same request.
7. Show the `403` response and the reason fields.
8. Ask students why the control belongs in the tool or policy layer rather than the prompt.

Expected student insight:

> The model may propose or trigger an action, but authorization must be enforced at the action boundary.

This demo can be used in a short format because it has a clear before/after result and does not require students to complete the entire BrokenPilot capstone.
