from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")
    print(f"wrote: {path}")


def append_once(path: str, marker: str, text: str) -> None:
    target = ROOT / path
    if not target.exists():
        print(f"skip missing file for append: {path}")
        return
    current = target.read_text(encoding="utf-8")
    start = f"<!-- {marker}:start -->"
    end = f"<!-- {marker}:end -->"
    block = f"\n\n{start}\n{text.strip()}\n{end}\n"
    if start in current and end in current:
        before = current.split(start)[0].rstrip()
        after = current.split(end, 1)[1].lstrip()
        target.write_text(before + block + "\n" + after, encoding="utf-8", newline="\n")
    else:
        target.write_text(current.rstrip() + block, encoding="utf-8", newline="\n")
    print(f"updated: {path}")


INSTRUCTOR_GUIDE = r'''
# Toy Classifier Facilitation Guide

This guide helps instructors run the toy-classifier lab for Modules 03 and 10. The lab is intentionally small and synthetic. Its purpose is not to teach malware detection, spam detection, or realistic phishing bypass. Its purpose is to make classical ML security failures observable in a controlled classroom setting.

## What the lab teaches

Students should leave with four security conclusions:

1. Model accuracy is not a security argument by itself.
2. A classifier used as a hard decision gate creates a security boundary.
3. Input manipulation, poisoned labels, model probing, and output-threshold tampering are different failure modes that need different controls.
4. The best deliverable is not proof that the model can be tricked. The best deliverable is a control plan with validation and residual risk.

## Recommended placement in the 40-hour course

Use this lab after students understand security boundaries and after they have seen OWASP ML risk categories.

| Course point | Use |
|---|---|
| Module 03 | Map each script to an OWASP ML risk category. |
| Module 10 | Discuss robustness, hard-gate risk, fallback, and monitoring. |
| Day 4 checkpoint | Ask for a short robustness decision memo. |

## Instructor setup

From the repository root:

```bash
cd labs/toy-ml-attacks/toy-classifier-app
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python train.py
pytest
```

PowerShell:

```powershell
cd labs\toy-ml-attacks\toy-classifier-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
python train.py
pytest
```

Expected test result: all toy-classifier tests pass.

## Live teaching flow

### 1. Baseline

Run:

```bash
python train.py
```

Ask students what the model is allowed to decide. Then ask what would change if this classifier blocked account access, escalated fraud cases, auto-closed tickets, or denied a transaction.

Teaching point: the security question is not whether the classifier is useful. The question is whether it is safe for the authority it has been given.

### 2. Evasion

Run:

```bash
python attacks/evasion.py
```

Students should observe that a small text perturbation changes the model outcome while the synthetic intent remains the same.

Ask:

- What security property changed?
- What would a naive fix look like?
- Why would blocking a few words not be enough?
- What would a robust control plan include?

Good answers mention input validation, adversarial test sets, confidence thresholds, fallback review, monitoring for drift in phrase distributions, and not using the classifier as the only enforcement point.

### 3. Poisoning

Run:

```bash
python attacks/poisoning.py
```

Students should observe that a few corrupted labels can change the model behavior after retraining.

Ask:

- Where would label poisoning enter a real pipeline?
- Who can submit labels, adjudicate labels, or approve training data?
- What evidence would you require before promoting the retrained model?

Good answers mention dataset provenance, label-review workflow, data versioning, holdout evaluation, approval gates, and rollback.

### 4. Extraction

Run:

```bash
python attacks/extraction.py
```

Students should observe that repeated queries reveal rough decision behavior.

Ask:

- Is this a model-theft issue, a privacy issue, an abuse-monitoring issue, or all three?
- What should change if the model is externally exposed?
- What logging is useful without creating a new privacy leak?

Good answers mention rate limits, query monitoring, canary prompts or synthetic probes, response minimization, and abuse detection. Strong answers also discuss what not to log.

### 5. Output integrity

Run:

```bash
python attacks/output_integrity.py
```

Students should observe that changing the decision threshold changes outcomes without changing the model.

Ask:

- Why is this not a model-training problem?
- Who should be allowed to change thresholds?
- How would you detect unauthorized threshold changes?

Good answers mention configuration integrity, change control, signed configuration, deployment provenance, audit trails, and separation of duties.

## Naive fixes to challenge

When students suggest a simple fix, test whether it actually changes the security property.

| Naive fix | Why it is insufficient | Better direction |
|---|---|---|
| Block the exact evasion words | Attackers can use other perturbations. | Robustness tests, fallback, monitoring. |
| Retrain with more data | More poisoned or biased data can worsen risk. | Data provenance, label governance, holdout tests. |
| Hide confidence scores | Query behavior can still leak decision boundaries. | Rate limits, monitoring, response minimization. |
| Only protect the model file | Threshold/config tampering can bypass the model. | Protect model, config, pipeline, and promotion gates. |

## Defense-in-depth moment

Use the output-integrity script to show that a model can remain unchanged while the system decision changes. This is the defense-in-depth lesson: ML security is not only model security. The model, feature pipeline, threshold, policy layer, deployment config, monitoring, and rollback path all matter.

## Graded artifact

Students should submit a short robustness decision memo, not just screenshots.

Required sections:

1. What authority the classifier has.
2. Which failure was observed.
3. Why the naive fix is insufficient.
4. What control should be implemented.
5. How the control should be validated.
6. What residual risk remains.
7. Whether the classifier can be used as a hard decision gate.

## Instructor grading anchors

A strong submission makes a decision. It does not say only that the classifier is vulnerable. It explains whether the classifier can be used for automatic enforcement, assisted triage, or monitoring only.

A weak submission lists attacks and screenshots but does not connect them to authority, controls, validation, or residual risk.
'''

