from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()


def ensure_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def write(path: str, content: str) -> None:
    target = ROOT / path
    ensure_dir(target)
    target.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path}")


def append_once(path: str, marker: str, section: str) -> None:
    target = ROOT / path
    ensure_dir(target)
    if target.exists():
        text = target.read_text(encoding="utf-8")
    else:
        text = f"# {target.stem.replace('-', ' ').title()}\n"
    if marker in text:
        print(f"already updated: {path}")
        return
    target.write_text(text.rstrip() + "\n\n" + section.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"updated: {path}")


COURSE_FLOW_REVIEW = r'''
# Course Flow Review and Completion Plan

Status: v1.1-dev content and lab readiness pass.

Purpose: make the course coherent as a 40-hour professional training before final release cleanup. This file is not a release checklist. It is a course-quality map that answers three questions:

1. Does the course have a clear learning journey?
2. Do labs and assessments match the learning goals?
3. What remains thin before the final cleanup phase?

## Completion decision

The course is close to content-complete for a one-week professional format, but it is not yet release-complete. The remaining work should focus on coherence, anchors, and integration rather than adding more isolated pages.

Content readiness today:

| Area | Readiness | Decision |
|---|---:|---|
| Module structure | High | Keep the 12-module model. Do not add more modules. |
| BrokenPilot runnable path | High | Use as the main LLM, RAG, agent, privacy, and red-team target. |
| Toy classifier path | Medium-high | Use for OWASP ML and adversarial ML. Add teaching anchors after first classroom dry run. |
| MLOps supply-chain path | Medium-high | Keep as evidence-pack review, not a runnable fake pipeline. |
| Reasoning labs | Medium-high | Strong, but need a final anchor consistency pass. |
| Assessment flow | Medium-high | Daily checkpoints and capstone checkpoints now exist. Validate against the full 40-hour path. |
| Website and CI | Deferred | Clean after content freezes. |
| Release polish | Deferred | Remove temporary scripts and generated-looking scaffolding at the end. |

## Course story

The course should read as one argument:

> ML security is security engineering for systems that contain models. The model changes the failure modes, but it does not remove the need for boundaries, authorization, provenance, validation, monitoring, and residual-risk decisions.

Every module should reinforce that argument from a different angle:

| Module | Role in the story | What the student must learn to decide |
|---|---|---|
| 01 Security Engineering for AI | Establish the security-engineering lens | Where should the system enforce boundaries instead of trusting model behavior? |
| 02 ML System Architecture | Turn the system into a reviewable map | Where do data, authority, artifacts, logs, and outputs cross trust boundaries? |
| 03 OWASP ML Top 10 | Build a shared risk taxonomy | Which risk category explains the observed behavior, and what evidence proves it? |
| 04 BIML Architectural Risk Analysis | Move from taxonomy to design review | Which assumptions are unsafe before implementation begins? |
| 05 LLM Application Security | Show instruction/data confusion and output-sink risk | What text is untrusted, and what downstream component must not trust model output? |
| 06 RAG Security | Make retrieval a security boundary | Who is allowed to retrieve, summarize, log, and cite each document? |
| 07 Agent and Tool Security | Separate intent from execution | Which component authorizes the action, target object, and approval step? |
| 08 Secure MLOps and AI Supply Chain | Treat model artifacts as software supply-chain assets | Can this artifact be promoted, reproduced, rolled back, and trusted? |
| 09 Privacy Attacks and Data Protection | Protect information from disclosure, inference, reconstruction, and logging | What information must never cross this boundary, even indirectly? |
| 10 Adversarial ML and Robustness | Avoid overtrusting model accuracy | Is the model safe as a hard gate, or does it require fallback and monitoring? |
| 11 AI Red Team Methodology | Turn testing into decision evidence | What evidence would change launch, scope, controls, or monitoring? |
| 12 BrokenPilot Capstone | Integrate the whole course | Can the student produce evidence, controls, validation, and residual-risk decisions? |

## Thin areas to resolve before final release

These are not all equally urgent. The first four affect the learning experience most.

### 1. Capstone synthesis still needs a full final dry run

BrokenPilot is now strong, but the complete student journey should be tested end to end:

- start from the student brief;
- collect evidence from at least three attack paths;
- write a finding;
- propose controls;
- validate one control;
- write residual risk;
- prepare a short executive readout.

Completion criterion: one complete worked student submission exists that uses the current lab paths, not older paper-only assumptions.

### 2. Toy classifier needs instructor-facing explanation

The toy classifier makes Modules 03 and 10 observable, but instructors need a short guide explaining what not to overclaim:

- it is synthetic;
- it demonstrates failure modes, not real-world attack capability;
- it should be framed around decision risk, not clever bypasses;
- the main decision is whether a classifier should be a hard authorization gate.

Completion criterion: instructor notes exist for toy-classifier facilitation and debrief.

### 3. MLOps evidence pack needs a complete model answer

The evidence pack is useful only if instructors can calibrate what good looks like. The strong/weak examples help, but a complete evidence-pack review answer should show:

- findings;
- evidence references;
- promotion decision;
- required controls;
- validation plan;
- residual risk;
- executive recommendation.

Completion criterion: one complete model answer exists for the MLOps evidence-pack lab.

### 4. Reasoning labs need final anchor consistency

Reasoning labs should all end in a concrete artifact. The final check should confirm every reasoning lab has:

- a deliverable template or clear expected artifact;
- a strong example or anchor;
- a weak example or anti-pattern;
- a grading rubric or connection to a shared rubric;
- a residual-risk section.

Completion criterion: the reasoning-lab anchor matrix has no missing critical cells.

### 5. Module intros should be made less repetitive

Many module files now have good material, but the final voice pass should reduce repeated phrasing and repeated section patterns. The content should feel curated, not assembled.

Completion criterion: no module README reads like a generated index. Each should explain why the module exists, what decision it teaches, and where the student practices it.

### 6. Cleanup and release hardening should wait

The repo intentionally contains temporary apply/check scripts from iterative packaging. Do not clean them while content is still moving. Cleanup should happen after the course-quality pass is complete.

Completion criterion: final cleanup removes temporary scripts, stale generated folders, unused release notes, and any duplicated material.

## 40-hour learning journey

The one-week version should not attempt to teach every page live. It should guide students through decisions and evidence.

| Day | Live focus | Lab or artifact | Exit evidence |
|---|---|---|---|
| Day 1 | Security lens, architecture, OWASP, BIML | Architecture risk review | Trust-boundary map and top risks |
| Day 2 | LLM and RAG | BrokenPilot direct injection, output handling, retrieval authz | Evidence log plus control explanation |
| Day 3 | Agents, tools, MLOps | BrokenPilot tool/memory labs plus MLOps evidence review | Tool permission decision and supply-chain recommendation |
| Day 4 | Privacy, adversarial ML, red-team method | Privacy lab, toy classifier, finding rewrite | Strong finding with validation and residual risk |
| Day 5 | Capstone | BrokenPilot final review | Final report and executive readout |

## What not to add

Avoid adding more broad theory unless it directly supports a graded decision or lab. Do not add:

- more standalone framework summaries;
- more untested lab ideas;
- more duplicate RAG or agent paper labs;
- a fake MLOps runtime pipeline unless it teaches more than the evidence pack;
- more capstone deliverables without removing or consolidating existing ones.

## Completion backlog

| Priority | Item | Why it matters | Type |
|---|---|---|---|
| P1 | Complete BrokenPilot final dry run using current labs | Validates the flagship course path | Content plus assessment |
| P1 | Add toy-classifier instructor guide | Prevents overclaiming and improves classroom delivery | Instructor support |
| P1 | Add complete MLOps evidence-pack model answer | Makes Module 08 gradable and self-study friendly | Worked example |
| P2 | Reasoning-lab anchor matrix | Ensures non-runnable labs are still graded well | Assessment quality |
| P2 | Module README voice pass | Reduces generated feel and improves student reading flow | Editorial |
| P2 | Capstone integration map update | Ensures all improved labs feed the final report | Course coherence |
| P3 | MkDocs strict navigation | Release quality only after content freeze | Website |
| P3 | CI consolidation | Protects runnable labs after final structure settles | Release engineering |
| P3 | Temporary script cleanup | Removes iterative packaging artifacts | Repository hygiene |

## Release readiness line

The course should be considered content-complete when:

- every module has a clear decision outcome;
- every attack lab has observable failure and observable fix;
- every reasoning lab has a graded artifact and anchors;
- the capstone can be completed from current docs without instructor improvisation;
- BrokenPilot and toy-classifier tests pass;
- the 40-hour path has no unresolved content dependency.

Only then should we fight MkDocs strict mode, CI polish, and cleanup.
'''

