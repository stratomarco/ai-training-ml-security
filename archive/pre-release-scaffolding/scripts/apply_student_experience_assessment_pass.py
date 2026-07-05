from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.strip() + "\n", encoding="utf-8")
    print(f"wrote: {path}")


def append_marker(path: str, marker: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        existing = target.read_text(encoding="utf-8")
    else:
        existing = f"# {Path(path).stem.replace('-', ' ').title()}\n"

    start = f"<!-- {marker}:START -->"
    end = f"<!-- {marker}:END -->"
    block = f"\n{start}\n{text.strip()}\n{end}\n"

    if start in existing and end in existing:
        before = existing.split(start)[0]
        after = existing.split(end, 1)[1]
        updated = before + block + after
    else:
        updated = existing.rstrip() + "\n" + block

    target.write_text(updated, encoding="utf-8")
    print(f"updated: {path}")


LAB_JOURNAL_GUIDE = """
# Student lab journal guide

This guide gives students one consistent way to record evidence across BrokenPilot, the toy classifier, and reasoning labs.

The journal is not a screenshot dump. It is a short engineering record that proves the student understood the failure, the control, the validation method, and the remaining risk.

## What every lab entry must contain

1. Lab name and module.
2. System state before the test, including user, tenant, role, control flags, and reset status when relevant.
3. Exact command, HTTP request, UI action, or review step used to produce the observation.
4. Observable failure or review evidence.
5. Root cause in security-engineering terms.
6. Control or design change proposed.
7. Validation step that proves the security property changed.
8. Residual risk and operational follow-up.

## Attack lab entries

Attack labs must show both the vulnerable behavior and the controlled behavior when the lab supports it.

For BrokenPilot this usually means:

```text
/reset
controls off
run the request
record the unsafe observation
controls on
run the same request
record the changed security property
```

For the toy classifier this usually means:

```text
train the baseline model
run the attack script
record the before and after prediction or score
explain why the model should not be used as a hard authorization gate without fallback
```

## Reasoning lab entries

Reasoning labs are graded differently. They may not have a runnable failure. They must still end with an engineering artifact.

Examples:

- architecture risk review
- supply-chain evidence review
- privacy risk assessment
- red-team scope
- residual-risk memo

A good reasoning entry names the decision a real team must make, the evidence that supports the decision, the control backlog, and the residual risk.

## Evidence hygiene

Use fake local data only. Do not paste real tokens, customer records, production logs, or proprietary incident details. When a lab uses a fake secret, label it clearly as training-only evidence.
"""

STUDENT_LAB_JOURNAL_TEMPLATE = """
# Student lab journal template

Use one copy of this template per lab or checkpoint.

## Lab identity

- Student or team:
- Module:
- Lab:
- Date:
- Lab class: attack lab / reasoning lab
- Target: BrokenPilot / toy classifier / evidence pack / tabletop

## Initial state

- Reset performed:
- User, tenant, and role:
- Relevant control flags:
- Dataset or evidence pack used:
- Assumptions:

## Observation 1: vulnerable behavior or review evidence

### Action taken

Record the command, API request, UI action, or review step.

```text
paste command, request, or review note here
```

### Result observed

```text
paste relevant local output or short paraphrase here
```

### Security property affected

Examples: authorization, tenant isolation, instruction/data separation, output handling, provenance, model robustness, privacy, auditability.

## Root cause

Explain the design weakness. Avoid saying only that the model was tricked.

## Naive fix and why it is insufficient

Describe the quick fix a team might suggest and why it does not fully address the root cause.

## Proposed control

Name the concrete control, owner, and enforcement point.

## Validation

Show how the same scenario changes after the control or design rule is applied.

```text
paste validation result here
```

## Residual risk

What still needs monitoring, approval, rollback, incident response, or follow-up review?

## Graded conclusion

One paragraph that a technical lead or security reviewer could act on.
"""

DAILY_CHECKPOINT_TEMPLATE = """
# Daily checkpoint submission template

Use this template for the end-of-day checkpoint in the 40-hour course.

## Day and theme

- Day:
- Theme:
- Team members:

## Required artifacts submitted

List the artifacts completed today.

## Best evidence

Paste the single strongest piece of local evidence or review evidence from the day. Keep it short.

## Most important root cause

Explain the most important root cause learned today.

## Control decision

What control, design change, or review gate would you implement first?

## Validation or confidence argument

How would you prove the control works, or what evidence gives confidence for a reasoning lab?

## Residual risk

What remains open after your proposed control?

## Question for the instructor

One question that would improve your design or report.
"""

DAILY_CHECKPOINTS = """
# 40-hour daily checkpoints

These checkpoints make the one-week course easier to run and easier to grade. They are short, evidence-based, and tied to the labs students already perform.

## Grading posture

Daily checkpoints are lightweight. They are used to catch misunderstandings early. The final capstone remains the main graded artifact.

Use this weighting for a 40-hour professional course:

| Component | Weight |
|---|---:|
| Daily checkpoints | 20 percent |
| Lab journal quality | 20 percent |
| BrokenPilot or toy-classifier evidence | 20 percent |
| Capstone report | 30 percent |
| Final presentation or readout | 10 percent |

## Day 1 checkpoint: system and security boundaries

### Student submits

- one system context diagram or text equivalent
- one trust-boundary list
- two abuse cases
- one early risk statement

### Instructor checks

- The student distinguishes model behavior from system security behavior.
- Trust boundaries are explicit.
- At least one abuse case describes misuse by an authorized user.

### Common weak answer

The student says the solution is to make the prompt stronger, without identifying an enforcement point.

## Day 2 checkpoint: LLM, RAG, and output handling

### Student submits

- one direct or indirect prompt-injection observation
- one retrieval or tenant-isolation observation
- one output-handling observation or explanation
- one proposed control and validation step

### Instructor checks

- The student explains untrusted text treated as authority.
- The student can name the trust boundary for user input and retrieved content.
- The student understands that output must be encoded or validated for the downstream context.

## Day 3 checkpoint: agents and supply chain

### Student submits

- one tool authorization finding or permission matrix
- one evidence-pack supply-chain finding
- one approval or promotion-gate recommendation

### Instructor checks

- The student separates model intent from tool execution.
- The student can identify provenance and artifact-integrity gaps.
- The recommendation is implementable by an engineering team.

## Day 4 checkpoint: privacy, adversarial ML, and red-team reporting

### Student submits

- one privacy leakage finding or privacy tabletop review
- one toy-classifier observation or adversarial ML risk argument
- one rewritten finding using the course finding format

### Instructor checks

- The student avoids overclaiming from toy data.
- The student frames model robustness around engineering decisions and fallbacks.
- The finding includes root cause, control, validation, and residual risk.

## Day 5 checkpoint: capstone readiness

### Student submits

- final finding list
- remediation backlog
- residual-risk section
- leadership recommendation

### Instructor checks

- The report does not grade the model alone.
- Evidence is local and reproducible.
- Findings map to concrete controls and validation steps.
- The recommendation is clear: launch, limited pilot, delay, or stop.
"""

CHECKPOINT_RUBRIC = """
# 40-hour checkpoint rubric

Use this rubric for daily checkpoints and short lab deliverables.

| Criterion | Strong | Weak |
|---|---|---|
| Evidence | Shows the exact local observation or review artifact | Gives a vague claim with no reproducible support |
| Root cause | Names the violated security property and design weakness | Says the model was tricked or the AI failed |
| Control | Identifies an enforcement point, owner, and concrete change | Says add guardrails, monitor more, or improve prompt |
| Validation | Re-runs the scenario or explains the confidence argument | Assumes the fix works |
| Residual risk | Names what remains and how it is managed | Claims the risk is fully solved |
| Communication | Gives a decision-ready summary | Uses tool output without interpretation |

## Scoring

- 3: strong and actionable
- 2: mostly correct but missing one important element
- 1: partial, vague, or not tied to evidence
- 0: absent or unsafe

A passing checkpoint should average at least 2 across the six criteria.
"""

DELIVERABLE_CHECKLIST = """
# Lab deliverable quality checklist

Use this checklist before submitting any lab artifact.

## Required for attack labs

- I reset the environment or documented the initial state.
- I captured the vulnerable behavior.
- I changed one relevant control or design rule.
- I re-ran the same scenario.
- I explained the security property that changed.
- I explained why a naive fix is insufficient.
- I documented residual risk.

## Required for reasoning labs

- I named the engineering decision being reviewed.
- I cited evidence from the provided artifact, scenario, or evidence pack.
- I separated likelihood, impact, and uncertainty.
- I proposed implementable controls.
- I included validation or assurance evidence.
- I included residual risk.

## Required for all labs

- The graded artifact is the control decision and validation, not the exploit.
- The write-up is short enough for a technical lead to read.
- No real secrets, customer data, production logs, or sensitive company details are included.
"""

INSTRUCTOR_RUNBOOK = """
# 40-hour student experience runbook

This runbook helps the instructor manage the course as a one-week professional training, not as twelve independent lectures.

## Course rhythm

Use the same rhythm each day:

1. Frame the security property.
2. Demonstrate the vulnerable or risky condition.
3. Let students reproduce or review the evidence.
4. Discuss why naive fixes are insufficient.
5. Convert evidence into a graded artifact.
6. Close with a checkpoint.

## What to protect

Do not let the class become a prompt-hacking tournament. The purpose is security engineering. The best student output is a control decision with validation and residual risk.

## Daily instructor flow

### Start of day

- State the day theme.
- Name the required deliverable.
- Show one strong example and one weak example when available.
- Remind students which target is in use: BrokenPilot, toy classifier, evidence pack, or tabletop.

### During labs

Watch for these failure modes:

- Students focus on clever payloads instead of root cause.
- Students propose prompt wording as the primary control.
- Students record screenshots without explaining the security property.
- Students overclaim from toy data.
- Students ignore residual risk.

Intervene by asking:

- What is the enforcement point?
- What changes when the control is enabled?
- What would an engineer implement?
- What would you monitor after rollout?
- What could still go wrong?

### End of day

Collect a short checkpoint. Give feedback on one item only: the highest-leverage gap for the next day.

## Suggested checkpoint timing

| Day | Checkpoint time | Main artifact |
|---|---:|---|
| 1 | 30 minutes | system boundary and abuse cases |
| 2 | 45 minutes | LLM/RAG/output-handling evidence |
| 3 | 45 minutes | tool control or supply-chain review |
| 4 | 45 minutes | privacy/adversarial/finding rewrite |
| 5 | 90 minutes | capstone report and readout |

## Instructor grading anchors

Strong submissions are concise, evidence-based, and implementable.

Weak submissions are long, clever, or dramatic, but do not identify an enforcement point or validation method.
"""

TROUBLESHOOTING = """
# Lab troubleshooting and reset guide

This guide keeps classroom support from overwhelming the instructor.

## General reset order

1. Confirm the student is in the correct directory.
2. Confirm the virtual environment is active.
3. Confirm dependencies are installed.
4. Reset generated state.
5. Re-run the smallest test.
6. Only then inspect application code.

## BrokenPilot quick checks

From `labs/brokenpilot/prototype-app`:

```powershell
python -m pip install -r requirements.txt
pytest
```

If a scenario behaves differently than expected:

- call `/reset`
- check `/controls`
- verify the user, tenant, and role
- verify the control flag being tested
- run the relevant test function before changing code

## Toy classifier quick checks

From `labs/toy-ml-attacks/toy-classifier-app`:

```powershell
python -m pip install -r requirements-dev.txt
python train.py
pytest
```

If attack output differs:

- delete generated model files
- re-run `python train.py`
- confirm the synthetic dataset was not edited
- confirm scikit-learn installed from the project requirements

## MLOps evidence pack checks

The evidence pack is not meant to run. Students inspect it. If a student tries to execute the notebook or pipeline, redirect them to the evidence-review task.

The intended task is to identify weak provenance, weak artifact integrity, weak promotion gates, and missing rollback evidence.

## What not to debug during class

- MkDocs strict navigation warnings
- OneDrive file locks on generated website folders
- cosmetic markdown warnings
- optional external DVAIA setup if the core BrokenPilot path is available

Those belong to release maintenance, not live teaching.
"""

CAPSTONE_CHECKPOINTS = """
# BrokenPilot capstone checkpoints

The capstone should not wait until the final hour. Use these checkpoints to keep student teams aligned with the expected report quality.

## Checkpoint 1: scope and system model

### Student produces

- target scope
- user and tenant assumptions
- trust boundaries
- attack surfaces
- out-of-scope items

### Instructor looks for

- no overclaim that BrokenPilot covers every module
- clear distinction between runnable findings and tabletop findings
- realistic user roles and tenant boundaries

## Checkpoint 2: reproducible evidence

### Student produces

- at least two runnable observations from BrokenPilot
- one clear before and after control comparison
- exact request, command, or UI path

### Instructor looks for

- evidence is local and fake
- the same scenario is re-run after a control changes
- the student explains the changed security property

## Checkpoint 3: remediation backlog

### Student produces

- prioritized controls
- owner or enforcement point
- validation method
- residual risk

### Instructor looks for

- fixes are not prompt-only
- authorization and approval controls sit outside the model
- logging, monitoring, and rollback are included where relevant

## Checkpoint 4: leadership recommendation

### Student produces

- final recommendation: launch, limited pilot, delay, or stop
- short rationale
- top three risks
- top three required controls

### Instructor looks for

- decision-ready communication
- clear residual risk
- no unsupported claims
- no dumping raw lab output without interpretation
"""

MODULE_12_CAPSTONE_CHECKPOINTS = """
# Module 12 capstone checkpoints

Use this page with the BrokenPilot capstone. The capstone is the final integration point for the course, so students should build the report over several checkpoints instead of writing it at the end.

## Required checkpoints

1. Scope and system model.
2. Reproducible evidence.
3. Remediation backlog.
4. Leadership recommendation.

Each checkpoint should update the same final report. Students should not submit four unrelated documents.

## Grading emphasis

The capstone is graded on evidence, root cause, implementable controls, validation, residual risk, and communication. It is not graded on the number of payloads attempted.

## How to use with the 40-hour course

- Day 1: start the scope and system model.
- Day 2: add LLM and RAG evidence.
- Day 3: add tool-control and supply-chain reasoning.
- Day 4: rewrite findings and add residual-risk language.
- Day 5: finish the report and readout.

## Common instructor intervention

If a student report says only that the agent can be tricked, ask where the trust boundary failed and what enforcement point would change the result.
"""

ANCHOR_BASED_GRADING = """
# Anchor-based grading guide

Anchor-based grading helps instructors give consistent feedback without turning the course into a checklist exercise.

## How to grade

For each deliverable, compare it to the closest strong and weak worked example. Then score based on the rubric.

Do not reward dramatic exploits without engineering analysis. Do not penalize a short answer if it contains evidence, root cause, control, validation, and residual risk.

## Strong anchor traits

- Uses exact local evidence or artifact evidence.
- Identifies the security property.
- Names the enforcement point.
- Shows how the control changes the outcome or confidence level.
- States residual risk.
- Gives a decision that a technical lead can act on.

## Weak anchor traits

- Says the AI was tricked.
- Recommends better prompts or guardrails without an enforcement point.
- Gives screenshots or raw output without interpretation.
- Skips validation.
- Claims the issue is fully solved.
- Does not connect the finding to a business or engineering decision.

## Feedback style

Give one high-leverage improvement per checkpoint. Students do not need line edits during the course. They need direction on the main gap in their reasoning.
"""

DOCS_STUDENT_WORKBOOK = """
# 40-hour student workbook

This workbook gives students a single path through the one-week version of the course.

## How to use it

For each day, complete the required labs or reasoning exercises, fill the lab journal, and submit the checkpoint. Keep the same evidence and wording for the final capstone where possible.

## Day 1

Focus: security foundations, system boundaries, and abuse cases.

Submit: system context, trust boundaries, two abuse cases, and one early risk statement.

## Day 2

Focus: LLM, RAG, direct and indirect injection, and output handling.

Submit: one vulnerable observation, one controlled observation, and one control validation.

## Day 3

Focus: agent/tool security and MLOps supply chain.

Submit: one permission or approval decision, and one evidence-pack supply-chain finding.

## Day 4

Focus: privacy, adversarial ML, and red-team reporting quality.

Submit: one privacy or adversarial finding and one rewritten strong finding.

## Day 5

Focus: BrokenPilot capstone report and readout.

Submit: final report, remediation backlog, residual-risk statement, and leadership recommendation.
"""

CHECK_SCRIPT = r"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "labs/STUDENT_LAB_JOURNAL_GUIDE.md",
    "course-templates/student-lab-journal-template.md",
    "course-templates/daily-checkpoint-submission-template.md",
    "assessments/40-hour-daily-checkpoints.md",
    "assessments/40-hour-checkpoint-rubric.md",
    "assessments/lab-deliverable-quality-checklist.md",
    "assessments/anchor-based-grading-guide.md",
    "instructor/40-hour-student-experience-runbook.md",
    "instructor/lab-troubleshooting-and-reset-guide.md",
    "labs/brokenpilot/CAPSTONE_CHECKPOINTS.md",
    "modules/12-capstone-brokenpilot/capstone-checkpoints.md",
    "docs/start-here/40-hour-student-workbook.md",
]