DEBRIEF_GUIDE = r'''
# Toy Classifier Debrief Guide

Use this debrief after students run the four toy-classifier scripts. The goal is to connect a small synthetic exercise to real engineering decisions without overstating what the toy model proves.

## Debrief opening

Start with this statement:

> The toy classifier is not realistic because it is supposed to be realistic. It is useful because it makes four classes of ML security failure observable, repeatable, and discussable.

Then ask students to separate three ideas:

1. What happened in the toy lab.
2. What this represents in a real ML system.
3. What evidence would be needed before changing a production control.

## Attack-by-attack debrief

### Evasion

Observed failure: the input changed enough to cross the model boundary, while the synthetic intent stayed similar.

Real-world analogue: a fraud, spam, abuse, malware, or policy classifier sees changed features that preserve attacker intent.

Engineering decision: do not use a brittle classifier as the only hard enforcement gate unless there is fallback, monitoring, challenge flow, or review.

Good control language:

- Maintain adversarial and regression test sets.
- Track confidence and uncertainty.
- Route uncertain decisions to review or step-up controls.
- Monitor feature and phrase drift.
- Avoid using the classifier as the sole authorization mechanism.

### Poisoning

Observed failure: training labels were changed and the retrained model behaved differently.

Real-world analogue: feedback loops, analyst labels, customer reports, vendor datasets, or automated labeling pipelines can corrupt training data.

Engineering decision: training data needs provenance, review, versioning, and promotion controls.

Good control language:

- Version datasets and labels.
- Separate label submission from label approval.
- Compare retrained models against clean holdout sets.
- Require promotion evidence before deployment.
- Keep rollback paths for model and data versions.

### Extraction

Observed failure: repeated queries revealed rough boundary behavior.

Real-world analogue: externally exposed models can be probed for model theft, policy bypass, or sensitive behavior inference.

Engineering decision: the model interface is an attack surface.

Good control language:

- Rate-limit suspicious query patterns.
- Minimize unnecessary confidence or explanation output.
- Monitor query distributions.
- Use tenant-aware abuse detection.
- Avoid logging sensitive user content without controls.

### Output integrity

Observed failure: decision threshold tampering changed outcomes without changing the model.

Real-world analogue: configuration or policy-layer changes can bypass model validation.

Engineering decision: protect the whole decision path, not only the model artifact.

Good control language:

- Treat thresholds and feature transforms as controlled artifacts.
- Require review for threshold changes.
- Record threshold and config versions with each decision.
- Alert on unauthorized changes.
- Test the deployed decision path, not only the model file.

## Common student mistakes

| Mistake | How to redirect |
|---|---|
| Treating the toy attack as the whole lesson | Ask what production decision it represents. |
| Saying the fix is more training data | Ask how they prevent poisoned training data. |
| Saying the fix is hiding the model | Ask whether the exposed API still leaks behavior. |
| Focusing only on accuracy | Ask whether accuracy proves safe use as a hard gate. |
| Ignoring thresholds and policy | Ask what happens if config changes after model validation. |

## Closing question

Ask each group to answer:

> In what mode would you allow this classifier to operate: automatic enforcement, assisted triage, monitoring only, or not at all?

They must defend the answer with evidence from the lab, proposed controls, validation, and residual risk.
'''