LAB_MATURITY_MATRIX = r'''
# Lab Coverage and Maturity Matrix

Purpose: track whether each lab has the right modality, observable behavior when appropriate, and a graded artifact.

## Lab quality standard

Attack labs should show an observable failure and an observable fix. Reasoning labs do not need runtime behavior, but they must end in a graded artifact with anchors.

| Bar | Meaning |
|---|---|
| Observable failure | Student can reproduce the unsafe behavior. |
| Observable fix | Student can enable or design a control and see the security property change. |
| Graded artifact | Student submits a concrete engineering deliverable. |
| Naive fix fails | The lab shows why prompt wording, policy text, or vague guardrails are insufficient. |
| Defense in depth | At least one control interaction is visible or reasoned through. |
| Resettable or bounded | Attack labs reset cleanly; reasoning labs have bounded evidence packs. |
| Anchored grading | Strong and weak examples or a rubric exist. |

## Current lab maturity

| Area | Lab | Modality | Current maturity | Next improvement |
|---|---|---|---|---|
| LLM direct injection | BrokenPilot direct prompt injection | Runnable | Strong | Add to capstone dry-run path. |
| LLM output handling | BrokenPilot render endpoint | Runnable | Strong | Ensure Module 05 debrief stresses sink-specific encoding. |
| RAG retrieval authz | BrokenPilot retrieval path | Runnable | Strong | Consolidate remaining paper RAG references into this path. |
| Agent tool authz | BrokenPilot tool update path | Runnable | Strong | Keep as reference standard. |
| Agent memory poisoning | BrokenPilot memory path | Runnable | Strong | Keep defense-in-depth lesson central. |
| Privacy leakage | BrokenPilot cross-tenant retrieval | Runnable | Medium-high | Add logging-still-leaks optional debrief. |
| Red-team chain | BrokenPilot capstone | Runnable | High | Run a complete final report with current labs. |
| OWASP ML input manipulation | Toy classifier evasion | Runnable | Medium-high | Add instructor debrief and caution against overclaiming. |
| OWASP ML poisoning | Toy classifier poisoning | Runnable | Medium-high | Add strong student interpretation example. |
| OWASP ML model theft | Toy classifier extraction | Runnable | Medium | Explain approximation limits. |
| OWASP ML output integrity | Toy classifier threshold tampering | Runnable | Medium-high | Tie to deployment controls and change management. |
| MLOps supply chain | Evidence-pack review | Reasoning | Medium-high | Add complete model answer. |
| Membership inference | Tabletop | Reasoning | Medium-high | Confirm residual-risk deliverable. |
| Poisoning/backdoor tabletop | Tabletop | Reasoning | Medium-high | Keep separate from toy runnable poisoning. |
| BIML architecture review | DocOps review | Reasoning | High | Ensure it feeds Day 1 checkpoint. |
| Red-team scoping | Scope tabletop | Reasoning | Medium-high | Add scope-quality anchors to instructor runbook. |

## Key routing decisions

1. BrokenPilot owns LLM, RAG, agent, privacy, and integrated red-team paths.
2. Toy classifier owns classical ML and adversarial ML paths.
3. MLOps remains evidence-review based.
4. Reasoning labs are not second-class labs; they are graded on decision quality, not runtime behavior.
5. Paper duplicates should route to runnable targets instead of being maintained as parallel labs.

## Completion gaps

| Gap | Impact | Suggested fix |
|---|---|---|
| No complete current capstone dry run | Students may not see how new labs combine into final report | Add complete current final report sample. |
| Toy classifier lacks instructor debrief | Risk of toy lab being interpreted as a real attacker capability lab | Add facilitation and debrief guide. |
| MLOps pack lacks full answer | Grading may vary by instructor | Add complete model answer. |
| Reasoning labs have uneven anchor coverage | Self-study students may not know what good looks like | Add anchor matrix and fill missing examples. |
| Cleanup deferred | Repo feels iterative | Keep cleanup deferred until content freezes. |
'''