KEYWORDS = {
    "labs/STUDENT_LAB_JOURNAL_GUIDE.md": ["observable failure", "residual risk", "reasoning labs"],
    "course-templates/student-lab-journal-template.md": ["Root cause", "Validation", "Residual risk"],
    "assessments/40-hour-daily-checkpoints.md": ["Day 1", "Day 5", "Capstone report"],
    "assessments/40-hour-checkpoint-rubric.md": ["Evidence", "Root cause", "Residual risk"],
    "instructor/40-hour-student-experience-runbook.md": ["prompt-hacking tournament", "enforcement point", "checkpoint"],
    "instructor/lab-troubleshooting-and-reset-guide.md": ["BrokenPilot", "Toy classifier", "MLOps evidence pack"],
    "labs/brokenpilot/CAPSTONE_CHECKPOINTS.md": ["Checkpoint 1", "Checkpoint 4", "leadership recommendation"],
    "modules/12-capstone-brokenpilot/capstone-checkpoints.md": ["Scope and system model", "Reproducible evidence", "Remediation backlog"],
}


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit("Missing required files:\n" + "\n".join(missing))

    failures: list[str] = []
    for relpath, terms in KEYWORDS.items():
        text = (ROOT / relpath).read_text(encoding="utf-8").lower()
        for term in terms:
            if term.lower() not in text:
                failures.append(f"{relpath} missing {term!r}")

    if failures:
        raise SystemExit("Student experience checks failed:\n" + "\n".join(failures))

    print("Student experience and assessment checks passed.")


