# AI Training — ML Security

**Security engineering for systems that contain machine learning.**

This repository contains a GitHub-ready curriculum for practical ML, LLM, RAG, and agent security training. The goal is not to reinvent software security. The goal is to apply strong security engineering foundations to systems where models, datasets, prompts, retrieval pipelines, tools, and autonomous workflows become part of the attack surface.

This training is designed for security engineers, AppSec teams, ML engineers, platform engineers, architects, security champions, red teams, and engineering leaders.

## Core idea

ML Security is not separate from software security. It is software security, data security, cloud security, identity security, privacy engineering, supply chain security, and adversarial ML applied to systems that contain machine learning.

AI systems fail through:

- Normal software flaws
- Normal infrastructure flaws
- Normal identity and access-control flaws
- Normal cryptographic mistakes
- Normal supply chain compromises
- New ML-specific failure modes
- New LLM, RAG, and agent-specific failure modes

The course therefore teaches students to reason about the whole system: code, model, data, users, tools, permissions, business workflows, logs, monitoring, and residual risk.

## What this course is not

This is not only prompt injection training.

This is not generic AI safety.

This is not a collection of jailbreak screenshots.

This is not a replacement for secure software engineering.

## What this course is

This is practical security engineering for AI-enabled systems.

Students learn how to:

- Threat model AI systems
- Understand ML, LLM, RAG, and agent attack surfaces
- Use OWASP, BIML, NIST, MITRE ATLAS, and classic security literature
- Perform hands-on labs using existing vulnerable environments such as DVAIA
- Design mitigations that balance security, usability, and developer velocity
- Produce useful engineering deliverables: threat models, risk registers, red-team reports, secure architecture reviews, and residual-risk statements

## Repository structure

```text
ai-training-ml-security/
├── README.md
├── syllabus.md
├── course-map.md
├── references.md
├── CHANGELOG.md
├── RELEASE_CHECKLIST.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── .github/
├── modules/
│   ├── 01-security-engineering-for-ai/
│   ├── 02-ml-system-architecture/
│   ├── 03-owasp-ml-top-10/
│   ├── 04-biml-architectural-risk-analysis/
│   ├── 05-llm-application-security/
│   ├── 06-rag-security/
│   ├── 07-agent-tool-security/
│   ├── 08-secure-mlops-supply-chain/
│   ├── 09-privacy-attacks/
│   ├── 10-adversarial-ml-robustness/
│   ├── 11-ai-red-team-methodology/
│   └── 12-capstone-brokenpilot/
├── labs/
│   ├── dvaia-guides/
│   ├── rag-labs/
│   ├── agent-labs/
│   ├── toy-ml-attacks/
│   └── brokenpilot/
├── templates/
├── instructor/
└── assessments/
```

## Build order

The project is now at a **v1.0 release-candidate** stage. The core curriculum spine is complete and all twelve modules have full teaching packages.

Completed for v1.0:

1. Finalized the syllabus and course map.
2. Completed Modules 01–12 as teachable units.
3. Built reusable templates for threat modeling, architecture review, privacy review, AI red teaming, MLOps review, agent control design, and capstone reporting.
4. Mapped DVAIA-style labs to OWASP and course modules.
5. Designed the BrokenPilot capstone as a complete paper-based exercise.
6. Added release readiness files: changelog, release checklist, security policy, code of conduct, issue templates, and PR template.

Recommended work after v1.0:

1. Expand selected lab wrappers with more concrete screenshots and environment-specific steps after testing DVAIA locally.
2. Convert BrokenPilot from paper design into a local vulnerable lab application.
3. Add optional slide-rendering workflows later if needed, while keeping Markdown as the source of truth.
4. Add more instructor examples from real architecture reviews and red-team reports.

## Lab philosophy

Existing vulnerable projects should be used where possible. The course value is in the structure, explanations, lab guides, architecture discussions, mitigation design, and assessment material.

DVAIA and similar projects can provide the hands-on substrate. This curriculum provides the learning path.

Labs should be local, controlled, fake-data environments. The goal is to teach security reasoning, not to attack systems the student does not own.

## License

The current repository includes `LICENSE.md` with a practical split-license model:

- Training content: Creative Commons Attribution 4.0 style terms.
- Future code/labs: Apache 2.0 or MIT can be added when code is introduced.

Review the license text before making the repository public.

## Course status

Current working version: **v1.0 release candidate**. Modules 01–12 have complete teaching packages, the BrokenPilot capstone is ready to teach, and the repository includes release-readiness material for a first public or private tagged release.