MODULE_SEQUENCE_MAP = r'''
# Module Sequence and Dependency Map

Purpose: make the module order explicit so instructors understand why the course moves from foundations to application security, then to supply chain, privacy, robustness, red team, and capstone.

## Sequence logic

| Phase | Modules | Why this order matters |
|---|---|---|
| Foundations | 01 to 04 | Students learn the security lens, architecture mapping, taxonomy, and architectural risk analysis before touching labs. |
| Application behavior | 05 to 07 | Students observe how LLM, RAG, and agent systems fail when text, retrieval, and tool authority are confused. |
| Lifecycle and data risk | 08 to 10 | Students move beyond app behavior into artifacts, privacy, and model robustness. |
| Testing and synthesis | 11 to 12 | Students turn observations into scoped tests, evidence, findings, controls, and residual-risk decisions. |

## Dependency map

| Module | Depends on | Feeds into |
|---|---|---|
| 01 | none | every module, especially 05 to 07 control-placement decisions |
| 02 | 01 | threat models, RAG boundaries, tool boundaries, MLOps provenance |
| 03 | 01, 02 | toy classifier, red-team finding classification, capstone taxonomy |
| 04 | 01, 02, 03 | architecture risk review, capstone system analysis |
| 05 | 01 to 04 | RAG injection, output handling, red-team attack chains |
| 06 | 05 | privacy leakage, capstone retrieval findings |
| 07 | 05, 06 | capstone action safety and defense in depth |
| 08 | 02, 03, 04 | MLOps review and launch recommendation |
| 09 | 02, 06 | privacy findings, logging decisions, capstone residual risk |
| 10 | 03 | toy classifier and robustness decision-making |
| 11 | all previous | final capstone methodology and report quality |
| 12 | all previous | final integrated assessment |

## Where students usually struggle

| Point | Common failure | Instructor intervention |
|---|---|---|
| After Module 03 | Treating OWASP as a checklist instead of evidence taxonomy | Ask what evidence proves the category. |
| During Module 05 | Treating prompt injection as a prompt-writing problem | Ask where authority should be enforced. |
| During Module 06 | Thinking RAG is safe because documents are internal | Ask who is allowed to retrieve, summarize, cite, and log each document. |
| During Module 07 | Letting the model authorize tools | Ask which component checks actor, action, target, and approval. |
| During Module 08 | Reporting supply-chain smells without promotion decision | Ask whether the artifact can be promoted today and why. |
| During Module 09 | Treating privacy as only direct disclosure | Ask about inference, reconstruction, logs, and cross-tenant summaries. |
| During Module 10 | Reporting evasion as a trick | Ask whether the classifier is safe as a hard gate. |
| During Module 11 | Writing test cases without decision relevance | Ask what launch or control decision the evidence changes. |
| During Module 12 | Writing a bug list instead of a risk decision | Ask for evidence, control, validation, residual risk, and owner. |

## Day-by-day dependency checkpoints

| Day | Checkpoint | Must be true before moving on |
|---|---|---|
| Day 1 | Architecture and risk framing | Students can draw boundaries and state abuse cases. |
| Day 2 | LLM and RAG evidence | Students can distinguish untrusted text from authority and explain retrieval authorization. |
| Day 3 | Agent and supply-chain decisions | Students can separate model intent from tool execution and judge artifact promotion evidence. |
| Day 4 | Privacy, robustness, and reporting | Students can write a finding with validation and residual risk. |
| Day 5 | Capstone synthesis | Students can defend a launch, pilot, or delay recommendation using evidence. |
'''