APP_INSTRUCTOR_NOTES = r'''
# Instructor Notes for the Toy Classifier App

The app is intentionally deterministic and synthetic. Keep the framing tight: it is a teaching model for security reasoning, not a benchmark or realistic classifier.

## Expected commands

```bash
python train.py
python attacks/evasion.py
python attacks/poisoning.py
python attacks/extraction.py
python attacks/output_integrity.py
pytest
```

## Expected observations

| Script | Student should observe |
|---|---|
| `evasion.py` | A small perturbation changes the decision. |
| `poisoning.py` | A small number of poisoned labels changes retrained behavior. |
| `extraction.py` | Repeated queries reveal approximate decision behavior. |
| `output_integrity.py` | Threshold changes alter decisions without changing the model. |

## What not to teach

Do not teach this as a realistic phishing detector. Do not claim the perturbations are production bypasses. Do not imply the attacks are exhaustive. The lab is a controlled microscope for concepts.

## What to teach

Teach that the model is one part of a decision system. The security review must include data provenance, interface exposure, configuration integrity, monitoring, fallback, and residual risk.

## Reset guidance

The lab can be reset by deleting generated model artifacts and rerunning training:

```bash
rm -f model.pkl
python train.py
pytest
```

PowerShell:

```powershell
Remove-Item .\model.pkl -ErrorAction SilentlyContinue
python train.py
pytest
```
'''

APP_DEBRIEF = r'''
# Student Debrief: Toy Classifier Lab

After running the four scripts, answer these questions before writing your final memo.

## 1. Authority

What decision does the classifier make in the scenario you are reviewing? Is it automatic enforcement, assisted triage, monitoring, or advisory output?

## 2. Evidence

For each script, record one observed before/after result.

| Script | Before | After | Security meaning |
|---|---|---|---|
| evasion.py |  |  |  |
| poisoning.py |  |  |  |
| extraction.py |  |  |  |
| output_integrity.py |  |  |  |

## 3. Naive fix

Pick one naive fix and explain why it is insufficient.

Examples:

- Block the exact words from the evasion example.
- Retrain with more data without provenance.
- Hide confidence scores but keep unlimited query access.
- Validate the model file but ignore threshold configuration.

## 4. Better control

Describe one control that changes the security property. Include how you would validate it.

## 5. Residual risk

What risk remains after your control? What monitoring, fallback, review, or rollback should exist?

## 6. Decision

Would you allow this classifier to be used as a hard gate? Answer one:

- Yes, automatic enforcement is acceptable.
- Yes, but only with step-up or review.
- No, assisted triage only.
- No, monitoring only.
- No, do not deploy yet.

Defend the answer with evidence.
'''

STRONG_EXAMPLE = r'''
# Strong Example: Toy Classifier Lab Report

## Decision

I would not allow this classifier to operate as a hard enforcement gate. I would allow it only for assisted triage until robustness tests, data-provenance controls, query-abuse monitoring, and configuration-integrity controls are implemented and validated.

## Evidence

The evasion script showed that a small input perturbation can change the model decision while the synthetic intent remains similar. The poisoning script showed that changing a small number of labels can change behavior after retraining. The extraction script showed that repeated queries can approximate decision behavior. The output-integrity script showed that changing the threshold can alter outcomes without changing the trained model.

## Root cause

The classifier is being treated as if model accuracy proves the safety of the full decision path. It does not. The model, training data, exposed query interface, threshold, and deployment configuration each create separate control points.

## Naive fix that fails

Blocking the exact evasion tokens is not a durable control. It addresses one observed perturbation, not the property that small feature changes can move an input across the decision boundary. It also does nothing for poisoned labels, extraction, or threshold tampering.

## Recommended controls

1. Keep an adversarial regression set for known perturbation families and run it before promotion.
2. Require dataset and label provenance for training inputs.
3. Separate label submission from label approval.
4. Rate-limit and monitor repeated boundary-probing queries.
5. Treat the threshold and feature pipeline as versioned, reviewed deployment artifacts.
6. Route low-confidence or high-impact decisions to human review or step-up verification.

## Validation

Before promotion, run the clean test set, adversarial test set, poisoning regression scenario, and threshold-integrity check. In production, record the model version, dataset version, threshold version, and decision mode for each high-impact decision. Alert on unauthorized threshold changes and suspicious query patterns.

## Residual risk

Attackers may still discover perturbations not represented in the test set. Label-quality controls reduce poisoning risk but do not remove it. Query monitoring can miss slow probing. For that reason, the classifier should not be the only enforcement mechanism for high-impact decisions.
'''

