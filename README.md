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
- Perform hands-on labs using existing vulnerable environments such as DVAIA
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

Current working version: **v1.1-dev testable-labs and course-depth draft**.

The v1.0 curriculum has been released. Current development focuses on making the course more portable, testable, instructor-ready, and self-study friendly before any future v1.1 release tag.

Completed in the v1.1-dev line:

1. DVAIA local validation and DVAIA-backed walkthroughs.
2. BrokenPilot runnable MVP with retrieval, tool-calling, memory poisoning, control toggles, and tests.
3. Deeper reading-first material for Modules 05, 06, 07, and 10.
4. Worked examples, grading calibration, finding rewrite exercises, and executive communication exercises.
5. 40-hour / one-week professional delivery model.
6. Single-source-of-truth MkDocs generation workflow.

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

Current working version: **v1.1-dev testable-labs and course-depth draft**. Modules 01–12 have complete teaching packages. DVAIA has been locally validated as an external lab dependency, BrokenPilot has a runnable MVP, and the course is being hardened for a future v1.1 release.

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

## Current development focus

The next development phase is not another release tag. It is focused on quality and testability:

1. Validate DVAIA locally and document exact setup notes.
2. Design a minimal runnable BrokenPilot prototype.
3. Add worked capstone examples for grading consistency.
4. Add instructor delivery guidance for different course lengths.
5. Add concrete control deliverables that require students to design implementable fixes.
6. Deepen Module 10 with worked adversarial ML examples.

The website layer is useful, but the highest priority is making the course more hands-on and instructor-ready.

## Recommended delivery target

The recommended instructor-led version is a **40-hour / one-week professional training**. The course remains usable for self-study, but live delivery should prioritize deep explanation, validated labs, concrete controls, decision-grade findings, and the BrokenPilot capstone.

<!-- content-quality-reading-flow-note -->

## Study flow note

Each module includes a `student-reading-guide.md` file. Use it before the deep dive or lab to understand the core security decision, the lab modality, the expected deliverable, and the exit ticket for the module.

<!-- course-storyline-link -->

## Course storyline

The course is organized as one security engineering journey: map the AI system, identify trust boundaries, observe failure modes, design enforceable controls, validate those controls, document validation evidence, and communicate residual risk. See [COURSE_STORYLINE.md](COURSE_STORYLINE.md) and [COURSE_VOICE_AND_COHESION_REVIEW.md](COURSE_VOICE_AND_COHESION_REVIEW.md).

## Release and usage

For release scope, quality gates, and licensing, see:

- [`COURSE_RELEASE_MANIFEST.md`](COURSE_RELEASE_MANIFEST.md)
- [`QUALITY_GATE_BASELINE.md`](QUALITY_GATE_BASELINE.md)
- [`USAGE_AND_LICENSING_GUIDE.md`](USAGE_AND_LICENSING_GUIDE.md)
- [`RELEASE_TAGGING_GUIDE.md`](RELEASE_TAGGING_GUIDE.md)

The course is free for self-study and internal company learning with attribution. Commercial training, resale, hosted-course use, or repackaging requires separate permission.
