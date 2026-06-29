# Exercise — BrokenPilot Red Team Review and Mitigation Design

## Goal

Create a red team review and mitigation plan for BrokenPilot.

This exercise builds on the threat model. You will choose attack paths, document representative findings, and design controls that reduce risk while preserving useful automation.

## Input materials

Use:

- [`../../labs/brokenpilot/attack-paths.md`](../../labs/brokenpilot/attack-paths.md)
- [`../../labs/brokenpilot/vulnerabilities.md`](../../labs/brokenpilot/vulnerabilities.md)
- [`../../labs/brokenpilot/secure-reference-architecture.md`](../../labs/brokenpilot/secure-reference-architecture.md)
- [`../../templates/brokenpilot-final-report-template.md`](../../templates/brokenpilot-final-report-template.md)
- [`../../templates/brokenpilot-evidence-log-template.md`](../../templates/brokenpilot-evidence-log-template.md)
- [`../../templates/brokenpilot-risk-register-template.md`](../../templates/brokenpilot-risk-register-template.md)
- [`../../templates/brokenpilot-remediation-backlog-template.md`](../../templates/brokenpilot-remediation-backlog-template.md)

## Part 1 — Select attack paths

Choose at least three attack paths.

Recommended options:

| Attack path | Primary concept |
|---|---|
| Indirect prompt injection through runbook content | RAG and context trust. |
| Cross-team document leakage | Retrieval authorization. |
| Unauthorized ticket update | Tool authorization and excessive agency. |
| Memory poisoning | Persistent untrusted state. |
| Insecure output handling | Treating model output as trusted UI content. |
| Sensitive trace leakage | Logging and privacy. |
| Overreliance on generated incident advice | Human factors and operational risk. |

## Part 2 — Define test objectives

For each attack path, define:

- objective;
- attacker persona;
- preconditions;
- target asset;
- expected control;
- expected evidence;
- safety boundary.

Example:

```text
Objective: Determine whether a low-privilege user can receive restricted incident notes through RAG.
Persona: Low-privilege employee.
Target asset: Restricted incident notes.
Expected control: Retrieval authorization before context assembly.
Safety boundary: Use only fake BrokenPilot data.
```

## Part 3 — Document representative evidence

For each finding, capture:

- input or scenario;
- role used;
- retrieved document IDs or fake evidence;
- model output summary;
- tool call, if any;
- violated policy;
- impact;
- root cause.

Do not rely only on screenshots. Explain the control failure.

## Part 4 — Score findings

Use a simple risk model:

| Factor | Questions |
|---|---|
| Impact | What business harm could occur? |
| Exploitability | How easy is the attack path? |
| Exposure | Who can reach the attack surface? |
| Privilege | What access is required? |
| Blast radius | One user, one team, or many teams? |
| Detectability | Would current logs show it? |
| Control gap | Is the missing control fundamental? |

Severity options:

- Critical
- High
- Medium
- Low
- Informational

## Part 5 — Design mitigations

For each finding, propose controls.

Good mitigations should specify where the control lives:

| Control type | Example location |
|---|---|
| Authorization | RAG retriever, tool gateway, backend API. |
| Validation | Tool schema, API boundary, output renderer. |
| Approval | Workflow service, ticket update path. |
| Isolation | Memory store, tenant partition, vector namespace. |
| Monitoring | Audit log pipeline, SIEM, anomaly detection. |
| Governance | Policy, ownership, release gate, risk acceptance. |

Avoid recommending only “improve the prompt.”

## Part 6 — Build the remediation roadmap

Group work into:

| Priority | Meaning |
|---|---|
| P0 | Must fix before broader deployment. |
| P1 | Fix soon; high-risk but compensating controls may exist. |
| P2 | Planned hardening. |
| P3 | Nice-to-have or future improvement. |

Include:

- owner;
- implementation notes;
- dependencies;
- validation test;
- residual risk.

## Part 7 — Prepare the readout

Prepare a short leadership readout:

1. What we reviewed.
2. What matters most.
3. Top three risks.
4. What must change before deployment.
5. What can ship with compensating controls.
6. What should not be automated yet.
7. Residual risk.

## Deliverable

Submit:

1. Attack plan.
2. Evidence log.
3. Findings.
4. Risk register.
5. Mitigation plan.
6. Remediation backlog.
7. Executive readout.

## Instructor evaluation

A strong submission is actionable.

It should help an engineering team decide what to implement next and help leadership understand what risk remains.
