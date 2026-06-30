# Project Backlog

This backlog tracks the build plan for **AI Training — ML Security**.

## Current release status

**Current version:** v1.1 development branch  
**Core curriculum:** complete  
**Modules:** 01–12 complete  
**Capstone:** BrokenPilot paper-based capstone complete  
**Repository readiness:** v1.0.x released; v1.1 development is focused on testable labs, website usability, and course depth

## v1.0 release checklist

The following items should be verified before tagging `v1.0.0`:

- [ ] Review `README.md` for stale status text.
- [ ] Review `syllabus.md` for consistency with all twelve modules.
- [ ] Review `course-map.md` for correct module/lab/template links.
- [ ] Review `references.md` and remove duplicated or low-quality sources.
- [ ] Confirm every module has:
  - [ ] `README.md`
  - [ ] `slides.md`
  - [ ] `instructor-notes.md`
  - [ ] `student-handout.md`
  - [ ] exercise file
  - [ ] `checklist.md`
  - [ ] `quiz.md`
  - [ ] `references.md`
- [ ] Confirm lab guides use fake/local data only.
- [ ] Confirm no third-party copyrighted lab content was copied into the repository.
- [ ] Confirm license strategy is acceptable before making the repo public.
- [ ] Confirm GitHub issue templates and PR template render correctly.
- [ ] Create a GitHub release using `docs/releases/v1.0.0.md` as the release notes.

## Completed milestones

### v0.1 — Curriculum spine

- [x] Course identity
- [x] Syllabus
- [x] Course map
- [x] Reference list
- [x] Module folder structure
- [x] Lab strategy
- [x] Initial templates

### v0.2 — Module 1 complete

- [x] Module 1 README
- [x] Slides
- [x] Instructor notes
- [x] Student handout
- [x] Threat modeling exercise
- [x] Checklist
- [x] Quiz
- [x] References

### v0.3 — Module 2 complete

- [x] ML lifecycle architecture
- [x] ML system data-flow exercise
- [x] ML architecture review template

### v0.4 — Module 3 complete

- [x] OWASP ML Security Top 10 module
- [x] Classical ML attack lab wrapper
- [x] ML attack summary template

### v0.5 — Module 4 complete

- [x] BIML architectural risk analysis module
- [x] Architecture review lab
- [x] Architecture risk review template

### v0.6 — Module 5 complete

- [x] LLM application security module
- [x] DVAIA-style LLM application security lab
- [x] LLM application security review template

### v0.7 — Module 6 complete

- [x] RAG security module
- [x] Indirect prompt injection lab
- [x] RAG threat model template
- [x] Vector database authorization checklist

### v0.8 — Module 7 complete

- [x] Agent and tool security module
- [x] Tool misuse lab
- [x] Memory poisoning and approval-gates lab
- [x] Agent control design templates

### v0.9 — BrokenPilot paper design complete

- [x] Scenario
- [x] Architecture
- [x] Roles
- [x] Data model
- [x] Tools
- [x] Vulnerabilities
- [x] Attack paths
- [x] Instructor solution
- [x] Secure reference architecture
- [x] Grading rubric

### v0.10 — Module 8 complete

- [x] Secure MLOps and AI supply chain module
- [x] Broken ML pipeline lab
- [x] Model artifact provenance lab
- [x] ML-BOM and provenance templates

### v0.11 — Module 9 complete

- [x] Privacy attacks and data protection module
- [x] Cross-tenant RAG privacy lab
- [x] Membership inference and model inversion tabletop
- [x] Privacy templates

### v0.12 — Module 10 complete

- [x] Adversarial ML and robustness module
- [x] Evasion and robustness lab
- [x] Poisoning and backdoor tabletop
- [x] Robustness evaluation templates

### v0.13 — Module 11 complete

- [x] AI red team methodology module
- [x] AI red team scoping tabletop
- [x] BrokenPilot attack-chain lab
- [x] AI red team templates

### v0.14 — Module 12 complete

- [x] BrokenPilot capstone teaching package
- [x] Capstone slides
- [x] Instructor notes
- [x] Student handout
- [x] Capstone exercises
- [x] Evidence, risk, and remediation templates
- [x] Final grading rubric

### v1.0-rc — Release readiness

- [x] `CHANGELOG.md`
- [x] `RELEASE_CHECKLIST.md`
- [x] `VERSION.md`
- [x] `ROADMAP.md`
- [x] `SECURITY.md`
- [x] `CODE_OF_CONDUCT.md`
- [x] `docs/releases/v1.0.0.md`
- [x] GitHub issue templates
- [x] Pull request template

## Post-v1.0 backlog

### Lab validation

- [x] Install DVAIA locally.
- [x] Verify which DVAIA labs are stable and useful for this course.
- [x] Add DVAIA validation baseline.
- [x] Add module-to-DVAIA mapping.
- [x] Add initial validated walkthroughs for Modules 05, 06, 07, and 11.
- [x] Add DVAIA evidence log template.
- [ ] Add exact screenshots or transcripts from an instructor run.
- [ ] Add exact panel names where DVAIA UI is stable.
- [ ] Add lab setup notes for macOS and Linux.
- [ ] Mark labs as beginner, intermediate, or advanced.

