# 40-Hour Delivery Plan

This is the recommended instructor-led format for **AI Training — ML Security**.

The course should be designed as a **one-week, 40-hour professional training** rather than a 12-week academic course. The goal is to provide enough depth for students to understand the security engineering behind ML, LLM, RAG, and agent systems while still leaving meaningful time for hands-on labs, concrete controls, and BrokenPilot capstone work.

## Positioning

This is not a five-day prompt-hacking workshop.

It is a security engineering course for systems that contain machine learning.

Students should leave with the ability to:

- explain the attack class,
- identify the violated security property,
- reproduce selected attacks in controlled labs,
- design implementable controls,
- validate those controls,
- write decision-grade findings,
- communicate residual risk to technical and executive audiences.

## Recommended format

| Format | Recommendation |
|---|---|
| Duration | 5 days |
| Total time | 40 hours |
| Daily time | 8 hours including breaks |
| Delivery mode | Instructor-led, hands-on |
| Lab mode | Local laptop, DVAIA, BrokenPilot |
| Capstone | BrokenPilot final assessment |
| Assessment | Evidence log, risk memo, finding rewrite, final report |

## Time allocation model

The live course should balance reading, explanation, discussion, and doing.

| Activity type | Approximate time | Purpose |
|---|---:|---|
| Instructor explanation | 14 hours | Concepts, architecture, attack anatomy, controls |
| Guided labs | 10 hours | DVAIA and BrokenPilot validation |
| Exercises and templates | 6 hours | Threat models, permission matrices, risk memos, findings |
| Capstone work | 7 hours | BrokenPilot assessment and final report |
| Review and discussion | 3 hours | Debrief, executive readouts, remediation choices |

The instructor should not attempt to read every page aloud. The deep-dive material is used for pre-reading, in-class reference, and post-course study.

## What is in scope for 40 hours

The 40-hour course should cover all 12 modules, but not with equal depth.

| Module | Live-course treatment |
|---|---|
| 01 — Security Engineering for AI | Core foundation |
| 02 — ML System Architecture | Core foundation |
| 03 — OWASP ML Security Top 10 | Survey with selected examples |
| 04 — BIML Architectural Risk Analysis | Architecture review lens |
| 05 — LLM Application Security | Deep coverage + DVAIA lab |
| 06 — RAG Security | Deep coverage + DVAIA/BrokenPilot lab |
| 07 — Agent and Tool Security | Deep coverage + BrokenPilot lab |
| 08 — Secure MLOps and AI Supply Chain | Deep coverage + executive memo |
| 09 — Privacy Attacks | Focused coverage |
| 10 — Adversarial ML and Robustness | Focused coverage with worked examples |
| 11 — AI Red Team Methodology | Deep coverage for reporting and evidence |
| 12 — BrokenPilot Capstone | Final assessment |

## What moves to self-study

Some material should be assigned as pre-reading or post-reading rather than delivered live.

Suggested self-study material:

- full reference reading list,
- optional quizzes for every module,
- advanced adversarial ML math,
- extended supply-chain standards reading,
- optional BrokenPilot implementation notes,
- optional DVAIA exploration beyond the validated walkthroughs.

## Five-day structure

| Day | Theme | Core modules | Main outcome |
|---|---|---|---|
| Day 1 | Foundations and ML architecture | 01, 02, 03, 04 | Students can reason about AI systems as security systems |
| Day 2 | LLM and RAG application security | 05, 06 | Students can explain and test prompt injection and RAG trust failures |
| Day 3 | Agent security and AI supply chain | 07, 08 | Students can validate tool controls and reason about MLOps supply-chain risk |
| Day 4 | Privacy, adversarial ML, and red team reporting | 09, 10, 11 | Students can test, report, and communicate AI security findings |
| Day 5 | BrokenPilot capstone | 12 | Students produce and present a final security assessment |

## Daily pacing principles

Each day should include:

1. concept explanation,
2. attack anatomy,
3. security principle mapping,
4. lab or tabletop exercise,
5. control/remediation discussion,
6. evidence or report artifact.

Avoid days that are all lecture or all lab.

## Minimum viable 40-hour course

If time gets tight, protect these elements:

- Module 01: the model is not the security boundary.
- Module 05: prompt injection is an architectural control-boundary issue.
- Module 06: retrieved content is untrusted input.
- Module 07: tools must enforce authorization outside the model.
- Module 08: models, datasets, prompts, and vector indexes are supply-chain artifacts.
- Module 11: evidence and remediation matter more than jailbreak screenshots.
- Module 12: BrokenPilot capstone.

Cut or compress:

- long standard-by-standard comparisons,
- extended literature discussion,
- optional quizzes,
- secondary labs,
- long tool demos that do not support a security decision.

## Instructor preparation checklist

Before delivery, validate:

- [ ] MkDocs site runs locally.
- [ ] DVAIA starts locally.
- [ ] DVAIA walkthroughs are reachable and current.
- [ ] BrokenPilot starts locally.
- [ ] BrokenPilot tests pass.
- [ ] BrokenPilot tool authorization scenario works.
- [ ] BrokenPilot memory poisoning scenario works.
- [ ] Student handouts are available.
- [ ] Templates are available.
- [ ] Capstone instructions are clear.
- [ ] Final report examples are reviewed.

## Student preparation checklist

Students should have:

- a laptop with Docker available,
- Python available,
- Git available,
- browser access to the course website,
- local access to DVAIA if participating in hands-on labs,
- local access to BrokenPilot for capstone work.

## Teaching stance

Instructors should constantly connect lab behavior back to engineering decisions.

For every finding, ask:

- What security property failed?
- What authority boundary was crossed?
- What control should enforce the boundary?
- How would an engineer implement the control?
- How would we test the fix?
- What residual risk remains?
- How would we explain this to leadership?
