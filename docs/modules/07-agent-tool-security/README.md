# Module 07 — Agent and Tool Security

## Purpose

Teach why agentic systems are riskier than chatbots and how to secure LLM-driven tools, workflows, memory, and autonomous actions.

A chatbot mainly produces text. An agent can act. Once an LLM can call tools, create tickets, send messages, query systems, execute code, browse websites, update records, or coordinate with other agents, AI security becomes workflow security, identity security, and authorization design.

## Key message

> An agent is an application that can act. The model may choose the action, but the system must enforce what actions are allowed.

The model should not be the security boundary. Agent safety depends on controls around identity, authorization, tool design, policy enforcement, approval gates, logging, sandboxing, and rollback.

## Learning objectives

By the end of this module, students should be able to:

1. Explain why agents introduce higher risk than simple LLM applications.
2. Identify assets, trust boundaries, identities, tools, permissions, and high-impact actions in an agentic system.
3. Explain tool misuse, excessive agency, memory poisoning, goal hijacking, identity abuse, insecure inter-agent communication, and cascading failures.
4. Design tool permission boundaries using least privilege and per-action authorization.
5. Distinguish model decision-making from enforceable security policy.
6. Add human approval gates for sensitive, destructive, expensive, or externally visible actions.
7. Define logging, audit, monitoring, kill-switch, and rollback requirements for agents.
8. Produce an agent control design that balances security, usability, and developer velocity.

## Topics

- Agent architecture
- Tool calling and function calling
- Tool schemas and argument validation
- Tool identity and scoped credentials
- Per-action authorization
- Least privilege for agents
- Direct and indirect prompt injection against agents
- Goal hijacking
- Tool misuse
- Identity and privilege abuse
- Memory and context poisoning
- Insecure inter-agent communication
- Excessive agency
- Human-agent trust exploitation
- Cascading failures
- Sandboxing and egress control
- Approval gates and break-glass flows
- Audit logs and accountability
- Kill switches and rollback

## Security engineering connection

Agent security reuses classic security principles:

| Principle | Agent security interpretation |
|---|---|
| Least privilege | Agents should only receive the tools, data, and scopes needed for the current task. |
| Complete mediation | Every tool action should be authorized at execution time, not only when the conversation starts. |
| Fail-safe defaults | When policy is unclear, the agent should not perform the action. |
| Separation of duties | The model may propose an action, but policy enforcement should happen outside the model. |
| Defense in depth | Prompt rules, tool validation, policy, approvals, monitoring, and rollback all matter. |
| Auditability | Every meaningful agent decision and tool action should be attributable and reviewable. |
| Economy of mechanism | Prefer small, specific tools over broad tools such as `run_shell`, `query_anything`, or `send_any_email`. |

## Reference architecture

```text
user / attacker / business workflow
  |
  v
agent interface
  |
  +-- conversation state
  +-- instruction hierarchy
  +-- model gateway
  +-- planning / orchestration layer
  +-- policy decision point
  +-- tool broker
  |     +-- ticket tool
  |     +-- document search tool
  |     +-- email / chat tool
  |     +-- code or shell tool
  |     +-- browser tool
  |     +-- internal API tools
  +-- memory service
  +-- audit log
  +-- monitoring and alerting
  +-- approval workflow
```

## Core design rule

The model can recommend, classify, summarize, plan, or request an action.

The application must decide:

- whether the user is allowed to request the action;
- whether the agent identity is allowed to perform the action;
- whether the target object is in scope;
- whether the arguments are valid;
- whether approval is required;
- whether rate, cost, or safety limits apply;
- whether the action must be logged or monitored.

## Lab

Students review and exploit a vulnerable internal operations agent that can:

- read fake incidents;
- search fake internal documents;
- update fake tickets;
- store memory;
- call a simulated notification tool;
- call a simulated shell-like diagnostic tool.

The goal is not to attack real systems. The lab uses local fake data and simulated tools.

## Deliverable

Students produce an **agent control design** containing:

1. Agent architecture diagram
2. Tool inventory
3. Tool permission matrix
4. Sensitive-action approval policy
5. Memory trust policy
6. Logging and monitoring requirements
7. Kill-switch and rollback plan
8. Residual risk statement

## Files in this module

- `slides.md` — Markdown slide deck
- `instructor-notes.md` — delivery guidance and facilitation notes
- `student-handout.md` — student-facing reference
- `exercise-agent-control-design.md` — main exercise
- `checklist.md` — agent security checklist
- `quiz.md` — quiz and answer key
- `references.md` — module-specific references

## Related labs and templates

- `../../labs/agent-labs/agent-tool-misuse-lab.md`
- `../../labs/agent-labs/memory-poisoning-approval-gates-lab.md`
- `../../templates/agent-control-design-template.md`
- `../../templates/tool-permission-matrix-template.md`
- `../../templates/agent-action-approval-policy-template.md`
