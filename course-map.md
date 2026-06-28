# Course Map

This file maps modules to frameworks, labs, deliverables, and core security principles.

## Module-to-framework map

| Module | OWASP ML Top 10 | OWASP LLM / GenAI | OWASP Agentic | BIML | NIST AI RMF / GenAI | MITRE ATLAS |
|---|---|---|---|---|---|---|
| 01 Security Engineering for AI | Partial | Partial | Partial | Strong | Strong | Partial |
| 02 ML System Architecture | Strong | Partial | Partial | Strong | Strong | Strong |
| 03 OWASP ML Top 10 | Strong | Partial | Partial | Strong | Partial | Strong |
| 04 BIML Risk Analysis | Strong | Strong | Strong | Strong | Strong | Partial |
| 05 LLM Application Security | Partial | Strong | Partial | Strong | Strong | Strong |
| 06 RAG Security | Partial | Strong | Strong | Strong | Strong | Strong |
| 07 Agent and Tool Security | Partial | Strong | Strong | Strong | Strong | Strong |
| 08 Secure MLOps | Strong | Strong | Partial | Strong | Strong | Strong |
| 09 Privacy Attacks | Strong | Strong | Partial | Strong | Strong | Strong |
| 10 Adversarial ML | Strong | Partial | Partial | Strong | Partial | Strong |
| 11 AI Red Team Methodology | Strong | Strong | Strong | Strong | Strong | Strong |
| 12 Capstone BrokenPilot | Strong | Strong | Strong | Strong | Strong | Strong |

## Module-to-lab map

| Module | Lab source | Lab type |
|---|---|---|
| 01 | Custom | Threat modeling tabletop |
| 02 | Custom | Architecture mapping |
| 03 | Custom toy ML app | Evasion, poisoning, extraction basics |
| 04 | Custom | Architecture risk review |
| 05 | DVAIA | Prompt injection and insecure output handling |
| 06 | DVAIA + custom RAG | Indirect prompt injection and retrieval auth |
| 07 | Vulnerable agent lab + BrokenPilot design | Tool misuse and excessive agency |
| 08 | Custom broken ML pipeline | Supply chain and MLOps review |
| 09 | Custom HR/customer-support RAG | Privacy leakage and cross-tenant retrieval |
| 10 | Custom classifier | Adversarial robustness |
| 11 | DVAIA + custom | Full AI red-team workflow |
| 12 | BrokenPilot | Capstone |

## Module-to-deliverable map

| Module | Deliverable |
|---|---|
| 01 | AI system context diagram and initial threat model |
| 02 | ML lifecycle data-flow diagram |
| 03 | ML attack summary and mitigation proposal |
| 04 | Architecture risk review |
| 05 | LLM vulnerability write-up |
| 06 | RAG threat model and mitigation design |
| 07 | Agent control design |
| 08 | Secure MLOps checklist and risk register |
| 09 | Privacy risk assessment |
| 10 | Adversarial test plan |
| 11 | AI red-team report |
| 12 | Capstone security review |

## Core security principles reused throughout the course

- Least privilege
- Complete mediation
- Fail-safe defaults
- Secure-by-default design
- Defense in depth
- Separation of duties
- Economy of mechanism
- Least astonishment
- Secure failure
- Explicit trust boundaries
- Input validation
- Output encoding
- Authentication and authorization
- Auditability
- Cryptographic key management
- Supply chain integrity
- Privacy by design
- Resilience and recoverability

## Repeated teaching pattern

For each topic, the instructor should connect four things:

1. Classic security principle
2. AI-specific failure mode
3. Practical exploit or abuse case
4. Engineering mitigation

Example:

```text
Classic principle: Least privilege
AI-specific failure: Agent has access to broad tools and data
Exploit: Prompt injection causes the agent to update a ticket or leak data
Mitigation: Per-action authorization, scoped tool tokens, approval gates, audit logs
```


## v0.3 update

- Module 02 — ML System Architecture is now expanded with slides, instructor notes, student handout, lifecycle DFD exercise, checklist, quiz, and references.
- Added `templates/ml-system-architecture-review-template.md`.


## v0.4 update

- Module 03 — OWASP ML Security Top 10 is now expanded with slides, instructor notes, student handout, attack review exercise, checklist, quiz, and references.
- Added `labs/toy-ml-attacks/classical-ml-attack-lab.md`.
- Added `templates/ml-attack-summary-template.md`.


## v0.5 update

- Module 04 — BIML Architectural Risk Analysis is now expanded with slides, instructor notes, student handout, architecture review exercise, checklist, quiz, and references.
- Added `templates/architecture-risk-review-template.md`.
- Added `labs/architecture-risk-review-labs/docops-assistant-architecture-review.md`.


## Build status update — v0.6

| Module | Status | Notes |
|---|---|---|
| 05 — LLM Application Security | Complete | Added README, slides, instructor notes, student handout, exercise, checklist, quiz, references, DVAIA lab guide, and review template. |


