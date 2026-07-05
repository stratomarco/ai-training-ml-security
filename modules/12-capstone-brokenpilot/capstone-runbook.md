# BrokenPilot Capstone Runbook

## Purpose

This runbook helps instructors deliver the BrokenPilot capstone as a structured final exercise.

The capstone can be run as a tabletop, workshop, or full-day exercise.

## Before the session

### Instructor preparation

- [ ] Review the BrokenPilot scenario.
- [ ] Review the architecture and trust boundaries.
- [ ] Review intentional vulnerabilities.
- [ ] Select the delivery format.
- [ ] Decide whether students will work individually or in teams.
- [ ] Prepare student handouts.
- [ ] Prepare templates.
- [ ] Decide which materials are instructor-only.
- [ ] Define scoring expectations.

### Student preparation

Ask students to review:

- Module 5  -  LLM Application Security.
- Module 6  -  RAG Security.
- Module 7  -  Agent and Tool Security.
- Module 11  -  AI Red Team Methodology.
- BrokenPilot scenario and architecture.

## Suggested folder map

Student-facing:

```text
modules/12-capstone-brokenpilot/student-handout.md
modules/12-capstone-brokenpilot/exercise-capstone-threat-model.md
modules/12-capstone-brokenpilot/exercise-capstone-red-team-review.md
labs/brokenpilot/scenario.md
labs/brokenpilot/architecture.md
labs/brokenpilot/roles.md
labs/brokenpilot/tools.md
course-templates/brokenpilot-final-report-template.md
course-templates/brokenpilot-risk-register-template.md
course-templates/brokenpilot-evidence-log-template.md
course-templates/brokenpilot-remediation-backlog-template.md
```

Instructor-only:

```text
labs/brokenpilot/vulnerabilities.md
labs/brokenpilot/attack-paths.md
labs/brokenpilot/instructor-solution.md
labs/brokenpilot/grading-rubric.md
assessments/brokenpilot-capstone-final-rubric.md
```

## Full-day delivery flow

### 1. Opening and mission  -  15 minutes

Explain:

- BrokenPilot business purpose;
- why the system matters;
- safety rules;
- expected deliverables;
- assessment criteria.

Key message:

> You are not here to collect prompt tricks. You are here to produce a security decision.

### 2. Architecture walkthrough  -  30 minutes

Walk through:

- web/API layer;
- LLM gateway;
- RAG retriever;
- vector database;
- document store;
- ticket system;
- service configuration tool;
- memory store;
- audit logs;
- approval workflows.

Ask students:

- What can the model see?
- What can the model do?
- Where are trust boundaries?
- Where should authorization happen?

### 3. Threat model  -  60 minutes

Students complete the threat model exercise.

Expected output:

- assets;
- actors;
- entry points;
- trust boundaries;
- abuse cases;
- top risks.

Instructor should circulate and challenge shallow answers.

### 4. Attack path planning  -  45 minutes

Students choose at least three attack paths.

They should define:

- objective;
- persona;
- preconditions;
- target asset;
- expected evidence;
- safety boundary.

### 5. Red team review/tabletop  -  75 minutes

Students document findings using the evidence log.

They should focus on representative evidence, not exhaustive exploitation.

Expected finding areas:

- RAG authorization;
- indirect prompt injection;
- tool misuse;
- excessive agency;
- memory poisoning;
- sensitive disclosure;
- audit gaps.

### 6. Mitigation design  -  60 minutes

Students design controls.

Require them to specify where each control lives:

- application layer;
- retriever;
- tool gateway;
- backend API;
- policy engine;
- approval workflow;
- logging pipeline;
- monitoring system;
- governance process.

### 7. Report and readout preparation  -  45 minutes

Students prepare:

- top risks;
- final report;
- remediation roadmap;
- residual risk;
- leadership readout.

### 8. Presentations  -  45 minutes

Each team gets 5–8 minutes.

Suggested structure:

1. System reviewed.
2. Top three risks.
3. Evidence summary.
4. Recommended controls.
5. Remediation priority.
6. Residual risk.

### 9. Instructor debrief  -  30 minutes

Compare student results to the instructor solution.

Reinforce:

- security decisions outside the model;
- retrieval authorization;
- tool approval;
- memory scope;
- observability;
- residual-risk honesty.

## Short tabletop variant

For a 2–3 hour version:

1. Use only the architecture review.
2. Select two attack paths.
3. Skip detailed evidence collection.
4. Focus on mitigation and residual risk.

Recommended attack paths:

- indirect prompt injection through retrieved document;
- unauthorized ticket update through tool misuse.

## Scoring

Use:

- [`../../assessments/brokenpilot-capstone-final-rubric.md`](../../assessments/brokenpilot-capstone-final-rubric.md)
- [`../../labs/brokenpilot/grading-rubric.md`](../../labs/brokenpilot/grading-rubric.md)

## Instructor close

End with:

> BrokenPilot is a fake system, but the failure patterns are real. AI security is not only model behavior. It is data, identity, authorization, tools, memory, logs, workflow, and security engineering judgment.