WEAK_EXAMPLE = r'''
# Weak Example: Toy Classifier Lab Report

The model can be tricked by changing words. This means it is vulnerable. The fix is to train it with more data and block bad words. The poisoning script also showed problems, so the team should protect the dataset. Extraction can be stopped by hiding the model. The threshold should not be changed.

I recommend improving the model and adding guardrails. After that it should be safe to deploy.

## Why this is weak

This report lists observations but does not make a clear deployment decision. It does not explain what authority the classifier has, what security property changed, how the proposed controls would be validated, or what residual risk remains. It also recommends broad fixes like more data and guardrails without specifying provenance, approval, monitoring, fallback, or rollback.
'''

RUBRIC = r'''
# Toy Classifier Lab Rubric

Use this rubric for the Module 03 and Module 10 toy-classifier deliverable.

| Criterion | Strong | Adequate | Weak |
|---|---|---|---|
| Evidence | Uses observed before/after behavior from all four scripts. | Uses evidence from at least two scripts. | Mentions attacks without concrete observations. |
| Authority | Explains what decision the classifier is allowed to influence. | Mentions the decision context but not its impact. | Treats the model as isolated from the system. |
| Root cause | Separates input manipulation, poisoning, extraction, and output-integrity failure modes. | Describes some differences between attacks. | Treats all failures as generic model weakness. |
| Naive fix analysis | Explains why simple fixes fail. | Identifies at least one weak fix. | Recommends prompt-like or blacklist-style fixes without critique. |
| Controls | Proposes implementable controls for data, interface, config, and decision path. | Proposes controls for at least two areas. | Says to add guardrails, retrain, or monitor without detail. |
| Validation | Defines how to test that controls changed the security property. | Gives partial validation steps. | Gives no validation method. |
| Residual risk | Explains remaining uncertainty and fallback. | Mentions remaining risk. | Claims the risk is solved. |
| Decision | Makes a clear deployment or usage recommendation. | Gives a recommendation with limited support. | Gives no decision. |

## Minimum passing bar

A passing submission must include evidence, a control, validation, residual risk, and a deployment-mode decision.

## Recommended grading

- 4: Strong engineering decision memo.
- 3: Mostly complete, but one area needs sharper validation or residual-risk treatment.
- 2: Understands the attacks but does not translate them into a usable security decision.
- 1: Screenshot or attack-only submission.
'''

TEMPLATE = r'''
# Toy Classifier Lab Report Template

## 1. Deployment decision

Recommended mode:

- [ ] Automatic enforcement
- [ ] Assisted triage
- [ ] Monitoring only
- [ ] Do not deploy yet

Reason:

## 2. Classifier authority

What can the classifier influence?

## 3. Evidence table

| Script | Observed behavior | Security meaning |
|---|---|---|
| evasion.py |  |  |
| poisoning.py |  |  |
| extraction.py |  |  |
| output_integrity.py |  |  |

## 4. Root cause

What system assumption failed?

## 5. Naive fix that is insufficient

Describe one tempting fix and why it does not solve the security property.

## 6. Recommended controls

List implementable controls.

## 7. Validation plan

How would you prove the control changes the security property?

## 8. Residual risk

What remains after the control?

## 9. Monitoring, fallback, or rollback

What should happen when the model is uncertain, attacked, or wrong?
'''

MODULE_03 = r'''
# Toy Classifier Debrief for Module 03

Module 03 uses the toy-classifier app to turn OWASP ML categories into concrete evidence.

## Mapping

| Toy script | OWASP-style risk lesson | Student question |
|---|---|---|
| `evasion.py` | Input manipulation | What input changes cross the boundary? |
| `poisoning.py` | Data poisoning | What training-data controls failed? |
| `extraction.py` | Model theft and probing | What does query access reveal? |
| `output_integrity.py` | Output integrity | What changes the decision after model validation? |

## Debrief prompt

Do not ask only, "Which OWASP category is this?" Ask, "What evidence would make this a finding, and what control would change the security property?"

## Graded artifact

Students submit a short finding that includes:

1. observed behavior,
2. risk category,
3. root cause,
4. control,
5. validation,
6. residual risk.
'''

MODULE_10 = r'''
# Toy Classifier Debrief for Module 10

Module 10 uses the toy-classifier app to discuss robustness and the danger of hard-gate decisions.

## Core decision

The key question is not whether the model can be fooled. The key question is whether the system can safely depend on the model for the authority it has been given.

## Discussion prompts

1. Should the classifier automatically block a user, transaction, ticket, or message?
2. What happens when the classifier is uncertain?
3. What perturbations should be in the regression test set?
4. What data controls would reduce poisoning risk?
5. What monitoring would detect probing or drift?
6. What rollback path exists if the deployed model or threshold is wrong?

## Expected conclusion

For most high-impact decisions, the classifier should start as assisted triage or monitoring only. Automatic enforcement requires stronger evidence: robustness tests, fallback, threshold governance, abuse monitoring, and clear rollback.
'''

