# Final Content Audit Before Release Cleanup

This document is a content-readiness audit for the v1.1 development line. It is intentionally separate from MkDocs, CI, and repository cleanup. Those tasks come after the course content and lab path stop moving.

## Current judgment

The course now has a credible 40-hour professional-training spine. The most important improvement is that the course no longer depends only on reading and tabletop reasoning. It now has three appropriate lab substrates:

| Modality | Target | Used for |
|---|---|---|
| LLM, RAG, agent, tool, memory, privacy, red-team flows | BrokenPilot | Modules 05, 06, 07, 09, 11, 12 |
| Classical ML attack behavior | toy-classifier app | Modules 03 and 10 |
| MLOps and supply-chain review | static evidence pack | Module 08 |

This is the right shape. BrokenPilot should not be forced to teach classical ML evasion or poisoning, and the toy classifier should not be forced to teach agent authorization. Each target now has a teaching job that matches its modality.

## Content-complete criteria

The course should be considered content-complete when the following statements are true.

1. Every module has a clear reading path, a lab or reasoning path, and a graded artifact.
2. Every attack lab has an observable failure and an observable fix or control comparison.
3. Every reasoning lab ends in a concrete review artifact, not only discussion.
4. Every major lab has a strong example, a weak example, or a model answer.
5. The capstone final report uses the current evidence path, not the older paper-only BrokenPilot design.
6. The 40-hour course can be taught without inventing major transitions during class.
7. The release does not overclaim what each lab can demonstrate.

## Module-by-module readiness

| Module | Current path | Readiness | Remaining content work |
|---|---|---|---|
| 01 Security Engineering for AI | Reading and reasoning deliverable | Strong | Final voice pass only |
| 02 ML System Architecture | Architecture review deliverable | Strong | Final voice pass only |
| 03 OWASP ML Top 10 | toy-classifier plus taxonomy mapping | Strong | Confirm instructor guide and debrief are applied |
| 04 BIML Architectural Risk Analysis | DocOps architecture review | Strong | Confirm strong/weak anchors are visible |
| 05 LLM Application Security | BrokenPilot direct injection and output handling | Strong | Confirm current capstone report references both |
| 06 RAG Security | BrokenPilot retrieval and indirect injection path | Strong | Consolidate old paper-only RAG lab language during cleanup |
| 07 Agent and Tool Security | BrokenPilot tool auth, approval, memory | Reference standard | Keep central, do not dilute |
| 08 Secure MLOps and Supply Chain | evidence-pack review | Strong | Confirm model answer package is applied |
| 09 Privacy Attacks and Data Protection | BrokenPilot cross-tenant leakage plus reasoning labs | Strong | Add explicit logging-still-leaks debrief if not already present |
| 10 Adversarial ML and Robustness | toy-classifier and reasoning tabletop | Strong | Keep hard-gate decision framing central |
| 11 AI Red Team Methodology | BrokenPilot attack-chain and scoping tabletop | Strong | Confirm current capstone evidence map is applied |
| 12 BrokenPilot Capstone | final report and presentation | Strong if current report package is applied | Confirm latest final report package is applied |

## Remaining content tasks before cleanup

### P1: apply and verify current capstone assets

The capstone must reflect the current BrokenPilot evidence path:

- direct user-message prompt injection
- insecure output handling
- cross-tenant privacy leakage
- retrieval authorization
- tool confused-deputy behavior
- tool authorization control
- memory poisoning
- defense in depth where memory can steer intent but tool authorization blocks execution

If the current final report package has not been applied, apply it before release cleanup.

### P1: verify instructor debrief coverage

The following debriefs should exist before cleanup:

- BrokenPilot capstone debrief
- toy-classifier debrief
- MLOps evidence-pack debrief
- reasoning-lab grading anchors

The goal is that a second instructor can run the course without reverse-engineering the author's intent from the exercises.

### P2: final 40-hour dry run

Before release cleanup, do a paper dry run using `COURSE_DRY_RUN_PLAN_40H.md`. The dry run should answer:

- Where do students get stuck?
- Which labs take longer than expected?
- Which readings are essential and which are optional?
- Which deliverables need clearer grading anchors?
- Which old pages duplicate the current lab route?

### P2: final voice and cohesion pass

The course should read like a coherent program, not a pile of generated modules. The final voice pass should remove:

- repetitive section formulas that add no teaching value
- inflated phrasing
- placeholder-like language
- repeated claims that a lab is important without saying what decision it teaches
- duplicated old lab paths that conflict with the current route

## What not to do before cleanup

Do not fight strict MkDocs yet. Do not tune CI for release while content is still moving. Do not remove apply scripts until all packages have been applied and committed. Do not flatten the course by trying to make every module runnable. Some modules are better as design review or evidence review exercises.

## Release-readiness signal

The course is ready for cleanup when the only remaining work is:

- navigation
- CI
- generated-script removal
- naming consistency
- stale file removal
- style cleanup
- final release notes

If a remaining task changes what students study, run, submit, or are graded on, it is still content work, not cleanup.
