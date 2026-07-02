# Exercise  -  BrokenPilot Threat Model

## Goal

Create a threat model for BrokenPilot that identifies assets, trust boundaries, attackers, abuse cases, and security requirements.

## Input materials

Use:

- [`../../labs/brokenpilot/scenario.md`](../../labs/brokenpilot/scenario.md)
- [`../../labs/brokenpilot/architecture.md`](../../labs/brokenpilot/architecture.md)
- [`../../labs/brokenpilot/roles.md`](../../labs/brokenpilot/roles.md)
- [`../../labs/brokenpilot/tools.md`](../../labs/brokenpilot/tools.md)
- [`../../labs/brokenpilot/data-model.md`](../../labs/brokenpilot/data-model.md)
- [`../../course-templates/threat-model-template.md`](../../course-templates/threat-model-template.md)

## Part 1  -  System summary

Write a short summary of what BrokenPilot does.

Include:

- users;
- business purpose;
- major components;
- sensitive data;
- actions the system can perform.

## Part 2  -  Asset inventory

Identify at least ten assets.

Examples:

| Asset | Why it matters | Confidentiality | Integrity | Availability |
|---|---|---|---|---|
| Incident notes | May contain sensitive operational details. | High | High | Medium |
| Ticket status | Drives workflow decisions. | Medium | High | High |
| Tool tokens | Enable backend actions. | High | High | Medium |

## Part 3  -  Trust boundaries

Draw or describe the trust boundaries.

At minimum include boundaries between:

- user and BrokenPilot API;
- BrokenPilot API and LLM gateway;
- application and RAG retriever;
- retriever and vector database;
- model and tools;
- tool gateway and backend systems;
- memory store and current session;
- logs and security review.

## Part 4  -  Entry points

Identify ways an attacker or untrusted data can enter the system.

Examples:

- user prompt;
- uploaded document;
- indexed runbook;
- ticket comment;
- service metadata;
- memory entry;
- tool output;
- model output rendered in UI.

## Part 5  -  Attacker personas

Define at least four personas.

| Persona | Access | Goal | Example abuse |
|---|---|---|---|
| Low-privilege employee | Normal internal user | Read restricted incident context | Ask broad questions that retrieve forbidden documents. |
| Malicious document author | Can edit a runbook | Influence future answers | Insert hidden instructions into indexed content. |
| Compromised account | Legitimate user account | Cause workflow change | Trigger unauthorized ticket update. |

## Part 6  -  Abuse cases

Write at least six abuse cases.

Use this format:

```text
As a [persona], I want to [abuse action], so that [impact].
```

Examples:

- As a malicious document author, I want retrieved content to override the assistant's instructions, so that the assistant leaks restricted context.
- As a low-privilege employee, I want BrokenPilot to summarize tickets from another team, so that I can learn sensitive operational details.
- As a compromised user, I want the agent to update ticket severity without approval, so that incident triage is manipulated.

## Part 7  -  Security requirements

Write security requirements that would reduce the abuse cases.

Examples:

| Requirement | Control location | Abuse case reduced |
|---|---|---|
| Retrieval must enforce document-level authorization before context assembly. | RAG retriever | Cross-team data leakage. |
| Tool execution must enforce per-user, per-action authorization. | Tool gateway | Unauthorized ticket update. |
| High-impact actions must require human approval. | Workflow service | Excessive agency. |

## Part 8  -  Prioritization

Select the top five risks.

Prioritize based on:

- business impact;
- likelihood;
- exposure;
- privilege required;
- blast radius;
- ease of mitigation;
- confidence in evidence.

## Deliverable

Submit:

1. System summary.
2. Asset inventory.
3. Trust-boundary diagram or description.
4. Entry-point list.
5. Attacker personas.
6. Abuse cases.
7. Security requirements.
8. Top five prioritized risks.

## Instructor evaluation

A strong submission should identify both AI-specific and classic security risks.

The best submissions do not say only “prompt injection.” They explain the trust boundary and control failure that makes the attack matter.
