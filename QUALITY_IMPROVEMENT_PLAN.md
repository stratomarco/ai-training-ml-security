# Quality Improvement Plan

This document merges the post-v1.0 improvement direction into a practical development plan. The goal is not to create another release immediately. The goal is to move from a complete curriculum to a testable, instructor-friendly, hands-on learning experience.

## Current honest state

The v1.0 course is structurally complete. It has 12 modules, lab guides, templates, assessments, references, and the BrokenPilot capstone. The strongest part is the coherent security engineering message and the BrokenPilot capstone design.

The main limitation is testability. Much of the course is still paper-based. DVAIA has now been locally validated as an external lab dependency, which removes the first major uncertainty. BrokenPilot is still a design capstone but not yet a runnable target. That is now the highest-priority testability gap.

## North star

Students should be able to:

1. Learn the concept.
2. See the architecture.
3. Trigger or simulate the failure mode.
4. Explain the root cause.
5. Produce a concrete control.
6. Communicate the risk clearly.
7. Repeat the process in the capstone.

## Priority order

### 1. Validate external hands-on labs

Status: **Completed initial local validation.**

DVAIA has been installed and validated locally on Windows / PowerShell using Docker and local mode. Initial per-lab walkthroughs have now been added for Modules 05, 06, 07, and 11. The remaining refinement is to add exact screenshots or transcripts from an instructor run, plus any panel-specific troubleshooting notes.

This remains high leverage because it changes selected labs from mostly descriptive to demonstrable.

### 2. Build a minimal BrokenPilot prototype

The first prototype does not need to be production-like. It should be intentionally small and intentionally vulnerable.

Minimum target:

- FastAPI backend
- Static or simple web UI
- Fake users and roles
- Fake tickets
- Fake internal documents
- Simple retrieval layer
- Tool endpoints
- Vulnerable policy design
- Instructor reset script

The goal is to create a runnable capstone target, not a polished product.

### 3. Add worked student examples

BrokenPilot needs examples of strong and weak submissions so instructors grade consistently.

Start with:

- Strong threat model
- Weak threat model
- Strong risk register
- Weak risk register
- Strong executive readout
- Weak executive readout

### 4. Add delivery format guidance

The course should support different delivery models:

- 2-hour lunch-and-learn
- Half-day workshop
- 1-day workshop
- 2-day intensive
- 12-week course

Each format needs guidance on what to cut, what to keep, and what to assign as homework.

### 5. Require students to produce concrete controls

The assessment model should reward fixing, not only finding. Add exercises where students must produce implementable controls:

- Tool permission matrix
- Retrieval authorization rule set
- Approval policy
- Logging and retention policy
- Risk memo to leadership

### 6. Deepen Module 10

Module 10 needs more worked examples because adversarial ML can otherwise feel abstract. Add examples that do not require a running lab:

- Feature-space evasion against a fraud classifier
- Text perturbation against a phishing classifier
- Backdoor trigger in a text classifier
- Poisoned feedback loop
- Drift and fallback design

## Development milestones

### v1.1-dev — Testable labs foundation

- DVAIA validation plan — done
- DVAIA setup checklist — done
- Module-to-DVAIA mapping — done
- Lab validation matrix — initial validation done
- Instructor troubleshooting notes — partial, needs per-lab refinement
- Per-lab DVAIA walkthroughs — initial set done for Modules 05, 06, 07, and 11
- DVAIA evidence log template — done
- Screenshot/transcript capture — next refinement

### v1.2-dev — BrokenPilot prototype design

Status: **Initial design package complete.**

- Prototype architecture — done
- API contract — done
- Fake data model — done
- Mock LLM mode — done
- Vulnerability implementation plan — done
- Control toggle plan — done
- Safe local deployment plan — done
- Student lab flow — done
- Instructor runbook — done
- Build backlog — done

Next step: implement the smallest FastAPI skeleton that can start locally, load fake data, and expose `/health`, `/users`, `/retrieve`, and `/chat`.

### v1.3-dev — Worked examples and grading anchors

- Strong and weak capstone examples
- Rubric calibration notes
- Example evidence log
- Example remediation backlog

### v1.4-dev — Delivery model

- 2-hour path
- Half-day path
- 1-day path
- 2-day path
- 12-week path
- Module-level cut/expand notes

### v1.5-dev — Concrete controls and executive communication

- Control implementation exercises
- CISO memo exercise
- Policy examples
- Retrieval authorization examples
- Tool permission examples

### v1.6-dev — Module 10 deepening

- Deep-dive worked examples
- New diagrams
- Tabletop exercises
- Adversarial robustness assessment improvements

## Non-goals for the next phase

- Do not tag a new public release yet.
- Do not over-polish the website before the labs are testable.
- Do not copy DVAIA code into this repository.
- Do not build a complex BrokenPilot app before the minimal prototype is defined.
- Do not turn the course into jailbreak theater.

## Working branch recommendation

Use a development branch:

```bash
git checkout -b website-dev
```

or:

```bash
git checkout -b v1.1-dev-testable-labs
```

Merge to `main` only after the website builds and the new documentation is internally consistent.


## BrokenPilot minimal runnable prototype — first MVP implemented

The first BrokenPilot runnable MVP now exists under:

```text
labs/brokenpilot/prototype-app/
```

This closes the initial gap between the paper capstone and a runnable assessment target. The MVP is intentionally small: it validates the architecture and teaching flow before adding tools, memory, vector databases, or real model providers.

Current MVP coverage:

- retrieval authorization failure
- indirect prompt injection through retrieved content
- deterministic vulnerable/controlled behavior
- local UI and API
- Docker support
- pytest smoke tests

Remaining prototype work:

- tool confused-deputy scenario
- memory poisoning scenario
- stronger audit evidence workflow
- instructor demo scripts
- optional vector database mode


## BrokenPilot tool-calling increment

The runnable BrokenPilot prototype now includes a deterministic tool-calling scenario for Module 07 and the capstone. It demonstrates a confused-deputy failure through `/tools/update-ticket` and `/agent/run`, plus control toggles for tool authorization and approval gates.

## Module 07 validation consolidation

- Moved the BrokenPilot tool authorization validation record into Module 07 to avoid duplicate validation documentation.
- Added a Module 07 validation page for the cross-tenant tool confused-deputy scenario.
- Linked the validated scenario from the Module 07 overview, exercise, instructor notes, and MkDocs navigation.