WORKFLOW_COURSE_QUALITY = r'''
name: Course Quality Checks

on:
  push:
    branches:
      - v1.1-dev-testable-labs
  pull_request:

jobs:
  brokenpilot-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install BrokenPilot dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r labs/brokenpilot/prototype-app/requirements.txt
      - name: Run BrokenPilot tests
        working-directory: labs/brokenpilot/prototype-app
        run: pytest

  toy-classifier-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install toy classifier dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r labs/toy-ml-attacks/toy-classifier-app/requirements-dev.txt
      - name: Run toy classifier tests
        working-directory: labs/toy-ml-attacks/toy-classifier-app
        run: pytest
'''

DEPLOY_DOCS = r'''
name: Deploy MkDocs site

on:
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install docs dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Generate MkDocs source
        run: python scripts/sync_mkdocs_content.py
      - name: Build MkDocs site in development mode
        run: mkdocs build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
'''


def main() -> None:
    write("instructor/toy-classifier-facilitation-guide.md", INSTRUCTOR_GUIDE)
    write("instructor/toy-classifier-debrief-guide.md", DEBRIEF_GUIDE)
    write("labs/toy-ml-attacks/toy-classifier-app/INSTRUCTOR_NOTES.md", APP_INSTRUCTOR_NOTES)
    write("labs/toy-ml-attacks/toy-classifier-app/DEBRIEF_GUIDE.md", APP_DEBRIEF)
    write("labs/toy-ml-attacks/toy-classifier-app/worked-examples/strong-toy-classifier-lab-report.md", STRONG_EXAMPLE)
    write("labs/toy-ml-attacks/toy-classifier-app/worked-examples/weak-toy-classifier-lab-report.md", WEAK_EXAMPLE)
    write("assessments/toy-classifier-lab-rubric.md", RUBRIC)
    write("course-templates/toy-classifier-lab-report-template.md", TEMPLATE)
    write("modules/03-owasp-ml-top-10/toy-classifier-debrief.md", MODULE_03)
    write("modules/10-adversarial-ml-robustness/toy-classifier-debrief.md", MODULE_10)
    write(".github/workflows/course-quality.yml", WORKFLOW_COURSE_QUALITY)
    write(".github/workflows/deploy-docs.yml", DEPLOY_DOCS)
    write("release-notes/v1.1-dev-toy-classifier-instructor-debrief.md", """
# v1.1-dev Toy Classifier Instructor Debrief

Adds instructor guidance, student debrief material, grading rubric, report template, strong and weak examples, and module-specific debrief notes for the toy-classifier lab. Also relaxes development workflows so MkDocs strict cleanup waits until content is frozen while runnable lab tests continue to run in CI.
""")

    append_once("labs/toy-ml-attacks/toy-classifier-app/README.md", "toy-classifier-instructor-debrief", """
## Instructor and debrief resources

- `INSTRUCTOR_NOTES.md` gives expected observations and reset guidance.
- `DEBRIEF_GUIDE.md` gives student reflection prompts after running the four scripts.
- `worked-examples/strong-toy-classifier-lab-report.md` shows a decision-grade report.
- `worked-examples/weak-toy-classifier-lab-report.md` shows a weak attack-only report.
""")
    append_once("labs/toy-ml-attacks/README.md", "toy-classifier-instructor-debrief", """
## Toy-classifier teaching resources

The toy-classifier app now has instructor notes, a student debrief, strong and weak examples, and a grading rubric. Use these materials to keep the lab focused on engineering decisions rather than attack novelty.
""")
    append_once("modules/03-owasp-ml-top-10/README.md", "toy-classifier-debrief-link", """
## Toy-classifier debrief

Use `toy-classifier-debrief.md` to connect the toy-classifier scripts to OWASP ML risk categories and finding quality.
""")
    append_once("modules/10-adversarial-ml-robustness/README.md", "toy-classifier-debrief-link", """
## Toy-classifier debrief

Use `toy-classifier-debrief.md` to frame evasion, poisoning, extraction, and output-integrity behavior around the hard-gate deployment decision.
""")
    append_once("CLEANUP_BEFORE_RELEASE.md", "toy-classifier-instructor-debrief-cleanup", """
## Toy-classifier package cleanup reminder

Before release, keep the durable toy-classifier instructor and debrief docs, but remove temporary apply/check scripts after their changes are committed. Re-enable strict MkDocs and broader release gates only after content and lab paths stop moving.
""")

    print("\nApplied toy-classifier instructor and debrief package.")


if __name__ == "__main__":
    main()
