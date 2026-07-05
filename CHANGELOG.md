# Changelog

## v1.1-dev-rc1 - release candidate

This release-candidate checkpoint marks the course as ready for final review after the release cleanup sequence.

Validation baseline:

- Repository structure check.
- Content readiness check.
- Lab target presence check.
- MkDocs strict build.
- BrokenPilot pytest suite.
- Toy classifier pytest suite.

Course status:

- BrokenPilot is the primary runnable capstone environment.
- The toy classifier lab is the primary classical ML attack environment.
- The MLOps evidence-pack lab is the primary secure MLOps reasoning lab.
- Optional legacy or external lab paths are marked as optional and are not required for the published course path.

Known non-blocking item:

- Material for MkDocs may print an upstream MkDocs 2.0 warning banner. That banner is informational and is not a course release blocker.


## v1.1-dev structural cleanup and portability review

Applied review-driven cleanup before further content work.

Changed:

- Made root-level course directories the canonical source of truth.
- Removed committed duplicate MkDocs module, lab, template, instructor, and assessment copies from `docs/`.
- Added `scripts/sync_mkdocs_content.py` to generate `.mkdocs-src/` for MkDocs.
- Added cleanup and repository-structure checks to prevent stale nested copies.
- Added em dash linting and removed em dashes from source Markdown/configuration.
- Added cross-platform Windows and macOS/Linux setup instructions.
- Pinned the validated DVAIA commit and documented the BrokenPilot fallback path.
- Clarified that the BrokenPilot mock prompt-injection marker check is a deterministic teaching stand-in, not a production control.
- Added BrokenPilot capstone assessment scope so runnable and tabletop assessment boundaries are explicit.
- Reconciled version/status strings to `v1.1-dev testable-labs and course-depth draft`.

Validation:

- `python scripts/check_repo_structure.py`: passed.
- `python scripts/check_no_em_dash.py`: passed.
- MkDocs source sync: passed.
- MkDocs nav path check: 0 missing.
- `mkdocs build`: passed.
- BrokenPilot tests: `10 passed`.

## v1.1-dev  -  40-hour one-week course delivery model

- Added a recommended 40-hour / one-week professional training delivery model.
- Added instructor 40-hour delivery plan and one-week course runbook.
- Added student-facing one-week learning path.
- Added 40-hour assessment plan balancing threat modeling, evidence logs, concrete controls, finding quality, executive communication, and BrokenPilot capstone.
- Updated instructor and assessment indexes and MkDocs navigation.

## v1.1-dev  -  Module 10 reading-first deepening

## Unreleased  -  BrokenPilot final report examples

- Added a gold-standard BrokenPilot final report example that combines evidence, root-cause analysis, remediation, residual risk, and executive recommendation.
- Added a weak final report contrast example to show common failure modes in student submissions.
- Added instructor notes for using the final report examples during grading calibration.
- Added MkDocs navigation entries for the complete final report examples.


Deepened Module 10  -  Adversarial ML and Robustness with reading-first materials:

- Added a conceptual deep dive explaining adversarial ML as production security engineering and robustness under adversarial pressure.
- Added attack anatomy coverage for evasion, text perturbation, poisoning, backdoors, model skewing, and drift.
- Added controls and remediations guidance focused on input/feature controls, provenance, evaluation, fallback, monitoring, and recovery.
- Added common mistakes to help students avoid vague answers such as “improve accuracy” or “retrain the model.”
- Added a worked example for a fraud-classifier adversarial robustness review.
- Updated Module 10 overview, student handout, instructor notes, and MkDocs navigation.


## v1.1-dev  -  Module 05 reading-first deepening

Deepened Module 05  -  LLM Application Security with reading-first materials:

- Added a conceptual deep dive explaining LLM application security as security engineering around a probabilistic component.
- Added attack anatomy coverage for prompt injection, indirect prompt injection, sensitive information disclosure, improper output handling, excessive agency, system prompt leakage, and unbounded consumption.
- Added controls and remediations guidance focused on deterministic controls outside the model.
- Added common mistakes to help students avoid prompt-only fixes and weak reporting.
- Added a worked example showing how to turn “the model was jailbroken” into an engineering-grade finding.
- Updated Module 05 overview, student handout, instructor notes, and MkDocs navigation.

# Changelog

## v1.1-dev  -  Content strategy and licensing update