if __name__ == "__main__":
    main()
"""


def main() -> None:
    write("labs/STUDENT_LAB_JOURNAL_GUIDE.md", LAB_JOURNAL_GUIDE)
    write("course-templates/student-lab-journal-template.md", STUDENT_LAB_JOURNAL_TEMPLATE)
    write("course-templates/daily-checkpoint-submission-template.md", DAILY_CHECKPOINT_TEMPLATE)
    write("assessments/40-hour-daily-checkpoints.md", DAILY_CHECKPOINTS)
    write("assessments/40-hour-checkpoint-rubric.md", CHECKPOINT_RUBRIC)
    write("assessments/lab-deliverable-quality-checklist.md", DELIVERABLE_CHECKLIST)
    write("assessments/anchor-based-grading-guide.md", ANCHOR_BASED_GRADING)
    write("instructor/40-hour-student-experience-runbook.md", INSTRUCTOR_RUNBOOK)
    write("instructor/lab-troubleshooting-and-reset-guide.md", TROUBLESHOOTING)
    write("labs/brokenpilot/CAPSTONE_CHECKPOINTS.md", CAPSTONE_CHECKPOINTS)
    write("modules/12-capstone-brokenpilot/capstone-checkpoints.md", MODULE_12_CAPSTONE_CHECKPOINTS)
    write("docs/start-here/40-hour-student-workbook.md", DOCS_STUDENT_WORKBOOK)
    write("scripts/check_student_experience_assessment_pass.py", CHECK_SCRIPT)
    write(
        "release-notes/v1.1-dev-student-experience-assessment-pass.md",
        """
