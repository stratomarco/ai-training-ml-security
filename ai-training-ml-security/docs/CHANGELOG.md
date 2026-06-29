# Changelog

## v1.1.0 — Website edition draft

### Added

- Added MkDocs Material website configuration in `mkdocs.yml`.
- Added Python dependency file `requirements.txt`.
- Added GitHub Pages deployment workflow at `.github/workflows/deploy-docs.yml`.
- Added website landing page at `docs/index.md`.
- Added Start Here section for overview, prerequisites, usage, and lab safety.
- Added Lab Setup section for local preview, DVAIA setup, and GitHub Pages deployment.
- Mirrored modules, labs, templates, instructor material, and assessments into `docs/` for website publishing.
- Added repository `.gitignore` for Python virtual environments and MkDocs build output.

### Notes

This release does not change the curriculum substance. It makes the material easier to browse, teach, and publish as a static training website.

All notable changes to this project are documented here.

The project uses a curriculum-oriented versioning model:

- `v0.x` versions track build milestones.
- `v1.0.0` represents the first complete teachable curriculum.
- Later versions should document content changes, new labs, corrections, and major restructuring.

## v1.0.0-rc2 — Review cleanup

### Fixed

- Removed incremental build-status notes from `README.md`, `syllabus.md`, and `course-map.md`.
- Updated Module 01 NIST adversarial ML reference from the old e2023 draft to NIST AI 100-2 E2025.
- Updated OWASP LLM02:2025 Sensitive Information Disclosure links to the current OWASP GenAI page.
- Updated Module 05 OWASP LLM framing to 2025 numbering and added an explicit note about 2023/2024 renumbering.
- Added missing primary URLs to Module 08 Secure MLOps references.
- Clarified that OWASP Agentic Skills Top 10 is supplementary to the Agentic Applications Top 10 risk framing.

## v1.0.0-rc — Release candidate

### Added

- Complete twelve-module ML Security curriculum.
- BrokenPilot capstone teaching package.
- Markdown-based module structure for every module:
  - overview
  - slides
  - instructor notes
  - student handout
  - exercise
  - checklist
  - quiz
  - references
- Lab wrappers for:
  - DVAIA-style LLM application security
  - RAG and indirect prompt injection
  - agent tool misuse
  - memory poisoning and approval gates
  - secure MLOps and AI supply chain
  - privacy leakage and membership inference tabletop
  - adversarial ML robustness
  - AI red team scoping and attack-chain exercises
  - BrokenPilot capstone
- Templates for:
  - threat modeling
  - abuse cases
  - architecture review
  - risk register
  - red team reporting
  - residual risk
  - ML architecture review
  - ML attack summaries
  - RAG threat modeling
  - agent control design
  - tool permission matrices
  - MLOps and ML-BOM review
  - privacy risk assessment
  - adversarial test planning
  - AI red team scope, attack plan, report, and executive readout
  - BrokenPilot final reporting
- Release readiness files:
  - `RELEASE_CHECKLIST.md`
  - `VERSION.md`
  - `ROADMAP.md`
  - `SECURITY.md`
  - `CODE_OF_CONDUCT.md`
  - GitHub issue templates
  - Pull request template
  - `docs/releases/v1.0.0.md`

### Changed

- Updated repository status from draft module build to v1.0 release candidate.
- Updated backlog to distinguish completed curriculum work from post-v1.0 implementation work.
- Clarified license strategy for content, future code, and third-party labs.

### Not yet included

- A custom runnable BrokenPilot vulnerable application.
- Validated DVAIA setup instructions for each operating system.
- Rendered PowerPoint/PDF slide decks.
- Full legal review of license text.

## v0.14 — Module 12 complete

### Added

- Full BrokenPilot capstone teaching package.
- Capstone slides, instructor notes, handout, exercises, checklist, quiz, and references.
- Final presentation, evidence log, remediation backlog, risk register, and grading material.

## v0.13 — Module 11 complete

### Added

- AI Red Team Methodology module.
- Red team scoping tabletop.
- BrokenPilot attack-chain lab.
- Red team scope, attack plan, report, and executive readout templates.

## v0.12 — Module 10 complete

### Added

- Adversarial ML and Robustness module.
- Evasion and robustness lab.
- Poisoning and backdoor tabletop.
- Adversarial test plan and robustness evaluation templates.

## v0.11 — Module 9 complete

### Added

- Privacy Attacks and Data Protection module.
- Cross-tenant RAG privacy lab.
- Membership inference and model inversion tabletop.
- Privacy risk and retention review templates.

## v0.10 — Module 8 complete

### Added

- Secure MLOps and AI Supply Chain module.
- Broken ML pipeline lab.
- Model artifact provenance lab.
- ML-BOM and supply chain templates.

## v0.9 — BrokenPilot paper design

### Added

- BrokenPilot scenario, architecture, roles, data model, tools, vulnerabilities, attack paths, secure reference architecture, and instructor solution.

## v0.8 — Module 7 complete

### Added

- Agent and Tool Security module.
- Tool misuse lab.
- Memory poisoning and approval-gates lab.
- Agent control design templates.

## v0.7 — Module 6 complete

### Added

- RAG Security and Indirect Prompt Injection module.
- RAG lab wrapper.
- RAG and vector database templates.

## v0.6 — Module 5 complete

### Added

- LLM Application Security module.
- DVAIA-style LLM lab guide.
- LLM security review template.

## v0.5 — Module 4 complete

### Added

- BIML Architectural Risk Analysis module.
- Architecture review lab and template.

## v0.4 — Module 3 complete

### Added

- OWASP ML Security Top 10 module.
- Classical ML attack lab wrapper.

## v0.3 — Module 2 complete

### Added

- ML System Architecture module.
- ML lifecycle DFD exercise.

## v0.2 — Module 1 complete

### Added

- Security Engineering for AI module.
- Reference module structure.
- Reusable module template.

## v0.1 — Curriculum skeleton

### Added

- Initial repository skeleton.
- Syllabus.
- Course map.
- Reference list.
- Initial templates and lab strategy.
