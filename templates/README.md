# Templates

This folder contains reusable Markdown templates for students and instructors.

## Core templates

| Template | Purpose |
|---|---|
| [`threat-model-template.md`](threat-model-template.md) | System threat model. |
| [`abuse-case-template.md`](abuse-case-template.md) | Abuse-case capture. |
| [`lab-guide-template.md`](lab-guide-template.md) | Standard lab guide structure. |
| [`red-team-report-template.md`](red-team-report-template.md) | AI red-team report. |
| [`risk-register-template.md`](risk-register-template.md) | Risk tracking. |
| [`architecture-review-template.md`](architecture-review-template.md) | General architecture review. |
| [`architecture-risk-review-template.md`](architecture-risk-review-template.md) | BIML-style architecture risk review. |
| [`residual-risk-template.md`](residual-risk-template.md) | Residual-risk statement. |
| [`module-template.md`](../modules/module-template.md) | Standard module structure. |

## AI/ML-specific templates

| Template | Purpose |
|---|---|
| [`ml-system-architecture-review-template.md`](ml-system-architecture-review-template.md) | ML lifecycle architecture review. |
| [`ml-attack-summary-template.md`](ml-attack-summary-template.md) | Classical ML attack summary. |
| [`llm-application-security-review-template.md`](llm-application-security-review-template.md) | LLM application review. |
| [`rag-threat-model-template.md`](rag-threat-model-template.md) | RAG threat model. |
| [`vector-database-authorization-checklist.md`](vector-database-authorization-checklist.md) | Vector DB authorization checklist. |
| [`agent-control-design-template.md`](agent-control-design-template.md) | Agent control design. |
| [`tool-permission-matrix-template.md`](tool-permission-matrix-template.md) | Tool permission matrix. |
| [`agent-action-approval-policy-template.md`](agent-action-approval-policy-template.md) | Risk-tiered approval policy. |
| [`brokenpilot-final-report-template.md`](brokenpilot-final-report-template.md) | BrokenPilot final security review report. |
| [`secure-mlops-review-template.md`](secure-mlops-review-template.md) | Secure MLOps and supply chain review. |
| [`dataset-provenance-review-template.md`](dataset-provenance-review-template.md) | Dataset source, lineage, sensitivity, and integrity review. |
| [`model-artifact-risk-review-template.md`](model-artifact-risk-review-template.md) | Model artifact trust, loading, integrity, and promotion review. |
| [`model-registry-access-control-template.md`](model-registry-access-control-template.md) | Model registry RBAC and promotion controls. |
| [`ml-bom-template.md`](ml-bom-template.md) | ML bill of materials for code, data, model, prompt, RAG, evaluation, and deployment artifacts. |
| [`privacy-risk-assessment-template.md`](privacy-risk-assessment-template.md) | AI privacy risk assessment. |
| [`ai-data-retention-log-review-template.md`](ai-data-retention-log-review-template.md) | Prompt, completion, retrieval, trace, memory, and feedback retention review. |
| [`ai-privacy-control-checklist.md`](ai-privacy-control-checklist.md) | Compact AI privacy control checklist. |
| [`adversarial-test-plan-template.md`](adversarial-test-plan-template.md) | Adversarial test plan for model-backed systems. |
| [`robustness-evaluation-template.md`](robustness-evaluation-template.md) | Robustness evaluation and threshold review template. |
| [`drift-abuse-monitoring-template.md`](drift-abuse-monitoring-template.md) | Drift, abuse monitoring, and response playbook template. |
| [`ai-red-team-scope-template.md`](ai-red-team-scope-template.md) | AI red team scope and rules-of-engagement template. |
| [`ai-red-team-attack-plan-template.md`](ai-red-team-attack-plan-template.md) | AI red team attack planning template. |
| [`ai-red-team-report-template.md`](ai-red-team-report-template.md) | Full AI red team report template. |
| [`ai-red-team-executive-readout-template.md`](ai-red-team-executive-readout-template.md) | Leadership-facing red team readout template. |


## v0.14 BrokenPilot templates

Added:

- `brokenpilot-risk-register-template.md`
- `brokenpilot-evidence-log-template.md`
- `brokenpilot-remediation-backlog-template.md`


## DVAIA validation templates

- `dvaia-evidence-log-template.md` — evidence log for validated DVAIA-backed labs.

## Reading-first content templates

Use these templates when deepening modules beyond slides and lab steps:

- `deep-dive-template.md` — explains a topic with architecture, principles, impact, controls, and framework mapping.
- `attack-anatomy-template.md` — breaks an attack into preconditions, root cause, attack path, evidence, impact, controls, and residual risk.
- `controls-and-remediations-template.md` — turns a finding into implementable engineering controls and test cases.

## Executive risk memo

Use `executive-risk-memo-template.md` when students need to communicate AI security risk as a leadership decision rather than a technical finding list.

## Finding write-up template

Use [`finding-rewrite-template.md`](finding-rewrite-template.md) when students need to rewrite a weak observation into an actionable security finding.