# v1.1-dev student experience and assessment pass

This package adds daily checkpoints, lab journal guidance, checkpoint rubrics, capstone checkpoints, and instructor troubleshooting support for the 40-hour course.

It does not change MkDocs strict mode, CI, or release cleanup. Those remain end-game tasks after content and labs stop moving.
""",
    )

    append_marker(
        "labs/README.md",
        "STUDENT_EXPERIENCE_PASS",
        """
## Student lab journal

Use `STUDENT_LAB_JOURNAL_GUIDE.md` and `../course-templates/student-lab-journal-template.md` to keep lab evidence consistent across BrokenPilot, the toy classifier, and reasoning labs.
""",
    )
    append_marker(
        "assessments/README.md",
        "STUDENT_EXPERIENCE_PASS",
        """
## 40-hour checkpoints and lab deliverables

Use `40-hour-daily-checkpoints.md`, `40-hour-checkpoint-rubric.md`, `lab-deliverable-quality-checklist.md`, and `anchor-based-grading-guide.md` for the one-week course.
""",
    )
    append_marker(
        "instructor/README.md",
        "STUDENT_EXPERIENCE_PASS",
        """
## Student experience support

Use `40-hour-student-experience-runbook.md` to run the daily course rhythm and `lab-troubleshooting-and-reset-guide.md` to keep lab support manageable.
""",
    )
    append_marker(
        "course-templates/README.md",
        "STUDENT_EXPERIENCE_PASS",
        """
## Student workflow templates

Use `student-lab-journal-template.md` and `daily-checkpoint-submission-template.md` for repeatable lab and checkpoint submissions.
""",
    )
    append_marker(
        "modules/12-capstone-brokenpilot/README.md",
        "STUDENT_EXPERIENCE_PASS",
        """
## Capstone checkpoints

Use `capstone-checkpoints.md` so students build the final report progressively instead of writing it all on the final day.
""",
    )
    append_marker(
        "CLEANUP_BEFORE_RELEASE.md",
        "STUDENT_EXPERIENCE_PASS",
        """
## Student experience package cleanup reminder

Before release, decide which temporary apply/check scripts stay. Keep durable quality checks, but remove one-time package application scripts after the content is stable.
""",
    )

    print("\nApplied student experience and assessment pass.")


if __name__ == "__main__":
    main()
