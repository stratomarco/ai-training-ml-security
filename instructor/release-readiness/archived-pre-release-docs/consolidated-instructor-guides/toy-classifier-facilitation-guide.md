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