CAPSTONE_INTEGRATION_MAP = r'''
# BrokenPilot Capstone Integration Map

Purpose: make sure the capstone uses the current course assets rather than older paper-only assumptions.

## Capstone scope

BrokenPilot is the capstone target for LLM application, RAG, agent, privacy, and red-team integration. It is not the target for classical ML evasion, poisoning, model extraction, or MLOps supply-chain runtime behavior.

## Current capstone-relevant evidence paths

| Evidence path | Module source | Runtime target | What the student observes |
|---|---|---|---|
| Direct prompt injection | 05 | BrokenPilot `/chat` | User-supplied override changes behavior when the filter is off. |
| Insecure output handling | 05 | BrokenPilot `/render` | Model-derived output reaches an HTML sink raw unless output encoding is enabled. |
| Indirect prompt injection | 06 | BrokenPilot retrieval and chat | Retrieved document text can steer response behavior when treated as instruction. |
| Cross-tenant retrieval | 06, 09 | BrokenPilot `/retrieve` and `/chat` | A beta user can see alpha restricted data when retrieval authorization is off. |
| Tool confused deputy | 07 | BrokenPilot `/tools/update-ticket` and `/agent/run` | Tool execution can affect a target object without target-object authorization. |
| Memory poisoning | 07 | BrokenPilot memory endpoints | Poisoned memory can steer intent, while tool authorization can still block execution. |
| Red-team chain | 11 | BrokenPilot mixed path | Student combines multiple findings into a scoped test narrative. |

## Capstone deliverables

A complete capstone submission should include:

1. System context and assumptions.
2. Evidence log with at least three reproduced behaviors.
3. Findings with root cause, impact, control, validation, and residual risk.
4. Permission or control matrix for at least one tool or retrieval path.
5. Leadership recommendation: launch, limited pilot, or delay.
6. Short executive readout.

## Minimum evidence set

For a 40-hour course, require three findings rather than every possible finding:

| Required area | Acceptable evidence |
|---|---|
| One LLM/RAG finding | Direct injection, indirect injection, output handling, or retrieval authorization. |
| One agent/tool finding | Tool confused deputy, weak approval, or memory poisoning interaction. |
| One privacy or governance finding | Cross-tenant leakage, logging risk, or weak evidence for safe operation. |

## Strong capstone pattern

A strong capstone does not say, "the AI can be tricked." It says:

- what trust boundary was crossed;
- what evidence demonstrates the behavior;
- what control enforces the security property;
- how the control was validated;
- what risk remains after the control;
- who owns the next decision.

## Capstone dry-run gap

The next major content task should be a complete final-report example based on the current lab set. Previous examples are useful, but the course now has new evidence paths. The current dry run should include:

- direct prompt injection;
- output handling;
- cross-tenant privacy leakage;
- memory poisoning plus tool authorization as the defense-in-depth moment;
- one leadership recommendation.
'''