- Added reading-first, lab-supported content strategy.
- Added content strategy and reading-first pages to the MkDocs site.
- Added deep-dive, attack anatomy, and controls/remediations templates.
- Replaced permissive split-license wording with a non-commercial split-license model.
- Added explicit permission for internal organizational learning with attribution when material is not sold, productized, or delivered as a paid external offering.
- Added content license, code license, and commercial licensing policy files.



## v1.1-dev  -  BrokenPilot worked examples and Module 07 validation refinement

### Added

- Added strong and weak BrokenPilot tool permission matrix examples.
- Added strong and weak BrokenPilot evidence log examples.
- Added strong and weak BrokenPilot remediation backlog examples.
- Mirrored worked examples into the MkDocs website content.

### Changed

- Updated Module 07 memory poisoning validation to document defense-in-depth behavior observed during local testing: memory poisoning can influence an attempted action, while independent tool authorization can still block the unsafe cross-tenant tool call.
- Updated MkDocs navigation for the expanded BrokenPilot worked examples.

## v1.1-dev  -  BrokenPilot test isolation fix

- Added pytest test isolation for BrokenPilot control environment variables.
- Documented how to reset PowerShell control toggles after manual validation.
- This fixes test failures where a previous manual `$env:ENABLE_TOOL_AUTHZ="true"` session caused vulnerable-default tests to run in hardened mode.


## v1.1-dev  -  BrokenPilot prototype design

Added a design package for the first minimal runnable BrokenPilot prototype. This is not a release tag and not the final implementation. It defines the MVP architecture, API contract, fake data plan, mock LLM mode, vulnerability implementation plan, control toggles, Docker Compose plan, student lab flow, instructor runbook, safety notes, and build backlog.

Added files under:

- `labs/brokenpilot/prototype/`
- `docs/labs/brokenpilot/prototype/`

This work moves the capstone from a paper-only design toward a runnable local target.


## Unreleased  -  v1.1-dev DVAIA validation

### Added

- Recorded DVAIA local validation baseline for Windows / PowerShell.
- Added DVAIA validated lab results summary.
- Added DVAIA walkthrough authoring plan.

### Changed

- Updated DVAIA validation and module mapping pages from planned/TODO status to locally validated status.
- Updated the quality improvement plan to reflect DVAIA validation completion and make BrokenPilot prototype the next major testability gap.


## v1.1.0  -  Website edition draft

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

## v1.0.0-rc2  -  Review cleanup

### Fixed

- Removed incremental build-status notes from `README.md`, `syllabus.md`, and `course-map.md`.
- Updated Module 01 NIST adversarial ML reference from the old e2023 draft to NIST AI 100-2 E2025.
- Updated OWASP LLM02:2025 Sensitive Information Disclosure links to the current OWASP GenAI page.
- Updated Module 05 OWASP LLM framing to 2025 numbering and added an explicit note about 2023/2024 renumbering.
- Added missing primary URLs to Module 08 Secure MLOps references.
- Clarified that OWASP Agentic Skills Top 10 is supplementary to the Agentic Applications Top 10 risk framing.

## v1.0.0-rc  -  Release candidate

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

## v0.14  -  Module 12 complete

### Added

- Full BrokenPilot capstone teaching package.
- Capstone slides, instructor notes, handout, exercises, checklist, quiz, and references.
- Final presentation, evidence log, remediation backlog, risk register, and grading material.

## v0.13  -  Module 11 complete

### Added

- AI Red Team Methodology module.
- Red team scoping tabletop.
- BrokenPilot attack-chain lab.
- Red team scope, attack plan, report, and executive readout templates.

## v0.12  -  Module 10 complete

### Added

- Adversarial ML and Robustness module.
- Evasion and robustness lab.
- Poisoning and backdoor tabletop.
- Adversarial test plan and robustness evaluation templates.

## v0.11  -  Module 9 complete

### Added

- Privacy Attacks and Data Protection module.
- Cross-tenant RAG privacy lab.
- Membership inference and model inversion tabletop.
- Privacy risk and retention review templates.

## v0.10  -  Module 8 complete

### Added

- Secure MLOps and AI Supply Chain module.
- Broken ML pipeline lab.
- Model artifact provenance lab.
- ML-BOM and supply chain templates.

## v0.9  -  BrokenPilot paper design

### Added

- BrokenPilot scenario, architecture, roles, data model, tools, vulnerabilities, attack paths, secure reference architecture, and instructor solution.

## v0.8  -  Module 7 complete

