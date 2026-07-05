# AI Training: ML Security

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
- Perform hands-on labs using BrokenPilot, the toy classifier lab, and the MLOps evidence-pack review
- Design mitigations that balance security, usability, and developer velocity
- Produce useful engineering deliverables: threat models, risk registers, red-team reports, secure architecture reviews, and residual-risk statements

## Website edition

The repository includes a MkDocs Material website layer. The canonical course content lives in the root-level `modules/`, `labs/`, `course-templates/`, `instructor/`, and `assessments/` directories. MkDocs source is generated into `.mkdocs-src/` before preview or deployment so the course is not hand-maintained in two places.

Preview locally on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\sync_mkdocs_content.py
mkdocs serve
```

Preview locally on macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/sync_mkdocs_content.py
mkdocs serve
```

Then open:

```text
http://127.0.0.1:8000
```

GitHub Pages deployment is configured through `.github/workflows/deploy-docs.yml`. In GitHub, set **Settings > Pages > Source** to **GitHub Actions**.

## Source of truth

Canonical course content lives in the root-level content directories. MkDocs source is generated into `.mkdocs-src/` before preview or deployment. See `SOURCE_OF_TRUTH.md`.

## Repository structure

```text
ai-training-ml-security/
├── README.md
├── mkdocs.yml
├── requirements.txt
├── CHANGELOG.md
├── RELEASE_TAGGING_GUIDE.md
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
│   └── releases/
├── modules/
├── labs/
├── course-templates/
├── instructor/
├── assessments/
└── scripts/
```

The root-level `modules/`, `labs/`, `course-templates/`, `instructor/`, and `assessments/` directories are the source of truth. The `docs/` directory contains only website-only pages such as the landing page, start-here material, lab setup notes, and release notes. Generated MkDocs source is built into `.mkdocs-src/` by `scripts/sync_mkdocs_content.py` and is ignored by Git.

## Development status

Current release: v1.1.0.1.0.

The v1 release is the first stable teaching release. It includes the full 12-module course, validated runnable labs, instructor guidance, assessment material, MkDocs strict navigation, and release-quality usage and licensing guidance.

Completed in the v1.1.0 line:

1. BrokenPilot-primary lab validation, with DVAIA retained only as optional external practice.
2. BrokenPilot runnable MVP with retrieval, tool-calling, memory poisoning, control toggles, and tests.
3. Deeper reading-first material for Modules 05, 06, 07, and 10.
4. Worked examples, grading calibration, finding rewrite exercises, and executive communication exercises.
5. 40-hour / one-week professional delivery model.
6. Single-source-of-truth MkDocs generation workflow.

## Lab philosophy

Existing vulnerable projects should be used where possible. The course value is in the structure, explanations, lab guides, architecture discussions, mitigation design, and assessment material.

BrokenPilot is the primary runnable lab environment for the LLM, RAG, agent, privacy, red-team, and capstone path. DVAIA and similar projects may be used as optional external practice, but they are not the primary course path.

Labs should be local, controlled, fake-data environments. The goal is to teach security reasoning, not to attack systems the student does not own.

## License

This repository uses a non-commercial split-license model:

- Course content: **CC BY-NC-SA 4.0**.
- Original code and runnable labs: **PolyForm Noncommercial 1.0.0**.
- Internal organizational learning is permitted when attribution is preserved and the material is not sold, productized, or delivered as a paid external offering.
- Commercial use, resale, paid workshops, paid platforms, and paid consulting delivery require prior written permission.

See `LICENSE.md`, `LICENSE-CONTENT.md`, `LICENSE-CODE.md`, and `COMMERCIAL-LICENSE.md`.

## Course status

Current release: v1.1.0.1.0.

| Module | Status | Notes |
|---|---|---|
| 01  -  Security Engineering for AI | Complete | Reference module with slides, notes, handout, exercise, checklist, quiz, and references. |
| 02  -  ML System Architecture | Complete | Lifecycle architecture, DFD exercise, architecture review template. |
| 03  -  OWASP ML Security Top 10 | Complete | Classical ML attack categories and toy ML lab. |
| 04  -  BIML Architectural Risk Analysis | Complete | Design review, abuse cases, architectural risk review lab. |
| 05  -  LLM Application Security | Complete | OWASP LLM/GenAI framing and DVAIA-style LLM lab. |
| 06  -  RAG Security and Indirect Prompt Injection | Complete | RAG architecture, retrieval authorization, indirect prompt injection, RAG lab, and templates. |
| 07  -  Agent and Tool Security | Complete | Tool calling, excessive agency, memory poisoning, approval gates, sandboxing, auditability, and agent control design. |
| 08  -  Secure MLOps and Supply Chain | Complete | Datasets, notebooks, dependencies, training jobs, model artifacts, registries, provenance, promotion gates, feedback loops, and ML-BOM templates. |
| 09  -  Privacy Attacks | Complete | Membership inference, model inversion, training data extraction, prompt/log leakage, embedding leakage, cross-tenant retrieval, memory leakage, and privacy risk assessment templates. |
| 10  -  Adversarial ML and Robustness | Complete | Evasion, poisoning, backdoors, drift, confidence, fallback behavior, monitoring, robustness evaluation, and adversarial test planning. |
| 11  -  AI Red Team Methodology | Complete | Scope, rules of engagement, attack planning, controlled testing, evidence, severity, reporting, executive readout, remediation, and residual risk. |
| 12  -  BrokenPilot Capstone | Complete | Full capstone teaching package, runbook, exercises, final presentation guide, evidence log, remediation backlog, templates, and assessment rubric. |

## Maintenance focus

The v1 release is intended to be stable for teaching. Future work should focus on:

- preserving BrokenPilot as the primary runnable lab path
- keeping lab tests and MkDocs strict checks green
- improving instructor handoff based on real delivery feedback
- keeping optional external practice clearly marked as optional
- reducing file sprawl only when it improves maintainability

## Recommended delivery target

The recommended instructor-led version is a **40-hour / one-week professional training**. The course remains usable for self-study, but live delivery should prioritize deep explanation, validated labs, concrete controls, decision-grade findings, and the BrokenPilot capstone.

<!-- content-quality-reading-flow-note -->

## Study flow note

Each module includes a `student-reading-guide.md` file. Use it before the deep dive or lab to understand the core security decision, the lab modality, the expected deliverable, and the exit ticket for the module.

<!-- course-storyline-link -->

## Course storyline

The course is organized as one security engineering journey: map the AI system, identify trust boundaries, observe failure modes, design enforceable controls, validate those controls, document validation evidence, and communicate residual risk. See [COURSE_STORYLINE.md](COURSE_STORYLINE.md).

## Release and usage

For release scope, quality gates, and licensing, see:

- [`COURSE_RELEASE_MANIFEST.md`](COURSE_RELEASE_MANIFEST.md)
- [`USAGE_AND_LICENSING_GUIDE.md`](USAGE_AND_LICENSING_GUIDE.md)
- [`RELEASE_TAGGING_GUIDE.md`](RELEASE_TAGGING_GUIDE.md)

Maintainer-only release evidence lives under `instructor/release-readiness/release-process-docs/`.

The course is free for self-study and internal company learning with attribution. Commercial training, resale, hosted-course use, or repackaging requires separate permission.