ASSESSMENT_MAP = r'''
# End-to-End Assessment Map

Purpose: align module learning outcomes, labs, checkpoints, and final capstone grading.

## Assessment principle

Students are not graded for making systems fail. They are graded for producing useful security engineering evidence:

- what failed;
- why it failed;
- what property was violated;
- what control would enforce the property;
- how the control is validated;
- what risk remains.

## Assessment chain

| Stage | Student output | Instructor checks |
|---|---|---|
| Day 1 foundation checkpoint | trust-boundary map and abuse cases | Has concrete assets, actors, flows, and assumptions. |
| Day 2 app security checkpoint | LLM/RAG evidence log | Shows vulnerable and controlled behavior. |
| Day 3 agent and supply-chain checkpoint | tool permission decision and artifact promotion recommendation | Distinguishes model intent, tool execution, artifact integrity, and approval. |
| Day 4 reporting checkpoint | rewritten finding with validation and residual risk | Avoids vague guardrail language. |
| Day 5 capstone | final report and executive readout | Connects evidence to decision. |

## Rubric alignment

| Rubric dimension | Weak submission | Strong submission |
|---|---|---|
| Evidence | Screenshot or vague claim | Reproducible step, observed behavior, and affected boundary. |
| Root cause | "The AI was tricked" | Untrusted text, retrieval, memory, or model output was trusted by the wrong component. |
| Control | "Add guardrails" | Authorization, encoding, provenance, approval, isolation, or monitoring control with owner. |
| Validation | Not described | Shows how to test the control and what result proves it. |
| Residual risk | Ignored | States what remains and how it is monitored or accepted. |
| Decision relevance | Bug list | Launch, pilot, delay, scope, or monitoring decision. |

## Missing assessment anchors

| Area | Current state | Action |
|---|---|---|
| Current BrokenPilot capstone final report | Older examples exist, but new evidence paths were added | Create a current full final report. |
| Toy classifier interpretation | Tests exist, but classroom interpretation can drift | Add instructor guide and example student interpretation. |
| MLOps evidence pack | Strong/weak examples exist | Add complete model answer. |
| Reasoning-lab matrix | Anchors added across several labs | Add a single matrix that confirms coverage. |

## Completion criterion

The course is assessment-complete when an instructor can grade a student using only:

- the daily checkpoint rubric;
- the lab deliverable quality checklist;
- the final capstone rubric;
- strong and weak anchors;
- the complete final report example.
'''

