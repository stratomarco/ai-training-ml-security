# Module 12  -  Capstone: BrokenPilot

## Purpose

Bring the entire course together in a realistic internal AI agent scenario.

BrokenPilot is an internal AI assistant used by engineering and operations teams. It can search documents, summarize incidents, read and update tickets, query fake service configuration, use tools, retrieve context through RAG, and store memory.

Students must threat model, attack, defend, and communicate risk for the system.

## Key message

The capstone is not about finding one clever prompt.

The capstone is about connecting architecture, exploitation, mitigation, governance, and residual risk.

A strong capstone submission shows that students can reason across:

- classic security engineering;
- ML lifecycle risk;
- LLM application security;
- RAG security;
- agent and tool security;
- MLOps and supply chain;
- privacy and data protection;
- adversarial robustness;
- red team methodology;
- secure architecture;
- leadership communication.

## Learning objectives

By the end of this capstone, students should be able to:

1. Explain the architecture of an AI-enabled internal operations assistant.
2. Identify assets, trust boundaries, user roles, and attacker personas.
3. Build a threat model for an LLM/RAG/agent system.
4. Demonstrate representative vulnerabilities safely in a fake lab environment.
5. Connect vulnerabilities to classic security engineering principles.
6. Map findings to OWASP, BIML-style architectural risks, NIST AI RMF-style risk thinking, and MITRE ATLAS-style tactics where useful.
7. Propose mitigations that balance security, usability, and developer velocity.
8. Design a secure reference architecture.
9. Produce a red-team report, risk register, and remediation roadmap.
10. Explain residual risk to leadership.

## Capstone storyline

BrokenPilot was built quickly to improve engineering productivity.

It can:

- answer questions about incidents;
- summarize tickets;
- search internal runbooks;
- retrieve service configuration;
- create and update tickets;
- remember user preferences;
- call internal tools through an API;
- generate operational recommendations.

The business likes it because it reduces repetitive work. Security is concerned because the assistant can see sensitive operational data and can perform actions that affect incident response workflows.

Students are asked to review the system before wider deployment.

## Module files

| File | Purpose |
|---|---|
| [`slides.md`](slides.md) | Markdown slide deck for the capstone session. |
| [`instructor-notes.md`](instructor-notes.md) | Facilitator guidance, timing, expected findings, and debrief notes. |
| [`student-handout.md`](student-handout.md) | Student-facing capstone brief and deliverable expectations. |
| [`exercise-capstone-threat-model.md`](exercise-capstone-threat-model.md) | Structured threat-modeling exercise. |
| [`exercise-capstone-red-team-review.md`](exercise-capstone-red-team-review.md) | Structured red team and mitigation-design exercise. |
| [`checklist.md`](checklist.md) | Capstone review checklist. |
| [`quiz.md`](quiz.md) | Capstone knowledge check and answer key. |
| [`capstone-runbook.md`](capstone-runbook.md) | End-to-end delivery runbook. |
| [`references.md`](references.md) | Module reference anchors and internal links. |

## Supporting BrokenPilot files

The detailed capstone design lives in [`../../labs/brokenpilot/`](../../labs/brokenpilot/README.md).

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
| [`../../labs/brokenpilot/final-presentation-guide.md`](../../labs/brokenpilot/final-presentation-guide.md) | Presentation structure for student teams. |
| [`../../labs/brokenpilot/evidence-log-guide.md`](../../labs/brokenpilot/evidence-log-guide.md) | Evidence handling and documentation guidance. |
| [`../../labs/brokenpilot/remediation-backlog-guide.md`](../../labs/brokenpilot/remediation-backlog-guide.md) | How to turn findings into an engineering backlog. |

## Suggested delivery formats

| Format | Duration | Best for |
|---|---:|---|
| Short tabletop | 2–3 hours | Leadership, architecture review, security champions. |
| Half-day workshop | 4 hours | AppSec, architects, platform, ML engineers. |
| Full-day capstone | 6–7 hours | Practitioner training with team presentations. |
| Two-day capstone | 10–12 hours | Full threat model, red team, defense design, and executive readout. |

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

## Assessment model

Students are assessed on security judgment, not only exploit success.

A strong final submission:

- explains the business impact;
- identifies the failed trust boundary;
- shows safe, fake-data evidence;
- proposes controls outside the model;
- accounts for developer velocity;
- prioritizes remediation;
- explains residual risk honestly.

## Defensive design themes

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

## Instructor note

Students may over-focus on prompt payloads. Redirect them toward the system:

- What can the model see?
- What can the model do?
- Which trust boundary failed?
- Which policy was missing?
- Which action should have required approval?
- Which data should never have reached the model?
- Which logs would be needed during an incident?

## Suggested reading

See [`references.md`](references.md) and the root [`../../references.md`](../../references.md).

## Assessment scope note

The runnable BrokenPilot MVP directly demonstrates Module 05, Module 06, Module 07, and Module 11 style findings. Module 08, Module 09, and Module 10 risks are assessed through tabletop analysis, architecture review, written deliverables, and discussion unless a future prototype increment implements those behaviors. See `labs/brokenpilot/capstone-assessment-scope.md`.
