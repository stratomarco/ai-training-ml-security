# Syllabus

## Course name

AI Training — ML Security

## Tagline

Security engineering for systems that contain machine learning.

## Course positioning

This course teaches practical ML, LLM, RAG, and agent security using strong security engineering foundations. It connects classic software security, cloud security, identity, cryptography, privacy, supply chain security, and adversarial thinking to the specific risks introduced by machine learning systems.

The course is designed to avoid shallow prompt-hacking-only training. Prompt injection matters, but it is only one part of the wider problem.

## Target audience

Primary audience:

- Application security engineers
- Product security engineers
- Security architects
- Cloud security engineers
- Platform engineers
- ML engineers
- Security champions
- Red teamers
- Engineering leaders working with AI systems

Secondary audience:

- CISOs
- Security managers
- Privacy engineers
- Risk teams
- Product managers responsible for AI-enabled products

## Required background

Students should ideally understand:

- Web application architecture
- APIs
- Authentication and authorization
- Common web vulnerabilities
- Basic cloud concepts
- Basic Python or scripting
- Basic machine learning concepts such as dataset, model, training, inference, evaluation, and deployment

Students do not need to be ML researchers.

## Learning outcomes

By the end of the course, students should be able to:

1. Explain why ML Security is an extension of security engineering.
2. Identify assets, trust boundaries, and attack surfaces in ML, LLM, RAG, and agent systems.
3. Threat model an AI-enabled application.
4. Explain the difference between traditional software risks and ML-specific risks.
5. Demonstrate prompt injection, indirect prompt injection, RAG poisoning, tool abuse, excessive agency, model theft, data leakage, and basic poisoning attacks in a lab.
6. Map findings to OWASP, BIML, NIST, and MITRE ATLAS-style categories.
7. Design practical mitigations that balance security, usability, and developer velocity.
8. Produce a red-team report, architecture review, risk register, and residual-risk statement for an AI system.
9. Explain AI security risks to engineers and leadership without hype.
10. Build a repeatable security testing approach for AI-enabled systems.

## Course modules

| Module | Title | Main outcome |
|---|---|---|
| 01 | Security Engineering for AI | Understand why AI security starts with classic security principles |
| 02 | ML System Architecture | Understand the ML lifecycle and its security boundaries |
| 03 | OWASP ML Top 10 | Learn classical ML attack categories |
| 04 | BIML and Architectural Risk Analysis | Review AI systems at design level |
| 05 | LLM Application Security | Treat LLM risks as application security problems |
| 06 | RAG Security and Indirect Prompt Injection | Secure retrieval and context pipelines |
| 07 | Agent and Tool Security | Secure AI systems that can take actions |
| 08 | Secure MLOps and AI Supply Chain | Secure datasets, artifacts, pipelines, and model registries |
| 09 | Privacy Attacks and Data Protection | Understand leakage, inference, and privacy abuse |
| 10 | Adversarial ML and Robustness | Test models under adversarial pressure |
| 11 | AI Red Team Methodology | Create repeatable AI security testing programs |
| 12 | Capstone: BrokenPilot | Threat model, attack, defend, and present residual risk |

## Teaching model

Each module should include:

- Theory
- Security engineering connection
- ML, LLM, RAG, or agent-specific risk
- Realistic scenario
- Hands-on lab or tabletop exercise
- Defensive design patterns
- Discussion questions
- Deliverable
- Instructor notes
- Student checklist

## Lab model

Every lab should follow this structure:

1. Context
2. Architecture
3. Asset at risk
4. Vulnerability
5. Exploit walkthrough
6. Impact
7. Root cause
8. Secure design
9. Fix or mitigation
10. Discussion questions
11. Extension challenge

Every lab must map to a real engineering decision. No lab should exist only because it is a cool trick.

## Assessment model

Students should be assessed on:

- Security reasoning
- Ability to identify trust boundaries
- Quality of threat model
- Exploit understanding
- Mitigation quality
- Ability to balance security and usability
- Communication to developers
- Communication to leadership
- Residual risk thinking

The goal is not to reward only exploitation. The goal is to reward complete security judgment.


## v0.8 curriculum status

Modules 01–07 became complete teaching packages. Module 07 added agent and tool security, including excessive agency, tool misuse, memory poisoning, approval gates, sandboxing, auditability, and agent control design.


## v0.9 update

The BrokenPilot capstone paper design is now complete. This includes scenario, architecture, roles, data model, tools, vulnerability list, attack paths, student brief, instructor solution guide, secure reference architecture, grading rubric, implementation notes, and module mapping.

The next recommended build step is Module 11 — AI Red Team Methodology.


## v0.10 update

Module 08 — Secure MLOps and AI Supply Chain is now complete. It adds training material for datasets, labels, notebooks, dependencies, training infrastructure, model artifacts, registries, provenance, promotion gates, feedback-loop security, and ML-BOM thinking.

The next recommended build step is Module 11 — AI Red Team Methodology.


## v0.11 update

Module 09 — Privacy Attacks and Data Protection is now complete. It adds training material for membership inference, model inversion, training data extraction, prompt and completion leakage, log leakage, embedding leakage, vector database exposure, cross-tenant retrieval, agent memory leakage, feedback-loop reuse, retention, deletion, and privacy risk assessment.

The next recommended build step is Module 11 — AI Red Team Methodology.


## v0.12 update

Module 10 — Adversarial ML and Robustness is now complete. It adds training material for evasion, poisoning, backdoors, trigger-based behavior, distribution shift, concept drift, confidence calibration, robustness testing, fallback behavior, monitoring, incident response, and secure retraining.

The next recommended build step is Module 11 — AI Red Team Methodology.


## Current status

Current working version: v0.14 draft. Modules 01–12 have complete teaching packages, and the BrokenPilot capstone is ready for v1.0 release review.


## v0.13 update — Module 11 complete

Module 11 — AI Red Team Methodology is complete. It covers scope, rules of engagement, safety boundaries, system understanding, threat modeling, attack planning, controlled testing, evidence collection, severity scoring, reporting, remediation, executive readout, and residual risk.

The module includes labs for AI red team scoping and BrokenPilot attack-chain planning, plus templates for scope, attack plans, full reports, executive readouts, and grading.


## v0.14 update — Module 12 complete

Module 12 — BrokenPilot Capstone is now complete as a full teaching package.

Added:

- Capstone slides
- Instructor notes
- Student handout
- Threat-modeling exercise
- Red team and mitigation-design exercise
- Capstone checklist
- Quiz and answer key
- Expanded capstone runbook
- Final presentation guide
- Evidence log guide
- Remediation backlog guide
- BrokenPilot-specific templates
- Final capstone assessment rubric

The course now has complete teaching packages for Modules 01–12. The next milestone is v1.0 release readiness: consistency review, reference review, license review, and optional public-release cleanup.