INSTRUCTOR_GUIDE = r'''
# Instructor Guide: Teaching the Course as One Journey

Purpose: help instructors avoid teaching the course as twelve disconnected topics.

## The through-line to repeat

Models create new failure modes, but the engineering question remains familiar:

> What can this component influence, and what must enforce the boundary?

Use that question in every module.

## How to frame each phase

### Phase 1: Foundations

Tell students that Modules 01 to 04 are not background reading. They are the vocabulary needed to make later lab findings precise. The goal is to prevent vague statements such as "the AI is risky" and replace them with asset, boundary, evidence, control, and decision language.

### Phase 2: LLM, RAG, and agents

These modules are the heart of the course. Keep the distinction sharp:

- prompts influence behavior;
- retrieval supplies untrusted content;
- tools change state;
- memory persists influence;
- the application must enforce authority.

### Phase 3: Lifecycle, privacy, and robustness

This phase prevents students from thinking ML security is only prompt injection. Supply chain, privacy, and robustness show that risk also comes from training data, artifacts, logs, thresholds, evaluation gaps, and deployment choices.

### Phase 4: Red team and capstone

Students should stop collecting tricks and start producing decision evidence. The capstone should be judged by whether the evidence changes launch, pilot, scope, control, or monitoring decisions.

## Instructor checkpoints

| Moment | Ask this question |
|---|---|
| After architecture mapping | What is the highest-risk boundary and why? |
| After prompt injection | Did the system confuse text with authority? |
| After RAG | Was retrieval authorization enforced before the model saw the document? |
| After agent tools | Who authorized the actor, action, target, and approval? |
| After MLOps | Would you promote this artifact today? What evidence is missing? |
| After privacy | What could leak through logs, summaries, or inference even if direct access is blocked? |
| After robustness | Is this classifier safe as a hard gate? |
| After red-team planning | What decision will this test inform? |

## What to cut if time is tight

Cut breadth before cutting synthesis.

Keep:

- one architecture review;
- one LLM/RAG behavior;
- one agent/tool behavior;
- one privacy or MLOps reasoning artifact;
- one finding rewrite;
- the capstone recommendation.

Cut or assign as self-study:

- secondary framework comparisons;
- extra reference reading;
- duplicate paper labs when a runnable path exists;
- optional release-engineering discussions;
- website navigation and repo cleanup.

## How to handle questions about realism

Be direct:

- BrokenPilot is a teaching target, not a production benchmark.
- Toy classifier is synthetic and deterministic by design.
- The MLOps evidence pack is closer to real review work than a fake pipeline would be.
- The course teaches security decisions, not exploit novelty.

## End-of-course standard

A student has succeeded if they can explain:

1. what failed;
2. what boundary was crossed;
3. what control enforces the boundary;
4. how to validate the control;
5. what risk remains;
6. what decision leadership should make.
'''