| Module | Status | Notes |
|---|---|---|
| 01 — Security Engineering for AI | Complete | Reference module with slides, notes, handout, exercise, checklist, quiz, and references. |
| 02 — ML System Architecture | Complete | Lifecycle architecture, DFD exercise, architecture review template. |
| 03 — OWASP ML Security Top 10 | Complete | Classical ML attack categories and toy ML lab. |
| 04 — BIML Architectural Risk Analysis | Complete | Design review, abuse cases, architectural risk review lab. |
| 05 — LLM Application Security | Complete | OWASP LLM/GenAI framing and DVAIA-style LLM lab. |
| 06 — RAG Security and Indirect Prompt Injection | Complete | RAG architecture, retrieval authorization, indirect prompt injection, RAG lab, and templates. |
| 07 — Agent and Tool Security | Complete | Tool calling, excessive agency, memory poisoning, approval gates, sandboxing, auditability, and agent control design. |
| 08 — Secure MLOps and Supply Chain | Complete | Datasets, notebooks, dependencies, training jobs, model artifacts, registries, provenance, promotion gates, feedback loops, and ML-BOM templates. |
| 09 — Privacy Attacks | Complete | Membership inference, model inversion, training data extraction, prompt/log leakage, embedding leakage, cross-tenant retrieval, memory leakage, and privacy risk assessment templates. |
| 10 — Adversarial ML and Robustness | Complete | Evasion, poisoning, backdoors, drift, confidence, fallback behavior, monitoring, robustness evaluation, and adversarial test planning. |
| 11 — AI Red Team Methodology | Complete | Scope, rules of engagement, attack planning, controlled testing, evidence, severity, reporting, executive readout, remediation, and residual risk. |
| 12 — BrokenPilot Capstone | Complete | Full capstone teaching package, runbook, exercises, final presentation guide, evidence log, remediation backlog, templates, and assessment rubric. |

## Previous update — v0.8

Module 7 — Agent and Tool Security is now complete.

Added:

- Agent and tool security slides
- Instructor notes
- Student handout
- Agent control design exercise
- Agent security checklist
- Quiz and answer key
- Agent tool misuse lab guide
- Memory poisoning and approval gates lab guide
- Agent control design template
- Tool permission matrix template
- Agent action approval policy template


## Build status update — v0.9

BrokenPilot capstone paper design is now complete.

Added:

- Scenario and business context
- Architecture and trust-boundary model
- Roles and attacker personas
- Fake data model
- Tool inventory and permission model
- Intentional vulnerability list
- Suggested attack paths
- Student-facing brief
- Instructor solution guide
- Secure reference architecture
- BrokenPilot-specific grading rubric
- Implementation notes for a future local lab
- Final report template

Next recommended work: Module 11 — AI Red Team Methodology.


## Build status update — v0.10

Module 8 — Secure MLOps and AI Supply Chain is now complete.

Added:

- Secure MLOps and AI supply chain slides
- Instructor notes
- Student handout
- Secure MLOps review exercise
- Secure MLOps checklist
- Quiz and answer key
- Broken ML pipeline lab guide
- Model artifact provenance lab guide
- Secure MLOps review template
- Dataset provenance review template
- Model artifact risk review template
- Model registry access-control template
- ML-BOM template

Next recommended work: Module 11 — AI Red Team Methodology.


## Build status update — v0.11

Module 9 — Privacy Attacks and Data Protection is now complete.

Added:

- Privacy attacks and data protection slides
- Instructor notes
- Student handout
- AI privacy risk assessment exercise
- AI privacy checklist
- Quiz and answer key
- Privacy leakage and cross-tenant RAG lab guide
- Membership inference and model inversion tabletop lab
- Privacy risk assessment template
- AI data retention and log review template
- AI privacy control checklist

Next recommended work: Module 11 — AI Red Team Methodology.


## Build status update — v0.12

Module 10 — Adversarial ML and Robustness is now complete.

Added:

- Adversarial ML and robustness slides
- Instructor notes
- Student handout
- Adversarial test plan exercise
- Adversarial ML robustness checklist
- Quiz and answer key
- Evasion and robustness lab guide
- Poisoning, backdoor, and feedback-loop tabletop lab
- Adversarial test plan template
- Robustness evaluation template
- Drift and abuse monitoring template

Next recommended work: Module 11 — AI Red Team Methodology.


## Build status update — v0.13

Module 11 — AI Red Team Methodology is now complete.

Added:

- AI red team methodology slides
- Instructor notes
- Student handout
- AI red team planning exercise
- AI red team checklist
- Quiz and answer key
- AI red team scoping tabletop lab
- BrokenPilot attack-chain red team lab
- AI red team scope template
- AI red team attack plan template
- AI red team report template
- AI red team executive readout template
- AI red team grading rubric

Next recommended work: expand Module 12 — BrokenPilot Capstone into a full teaching package and prepare the v1.0 teachable release review.


## Build status update — v0.14

Module 12 — BrokenPilot Capstone is now complete as a full teaching package.

Added:

- Capstone slide deck
- Instructor notes
- Student handout
- Capstone threat-modeling exercise
- Capstone red team and mitigation-design exercise
- Capstone checklist
- Quiz and answer key
- Expanded capstone runbook
- Module 12 references
- Final presentation guide
- Evidence log guide
- Remediation backlog guide
- BrokenPilot risk register template
- BrokenPilot evidence log template
- BrokenPilot remediation backlog template
- Final capstone grading rubric

Next recommended work: perform a v1.0 release review, clean stale status sections, verify references, review license wording, and decide whether the repository should remain private or become public.