### Added

- Agent and Tool Security module.
- Tool misuse lab.
- Memory poisoning and approval-gates lab.
- Agent control design templates.

## v0.7  -  Module 6 complete

### Added

- RAG Security and Indirect Prompt Injection module.
- RAG lab wrapper.
- RAG and vector database templates.

## v0.6  -  Module 5 complete

### Added

- LLM Application Security module.
- DVAIA-style LLM lab guide.
- LLM security review template.

## v0.5  -  Module 4 complete

### Added

- BIML Architectural Risk Analysis module.
- Architecture review lab and template.

## v0.4  -  Module 3 complete

### Added

- OWASP ML Security Top 10 module.
- Classical ML attack lab wrapper.

## v0.3  -  Module 2 complete

### Added

- ML System Architecture module.
- ML lifecycle DFD exercise.

## v0.2  -  Module 1 complete

### Added

- Security Engineering for AI module.
- Reference module structure.
- Reusable module template.

## v0.1  -  Curriculum skeleton

### Added

- Initial repository skeleton.
- Syllabus.
- Course map.
- Reference list.
- Initial templates and lab strategy.
## v1.1-dev  -  DVAIA validated walkthroughs

Added validated DVAIA-backed walkthroughs for Module 05 direct prompt injection, Module 06 indirect prompt injection/RAG trust boundaries, Module 07 agent/tool behavior, and Module 11 mini red-team assessment. Added a reusable DVAIA evidence log template and updated DVAIA lab guide navigation.


## v1.1-dev  -  BrokenPilot runnable MVP

Added the first minimal runnable BrokenPilot prototype.

Implemented:

- FastAPI local application
- static browser UI
- fake users, documents, and tickets
- keyword retrieval
- deterministic mock LLM behavior
- vulnerable default mode
- retrieval authorization control toggle
- prompt-injection filtering control toggle
- Dockerfile and Docker Compose
- pytest smoke tests
- lab guide for cross-document authorization and indirect prompt injection

This is not a full BrokenPilot implementation yet. It is the first testable MVP for turning the capstone from a paper-only exercise into a runnable local assessment target.

## Module 07 validation consolidation

- Moved the BrokenPilot tool authorization validation record into Module 07 to avoid duplicate validation documentation.
- Added a Module 07 validation page for the cross-tenant tool confused-deputy scenario.
- Linked the validated scenario from the Module 07 overview, exercise, instructor notes, and MkDocs navigation.

## Memory poisoning MVP increment

- Added BrokenPilot memory endpoints and deterministic memory-poisoning behavior.
- Added Module 07 memory validation material.
- Added prototype memory poisoning lab guide.
- Added tests for vulnerable and controlled memory behavior.

## v1.1-dev  -  Instructor grading calibration

Added an instructor grading calibration guide and grading calibration exercise. These materials use the BrokenPilot strong/weak worked examples to align scoring around threat models, evidence quality, implementable controls, remediation backlog quality, executive communication, and residual risk.


## v1.1-dev  -  Module 06 RAG Security deepening

Added reading-first deepening material for Module 06:

- RAG security deep dive
- RAG attack anatomy
- Controls and remediations
- Common mistakes
- Worked example for a RAG incident assistant

This strengthens the course goal that labs reinforce security reasoning rather than replace explanation.


## Module 07 deepening

- Deepened Module 07 with reading-first pages for agent/tool security, including attack anatomy, controls, common mistakes, and a BrokenPilot worked example.

## v1.1-dev  -  Executive communication exercise

- Added Module 08 executive risk memo exercise.
- Added executive risk memo template, rubric, instructor guide, and strong/weak examples.
- Linked executive communication practice to Module 07, Module 08, Module 11, and BrokenPilot.

## Unreleased  -  Finding rewrite classroom exercise

Added a classroom exercise that teaches students to rewrite vague AI security observations into decision-grade findings. Added a finding rewrite template, finding quality rubric, instructor facilitation guide, and BrokenPilot before/after example.

<!-- v1.1-dev-lab-improvement-part3-toy-classifier -->

## v1.1-dev: Toy-classifier observable ML attack lab

- Added a deterministic toy-classifier app for Modules 03 and 10.
- Added runnable evasion, poisoning, extraction, and output-integrity scripts.
- Added pytest coverage for all four attack demonstrations.
- Updated the toy ML and adversarial evasion labs to point to shipped data and scripts.