COMPLETION_SCORECARD = r'''
# Course Completion Scorecard

Purpose: define what "100 percent complete" means before final cleanup and release work.

## Scorecard

| Area | Required for content complete | Status to verify |
|---|---|---|
| Module decision outcome | Every module has a clear decision students must learn to make | Check module reading guides and lab-path files. |
| Runnable attack labs | BrokenPilot and toy classifier show observable failure and fix where appropriate | Run pytest and spot-check lab guides. |
| Reasoning labs | Every reasoning lab has a deliverable and grading anchor | Use reasoning-lab anchor matrix. |
| Capstone | Current full dry-run report exists | Create or update final report example after latest labs. |
| Instructor support | 40-hour runbook, troubleshooting, and module teaching guides exist | Verify no day depends on improvisation. |
| Student support | Lab journal, checkpoints, and workbook exist | Verify the student can self-study. |
| Assessment | Rubrics map to daily and final deliverables | Verify no rubric rewards only exploit count. |
| Cleanup | Temporary scripts and generated artifacts removed or moved | Defer until content freeze. |
| Website | MkDocs builds strictly with intentional navigation | Defer until content freeze. |
| CI | BrokenPilot and toy classifier tests run | Defer final consolidation until content freeze. |

## Definition of content complete

The course is content-complete when the remaining backlog is only cleanup, navigation, CI, release packaging, and style polishing.

Content-complete does not mean perfect. It means a real cohort can complete the course without hitting missing assets, ungraded deliverables, or unsupported claims.

## Remaining content tasks before cleanup

1. Create current complete BrokenPilot capstone final report.
2. Add toy-classifier instructor guide and debrief.
3. Add complete MLOps evidence-pack model answer.
4. Add reasoning-lab anchor matrix.
5. Do a module README voice pass.
6. Run one final 40-hour course dry-run checklist.

## Cleanup tasks after content complete

1. Remove temporary apply scripts that were only used to patch the repo during development.
2. Keep durable check scripts only.
3. Remove stale release notes or consolidate them into the changelog.
4. Clean generated folders from the repo.
5. Normalize file naming and navigation.
6. Finish MkDocs strict build and nav.
7. Finish CI with BrokenPilot and toy-classifier tests.
8. Read top-level docs for generated-looking phrasing and repetition.
'''