## Build status update — v0.7

| Module | Status | Notes |
|---|---|---|
| 06 — RAG Security and Indirect Prompt Injection | Complete | Added README, slides, instructor notes, student handout, RAG threat model exercise, checklist, quiz, references, RAG lab guide, RAG threat model template, and vector database authorization checklist. |

Updated lab mapping:

| Lab | Module | Purpose |
|---|---|---|
| `labs/rag-labs/rag-indirect-prompt-injection-lab.md` | 06 | Demonstrate indirect prompt injection, retrieval authorization failure, cross-tenant leakage, and mitigation design. |
| `templates/rag-threat-model-template.md` | 06 | Standard deliverable format for RAG security reviews. |
| `templates/vector-database-authorization-checklist.md` | 06 | Focused checklist for vector DB and retrieval-layer authorization. |


## Build status update — v0.8

| Module | Status | Notes |
|---|---|---|
| 07 — Agent and Tool Security | Complete | Added README, slides, instructor notes, student handout, agent control design exercise, checklist, quiz, references, agent tool misuse lab, memory poisoning lab, and agent control templates. |

Updated lab mapping:

| Lab or template | Module | Purpose |
|---|---|---|
| `labs/agent-labs/agent-tool-misuse-lab.md` | 07 | Demonstrate excessive agency, tool misuse, weak authorization, dangerous tool design, and approval design. |
| `labs/agent-labs/memory-poisoning-approval-gates-lab.md` | 07 | Demonstrate memory poisoning, memory provenance, review, expiry, and approval gates. |
| `templates/agent-control-design-template.md` | 07 | Standard deliverable format for agent security reviews. |
| `templates/tool-permission-matrix-template.md` | 07 | Defines per-tool users, roles, targets, actions, approval, logging, and rollback. |
| `templates/agent-action-approval-policy-template.md` | 07 | Defines risk-tiered approval requirements for agent actions. |


## Build status update — v0.9

| Area | Status | Notes |
|---|---|---|
| BrokenPilot capstone paper design | Complete | Added scenario, architecture, roles, data model, tools, vulnerability list, attack paths, student brief, instructor solution guide, secure reference architecture, grading rubric, implementation notes, and module mapping. |

Updated capstone mapping:

| File | Purpose |
|---|---|
| `labs/brokenpilot/scenario.md` | Business context and student mission. |
| `labs/brokenpilot/architecture.md` | Components, data flows, and trust boundaries. |
| `labs/brokenpilot/roles.md` | Legitimate users, attacker personas, and permission assumptions. |
| `labs/brokenpilot/data-model.md` | Fake data entities and classification model. |
| `labs/brokenpilot/tools.md` | Tool inventory, risk tiers, and permission matrix. |
| `labs/brokenpilot/vulnerabilities.md` | Intentional vulnerabilities mapped to course modules. |
| `labs/brokenpilot/attack-paths.md` | Suggested attack chains for capstone delivery. |
| `labs/brokenpilot/student-brief.md` | Student-facing assignment. |
| `labs/brokenpilot/instructor-solution.md` | Instructor guide with expected findings. |
| `labs/brokenpilot/secure-reference-architecture.md` | Target-state secure design. |
| `labs/brokenpilot/grading-rubric.md` | BrokenPilot-specific rubric. |
| `templates/brokenpilot-final-report-template.md` | Final report template. |

Next recommended module: Module 9 — Privacy Attacks and Data Protection.


## Build status update — v0.10

| Module | Status | Notes |
|---|---|---|
| 08 — Secure MLOps and AI Supply Chain | Complete | Added README, slides, instructor notes, student handout, Secure MLOps review exercise, checklist, quiz, references, broken ML pipeline lab, model artifact provenance lab, and supply chain templates. |

Updated lab and template mapping:

| Lab or template | Module | Purpose |
|---|---|---|
| `labs/mlops-supply-chain-labs/broken-ml-pipeline-lab.md` | 08 | Review dataset, notebook, dependency, training, registry, deployment, and feedback-loop supply chain risks. |
| `labs/mlops-supply-chain-labs/model-artifact-provenance-lab.md` | 08 | Review model artifact trust, provenance, safe loading, registry metadata, and production promotion decisions. |
| `templates/secure-mlops-review-template.md` | 08 | Standard deliverable format for Secure MLOps reviews. |
| `templates/dataset-provenance-review-template.md` | 08 | Focused template for dataset source, lineage, sensitivity, and integrity review. |
| `templates/model-artifact-risk-review-template.md` | 08 | Focused template for model artifact trust, loading, provenance, and promotion evidence. |
| `templates/model-registry-access-control-template.md` | 08 | Registry RBAC and promotion approval design template. |
| `templates/ml-bom-template.md` | 08 | ML bill-of-materials template covering code, data, model, prompt, RAG, evaluation, and deployment artifacts. |

Next recommended module: Module 9 — Privacy Attacks and Data Protection.
