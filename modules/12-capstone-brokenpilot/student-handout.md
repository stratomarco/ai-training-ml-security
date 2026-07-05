# Module 12 Student Handout  -  BrokenPilot Capstone

## Your mission

You are part of a security review team asked to assess BrokenPilot before wider internal deployment.

BrokenPilot is an internal AI assistant used by engineering and operations teams. It can summarize incidents, search documentation, read and update tickets, retrieve service configuration, use tools, and store memory.

Your task is to evaluate whether the system is safe enough to expand, what must change before deployment, and what residual risks remain.

## What you are expected to do

You must produce a practical security review, not just a list of prompt tricks.

Your team should:

1. Understand the system architecture.
2. Identify important assets and trust boundaries.
3. Define realistic attacker personas.
4. Create abuse cases.
5. Identify likely vulnerabilities.
6. Demonstrate or describe representative attack paths safely.
7. Document evidence using fake data only.
8. Explain root causes.
9. Recommend mitigations.
10. Present residual risk.

## Scope

In scope:

- BrokenPilot web/API layer;
- LLM gateway;
- prompts and context assembly;
- RAG retriever;
- vector database;
- internal document store;
- ticket system tools;
- service configuration tools;
- memory store;
- approval workflows;
- logging and monitoring;
- role and permission model;
- secure architecture.

Out of scope:

- real systems;
- real secrets;
- real production data;
- destructive actions;
- attacks against external services;
- attempts to bypass systems you do not own.

## Safety rules

Use only the fake BrokenPilot scenario and fake data.

Do not include real credentials, real customer data, real internal company data, or real system names in your report.

Your evidence should be reproducible, minimal, and safe.

## Core questions

Use these questions throughout the capstone:

1. What can the model see?
2. What can the model do?
3. Who authorized the action?
4. What data was retrieved?
5. Was retrieval authorization enforced?
6. Was the output treated as untrusted?
7. Was a tool call validated?
8. Was approval required?
9. Was memory scoped and reviewable?
10. Would logs allow incident reconstruction?

## Required deliverables

Your final report should include:

| Deliverable | What to include |
|---|---|
| Executive summary | Top risks and recommended decision. |
| System overview | Short architecture and trust-boundary summary. |
| Threat model | Assets, actors, entry points, trust boundaries, abuse cases. |
| Findings | Security issues with evidence and impact. |
| Risk register | Prioritized risk list with owners and status. |
| Mitigation plan | Controls, trade-offs, and implementation priority. |
| Secure reference architecture | Target-state design. |
| Residual risk | What remains after mitigation. |
| Leadership talking points | Plain-language summary for decision makers. |

## Suggested finding format

Use this structure for each finding:

```text
Title:
Severity:
Affected component:
Attack path:
Evidence:
Business impact:
Root cause:
Recommended mitigation:
Detection opportunity:
Residual risk:
```

## Example weak finding

> We jailbroke the model.

This is weak because it does not explain impact, root cause, or control failure.

## Example strong finding

> A low-privilege user can cause BrokenPilot to summarize restricted incident notes because the RAG retriever assembles context before enforcing document-level authorization. The failed control is retrieval authorization, not only prompt filtering.

This is stronger because it identifies the asset, actor, control failure, and impact.

## Suggested team roles

| Role | Responsibility |
|---|---|
| Architecture lead | Tracks components, trust boundaries, and data flows. |
| Red team lead | Builds attack paths and evidence plan. |
| Defense lead | Designs mitigations and target-state controls. |
| Reporter | Keeps the final report clear and structured. |
| Presenter | Prepares the leadership readout. |

For small teams, combine roles.

## Time management

Do not spend all your time on one prompt.

Suggested split:

- 25% architecture and threat model;
- 25% attack paths and evidence;
- 30% mitigation and secure design;
- 20% report and presentation.

## Success criteria

You are successful if your final answer helps engineering leadership decide:

- what can safely ship now;
- what must be fixed first;
- what needs monitoring;
- what requires human approval;
- what risk remains;
- what should not be automated yet.