CHECK_SCRIPT = r'''
from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()

REQUIRED_FILES = [
    "COURSE_FLOW_REVIEW.md",
    "labs/LAB_COVERAGE_AND_MATURITY_MATRIX.md",
    "modules/MODULE_SEQUENCE_AND_DEPENDENCY_MAP.md",
    "labs/brokenpilot/CAPSTONE_INTEGRATION_MAP.md",
    "assessments/END_TO_END_ASSESSMENT_MAP.md",
    "instructor/teaching-the-course-as-one-journey.md",
    "COURSE_COMPLETION_SCORECARD.md",
]

MODULE_IDS = [f"{i:02d}" for i in range(1, 13)]

REQUIRED_TERMS = [
    "Completion decision",
    "BrokenPilot",
    "toy classifier",
    "MLOps",
    "capstone",
    "residual risk",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        fail(f"missing {path}")
    return target.read_text(encoding="utf-8")


def main() -> None:
    for path in REQUIRED_FILES:
        text = read(path)
        if len(text.split()) < 250:
            fail(f"{path} looks too thin")

    flow = read("COURSE_FLOW_REVIEW.md")
    for term in REQUIRED_TERMS:
        if term not in flow:
            fail(f"COURSE_FLOW_REVIEW.md missing term: {term}")
    for module_id in MODULE_IDS:
        if f"{module_id}" not in flow:
            fail(f"COURSE_FLOW_REVIEW.md missing module id {module_id}")

    matrix = read("labs/LAB_COVERAGE_AND_MATURITY_MATRIX.md")
    for phrase in ["Observable failure", "Observable fix", "Reasoning", "Runnable"]:
        if phrase not in matrix:
            fail(f"lab matrix missing {phrase}")

    sequence = read("modules/MODULE_SEQUENCE_AND_DEPENDENCY_MAP.md")
    for phrase in ["Foundations", "Application behavior", "Lifecycle and data risk", "Testing and synthesis"]:
        if phrase not in sequence:
            fail(f"sequence map missing phase {phrase}")

    capstone = read("labs/brokenpilot/CAPSTONE_INTEGRATION_MAP.md")
    for phrase in ["Direct prompt injection", "Insecure output handling", "Memory poisoning", "Minimum evidence set"]:
        if phrase not in capstone:
            fail(f"capstone map missing {phrase}")

    scorecard = read("COURSE_COMPLETION_SCORECARD.md")
    for phrase in ["Definition of content complete", "Remaining content tasks before cleanup", "Cleanup tasks after content complete"]:
        if phrase not in scorecard:
            fail(f"scorecard missing {phrase}")

    cleanup = ROOT / "CLEANUP_BEFORE_RELEASE.md"
    if cleanup.exists():
        cleanup_text = cleanup.read_text(encoding="utf-8")
        if "Course flow review" not in cleanup_text:
            fail("CLEANUP_BEFORE_RELEASE.md was not updated with course flow review cleanup note")

    print("Course flow review pass checks passed.")


if __name__ == "__main__":
    main()
'''


def main() -> None:
    write("COURSE_FLOW_REVIEW.md", COURSE_FLOW_REVIEW)
    write("labs/LAB_COVERAGE_AND_MATURITY_MATRIX.md", LAB_MATURITY_MATRIX)
    write("modules/MODULE_SEQUENCE_AND_DEPENDENCY_MAP.md", MODULE_SEQUENCE_MAP)
    write("labs/brokenpilot/CAPSTONE_INTEGRATION_MAP.md", CAPSTONE_INTEGRATION_MAP)
    write("assessments/END_TO_END_ASSESSMENT_MAP.md", ASSESSMENT_MAP)
    write("instructor/teaching-the-course-as-one-journey.md", INSTRUCTOR_GUIDE)
    write("COURSE_COMPLETION_SCORECARD.md", COMPLETION_SCORECARD)
    write("scripts/check_course_flow_review_pass.py", CHECK_SCRIPT)

    append_once(
        "README.md",
        "<!-- course-flow-review-pass -->",
        """
<!-- course-flow-review-pass -->

## Course flow review

The current v1.1-dev work includes an end-to-end course flow review in `COURSE_FLOW_REVIEW.md`. Use it to understand the 40-hour journey, remaining content gaps, lab maturity, and what must be true before final cleanup and release hardening.
""",
    )
    append_once(
        "CLEANUP_BEFORE_RELEASE.md",
        "<!-- course-flow-review-cleanup-note -->",
        """
<!-- course-flow-review-cleanup-note -->

## Course flow review cleanup note

Before release, reconcile `COURSE_FLOW_REVIEW.md`, `COURSE_COMPLETION_SCORECARD.md`, and the cleanup checklist so the repo has one final release-readiness source of truth. Remove temporary apply scripts after all course content stops moving.
""",
    )
    write(
        "release-notes/v1.1-dev-course-flow-review-pass.md",
        """
# v1.1-dev course flow review pass

Added an end-to-end course flow review, lab maturity matrix, module dependency map, capstone integration map, assessment map, instructor journey guide, and completion scorecard.

This pass intentionally does not fight MkDocs strict mode or repository cleanup. It defines what remains before the course can be considered content-complete.
""",
    )
    print("\nApplied course flow review pass.")


if __name__ == "__main__":
    main()
