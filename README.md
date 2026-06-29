# AI Training — ML Security

**Security engineering for systems that contain machine learning.**

This repository contains a GitHub-ready and MkDocs-ready curriculum for practical ML, LLM, RAG, and agent security training. The goal is not to reinvent software security. The goal is to apply strong security engineering foundations to systems where models, datasets, prompts, retrieval pipelines, tools, and autonomous workflows become part of the attack surface.

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

## Website edition

The repository now includes a MkDocs Material website layer. The website turns the Markdown curriculum into a browsable training portal with navigation, search, module pages, lab setup pages, templates, and release documentation.

Preview locally:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

GitHub Pages deployment is configured through `.github/workflows/deploy-docs.yml`. In GitHub, set **Settings → Pages → Source** to **GitHub Actions**.

## Repository structure

```text
ai-training-ml-security/
├── README.md
├── mkdocs.yml
├── requirements.txt
├── CHANGELOG.md
├── RELEASE_CHECKLIST.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   └── deploy-docs.yml
│   └── pull_request_template.md
├── docs/
│   ├── index.md
│   ├── start-here/
│   ├── lab-setup/
│   ├── modules/
│   ├── labs/
│   ├── templates/
│   ├── instructor/
│   ├── assessments/
│   └── releases/
├── modules/
├── labs/
├── templates/
├── instructor/
└── assessments/
```

The `docs/` directory is the MkDocs website source. The root-level `modules/`, `labs/`, `templates/`, `instructor/`, and `assessments/` directories are preserved for repository browsing and compatibility with the v1.0 structure.

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

This repository uses a non-commercial split-license model:

- Course content: **CC BY-NC-SA 4.0**.
- Original code and runnable labs: **PolyForm Noncommercial 1.0.0**.
- Internal organizational learning is permitted when attribution is preserved and the material is not sold, productized, or delivered as a paid external offering.
- Commercial use, resale, paid workshops, paid platforms, and paid consulting delivery require prior written permission.

See `LICENSE.md`, `LICENSE-CONTENT.md`, `LICENSE-CODE.md`, and `COMMERCIAL-LICENSE.md`.

## Course status

Current working version: **v1.1 website edition draft**. Modules 01–12 have complete teaching packages, the BrokenPilot capstone is ready to teach, and the repository includes release-readiness material and a MkDocs Material website layer for local preview and GitHub Pages publishing.

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


## Current development focus

The next development phase is not another release tag. It is focused on quality and testability:

1. Validate DVAIA locally and document exact setup notes.
2. Design a minimal runnable BrokenPilot prototype.
3. Add worked capstone examples for grading consistency.
4. Add instructor delivery guidance for different course lengths.
5. Add concrete control deliverables that require students to design implementable fixes.
6. Deepen Module 10 with worked adversarial ML examples.

The website layer is useful, but the highest priority is making the course more hands-on and instructor-ready.
