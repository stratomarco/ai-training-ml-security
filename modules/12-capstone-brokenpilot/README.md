# Module 12 — Capstone: BrokenPilot

## Status

Design package complete. Full teaching package can be expanded later after Modules 8–11 are built.

The current capstone design lives in [`../../labs/brokenpilot/`](../../labs/brokenpilot/).

## Purpose

Bring the entire course together in a realistic internal AI agent scenario.

BrokenPilot is an internal AI assistant used by engineering and operations teams. It can search documents, summarize incidents, read and update tickets, query fake service configuration, use tools, retrieve context through RAG, and store memory.

Students must threat model, attack, defend, and communicate risk for the system.

## Key message

The capstone is not about finding one clever prompt.

The capstone is about connecting architecture, exploitation, mitigation, governance, and residual risk.

## Learning objectives

By the end of this capstone, students should be able to:

1. Explain the architecture of an AI-enabled internal operations assistant.
2. Identify assets, trust boundaries, and attacker personas.
3. Build a threat model for an LLM/RAG/agent system.
4. Demonstrate representative vulnerabilities safely in a fake lab environment.
5. Connect vulnerabilities to classic security engineering principles.
6. Propose mitigations that balance security, usability, and developer velocity.
7. Design a secure reference architecture.
8. Produce a red-team report and risk register.
9. Explain residual risk to leadership.

## Capstone materials

| File | Purpose |
|---|---|
| [`../../labs/brokenpilot/scenario.md`](../../labs/brokenpilot/scenario.md) | Business context and student mission. |
| [`../../labs/brokenpilot/architecture.md`](../../labs/brokenpilot/architecture.md) | System architecture and trust boundaries. |
| [`../../labs/brokenpilot/roles.md`](../../labs/brokenpilot/roles.md) | User roles and attacker personas. |
| [`../../labs/brokenpilot/data-model.md`](../../labs/brokenpilot/data-model.md) | Fake data model. |
| [`../../labs/brokenpilot/tools.md`](../../labs/brokenpilot/tools.md) | Tool inventory and permission model. |
| [`../../labs/brokenpilot/vulnerabilities.md`](../../labs/brokenpilot/vulnerabilities.md) | Intentional vulnerability list. |
| [`../../labs/brokenpilot/attack-paths.md`](../../labs/brokenpilot/attack-paths.md) | Suggested attack paths. |
| [`../../labs/brokenpilot/student-brief.md`](../../labs/brokenpilot/student-brief.md) | Student-facing assignment brief. |
| [`../../labs/brokenpilot/instructor-solution.md`](../../labs/brokenpilot/instructor-solution.md) | Instructor solution guide. |
| [`../../labs/brokenpilot/secure-reference-architecture.md`](../../labs/brokenpilot/secure-reference-architecture.md) | Target-state secure design. |
| [`../../labs/brokenpilot/grading-rubric.md`](../../labs/brokenpilot/grading-rubric.md) | BrokenPilot-specific rubric. |

## Suggested delivery flow

| Phase | Activity | Time |
|---|---|---:|
| 1 | Introduce business context and architecture | 20 min |
| 2 | Student threat modeling | 45–60 min |
| 3 | Attack-path exploration | 60–90 min |
| 4 | Mitigation design | 45–60 min |
| 5 | Team presentations | 30–60 min |
| 6 | Instructor debrief | 30 min |

For a shorter workshop, use only one or two attack paths and focus heavily on mitigation design.

## Required student deliverables

1. Executive summary.
2. Architecture and trust-boundary summary.
3. Threat model.
4. Abuse cases.
5. Findings with evidence.
6. Risk register.
7. Mitigation plan.
8. Secure reference architecture.
9. Residual-risk statement.
10. Leadership talking points.

## Instructor notes

Students may over-focus on prompt payloads. Redirect them toward:

- What the model can see.
- What the model can do.
- Which trust boundary failed.
- Which policy was missing.
- Which action should have required approval.
- Which data should never have reached the model.
- Which logs would be needed during an incident.

## Defensive design patterns

- Keep security decisions outside the model.
- Treat model input and output as untrusted.
- Apply least privilege to data, tools, and workflows.
- Validate tool arguments and enforce authorization per action.
- Add human approval for destructive or high-impact actions.
- Preserve document metadata during chunking.
- Enforce retrieval authorization.
- Scope, review, and expire memory.
- Log security-relevant events.
- Rate-limit expensive or sensitive operations.
- Build monitoring for abuse, drift, and unexpected behavior.

## Suggested reading

See [`../../references.md`](../../references.md).