### BrokenPilot implementation

- [ ] Build minimal local web app.
- [ ] Add fake users, fake tickets, fake docs, and fake configuration data.
- [ ] Add intentionally vulnerable RAG workflow.
- [ ] Add intentionally overprivileged tools.
- [ ] Add memory poisoning scenario.
- [ ] Add secure mode for comparison.
- [ ] Add Docker Compose.
- [ ] Add instructor reset scripts.

### Quality improvements

- [ ] Add diagrams as Mermaid where useful.
- [ ] Add optional slide export workflow.
- [ ] Add facilitator timing for half-day, one-day, two-day, and twelve-week formats.
- [ ] Add more quizzes to `assessments/quiz-bank.md`.
- [ ] Add sample completed student deliverables.
- [ ] Add an executive briefing version of the course.

### Community readiness

- [ ] Decide whether repo stays private or becomes public.
- [ ] Verify final license text.
- [ ] Add maintainers file if public.
- [ ] Add contribution labels.
- [ ] Add first GitHub release.

### v1.2-dev — BrokenPilot prototype design

- [x] Minimal runnable prototype goals
- [x] MVP architecture and trust boundaries
- [x] API contract
- [x] Fake data plan
- [x] Deterministic mock LLM mode
- [x] Vulnerability implementation plan
- [x] Control toggle plan
- [x] Docker Compose plan
- [x] Student lab flow
- [x] Instructor runbook
- [x] Safety notes
- [x] Prototype build backlog

Next implementation target:

- [ ] Create FastAPI skeleton
- [ ] Add fake data fixtures
- [ ] Add `/health`, `/users`, `/retrieve`, and `/chat`
- [ ] Add mock LLM provider
- [ ] Add first vulnerable indirect prompt injection path



## BrokenPilot prototype implementation status

The first minimal runnable BrokenPilot prototype has been implemented under:

```text
labs/brokenpilot/prototype-app/
```

Implemented:

- FastAPI app
- static local UI
- fake users/documents/tickets
- keyword retrieval
- deterministic mock LLM
- vulnerable default mode
- retrieval authorization toggle
- prompt-injection filtering toggle
- Dockerfile and Docker Compose
- pytest smoke tests

Next implementation increments:

1. Add tool-calling endpoint and confused-deputy tool misuse scenario.
2. Add memory endpoint and memory-poisoning scenario.
3. Add persistent audit log export.
4. Add challenge mode with controls partially enabled.
5. Add instructor solution scripts.


## BrokenPilot tool-calling increment

The runnable BrokenPilot prototype now includes a deterministic tool-calling scenario for Module 07 and the capstone. It demonstrates a confused-deputy failure through `/tools/update-ticket` and `/agent/run`, plus control toggles for tool authorization and approval gates.

## Module 07 validation consolidation

- Moved the BrokenPilot tool authorization validation record into Module 07 to avoid duplicate validation documentation.
- Added a Module 07 validation page for the cross-tenant tool confused-deputy scenario.
- Linked the validated scenario from the Module 07 overview, exercise, instructor notes, and MkDocs navigation.

## Memory poisoning MVP increment

- Added BrokenPilot memory endpoints and deterministic memory-poisoning behavior.
- Added Module 07 memory validation material.
- Added prototype memory poisoning lab guide.
- Added tests for vulnerable and controlled memory behavior.

## BrokenPilot worked examples expansion

Completed:

- [x] Add strong and weak tool permission matrix examples
- [x] Add strong and weak evidence log examples
- [x] Add strong and weak remediation backlog examples
- [x] Mirror examples into MkDocs website content
- [x] Add examples to MkDocs navigation

Next:

- [x] Add instructor grading calibration guide using the worked examples
- [ ] Add one complete sample final report assembled from the strong examples


## Next capstone quality improvements

- [ ] Add assembled sample BrokenPilot final report using the strong examples.
- [ ] Add instructor demo script for BrokenPilot prototype.
- [ ] Add grading calibration checklist to capstone runbook.

## Content depth backlog

- Add `deep-dive.md` to Module 05.
- Add `attack-anatomy.md` to Module 06.
- Add `controls-and-remediations.md` to Module 07.
- Add additional worked examples to Module 10.
- Add a gold-standard BrokenPilot final report.
- Review each module against the reading-first content standard.

## Module 05 reading-first depth completed

Module 05 now includes deep-dive, attack anatomy, controls/remediations, common mistakes, and a worked example. This is the first module upgraded to the reading-first, lab-supported content standard.


## Module 06 deepening

- [x] Add RAG deep dive
- [x] Add attack anatomy
- [x] Add controls and remediations
- [x] Add common mistakes
- [x] Add worked example


## Module 07 deepening

- Completed Module 07 deepening package. Next deepening target: Module 10 adversarial ML intuition and worked examples, or Module 12 BrokenPilot final report sample.
