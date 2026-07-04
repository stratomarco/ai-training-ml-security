# Lab  -  Classical ML Attack Scenarios

## Purpose

Use safe toy scenarios to practice the OWASP Machine Learning Security Top 10.

This lab is intentionally designed for controlled training environments. Do not apply these techniques against real third-party systems or production APIs.

## Lab modes

This lab can be run in two modes:

1. **Tabletop mode:** no code; students reason through attack paths and mitigations.
2. **Toy-code mode:** students use a local toy classifier to observe how small changes in data or input can change behavior.

## Scenario 1  -  Spam classifier evasion

### System

A local toy classifier labels messages as `spam` or `not_spam`.

### Attack concept

The attacker modifies message wording to bypass the classifier.

### OWASP category

- Primary: ML01 Input Manipulation
- Secondary: ML09 Output Integrity if downstream handling is weak

### Student tasks

1. Identify which parts of the input the attacker controls.
2. Describe how an attacker might change the input while preserving malicious intent.
3. Propose validation and detection controls.
4. Explain why this should not rely only on the ML model.

### Defensive discussion

Useful controls include:

- Sender reputation
- URL analysis
- Attachment sandboxing
- User reporting
- Message similarity clustering
- Rate limits
- Human review for suspicious cases

## Scenario 2  -  Fraud model poisoning

### System

A toy fraud model is periodically retrained using transaction history and analyst feedback.

### Attack concept

Attackers influence feedback or transaction patterns so the retrained model becomes less sensitive to their behavior.

### OWASP category

- Primary: ML02 Data Poisoning
- Secondary: ML08 Model Skewing

### Student tasks

1. Identify the feedback loop.
2. Identify where poisoned data could enter.
3. Propose provenance and review controls.
4. Define a rollback plan.

### Defensive discussion

Useful controls include:

- Data source trust scoring
- Label review
- Outlier detection
- Canary evaluation sets
- Dataset versioning
- Model behavior comparison before deployment
- Rollback to known-good model

## Scenario 3  -  Model extraction through excessive querying

### System

A toy model API returns classification labels and confidence scores.

### Attack concept

A user repeatedly queries the model to approximate decision boundaries.

### OWASP category

- Primary: ML05 Model Theft
- Secondary: ML03 Model Inversion or ML04 Membership Inference depending on data sensitivity

### Student tasks

1. Identify what the API exposes.
2. Explain why confidence scores may increase risk.
3. Propose monitoring and throttling controls.
4. Decide whether output minimization would reduce usability.

### Defensive discussion

Useful controls include:

- Authentication
- Rate limits
- Query anomaly detection
- Output minimization
- Abuse monitoring
- Terms of use and enforcement
- Model watermarking where appropriate

## Scenario 4  -  Output integrity failure

### System

A model produces a risk score. A downstream script converts the score into `approve`, `review`, or `decline`.

### Attack concept

The attacker changes the threshold or post-processing logic rather than attacking the model itself.

### OWASP category

- Primary: ML09 Output Integrity Attack

### Student tasks

1. Identify where the model output is transformed.
2. Identify who can change thresholds.
3. Propose change control and audit logging.
4. Explain how this differs from attacking the model.

### Defensive discussion

Useful controls include:

- Access control for thresholds
- Separation of duties
- Immutable deployment configuration
- Audit logs
- Change approval
- Integrity checks
- Runtime monitoring

## Current self-study mode

Until the dedicated toy classifier app is added, this lab is a tabletop exercise.

Do not tell students that a dataset or classifier is already provided. Students may either stay in tabletop mode or create a small synthetic dataset with this schema:

```json
{
  "id": "msg-001",
  "text": "fake training message using synthetic words only",
  "label": "spam"
}
```

Allowed labels for self-created data:

- `spam`
- `not_spam`

Safe exercises:

- train a local classifier on synthetic messages;
- change a few synthetic words and observe prediction changes;
- flip a small number of labels and observe behavior changes;
- compare predictions before and after poisoning.

The planned `labs/toy-ml-attacks/toy-classifier-app/` will replace this section with concrete scripts and a shipped dataset.

Keep this local and synthetic. The goal is conceptual understanding, not weaponization.

## Deliverable

Each group submits:

1. Chosen scenario.
2. OWASP ML mapping.
3. Attack path.
4. Impact.
5. Preventive controls.
6. Detective controls.
7. Recovery controls.
8. Residual risk.
9. One engineering trade-off.

## Instructor solution themes

Strong answers usually include:

- Clear attacker control.
- Lifecycle-stage mapping.
- Non-model controls.
- Monitoring and incident response.
- Honest residual risk.

Weak answers usually over-rely on:

- “Use more training data.”
- “Use a better model.”
- “Block bad inputs.”
- “Retrain more often.”

Push students to explain exactly how a control prevents, detects, or recovers from the attack.

<!-- toy-classifier-runnable-path -->

## Runnable path: toy-classifier app

Use the shipped app instead of inventing a dataset:

```powershell
cd labs/toy-ml-attacks/toy-classifier-app
python -m pip install -r requirements-dev.txt
python train.py
python attacks/evasion.py
python attacks/poisoning.py
python attacks/extraction.py
python attacks/output_integrity.py
pytest
```

macOS/Linux uses the same commands with `/` path separators.

Student deliverable: for each script, record the before/after output, identify the changed security property, propose one implementable control, and state residual risk.

## Round 3 correction: evasion must preserve intent

Use `toy-classifier-app/attacks/evasion.py` as the runnable evasion example. The corrected script keeps the malicious core message intact and adds benign-looking context until the model decision flips. Do not describe evasion as comparing a phishing message with an unrelated safe message; that teaches the wrong concept.
