# Lab — Classical ML Attack Scenarios

## Purpose

Use safe toy scenarios to practice the OWASP Machine Learning Security Top 10.

This lab is intentionally designed for controlled training environments. Do not apply these techniques against real third-party systems or production APIs.

## Lab modes

This lab can be run in two modes:

1. **Tabletop mode:** no code; students reason through attack paths and mitigations.
2. **Toy-code mode:** students use a local toy classifier to observe how small changes in data or input can change behavior.

## Scenario 1 — Spam classifier evasion

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

## Scenario 2 — Fraud model poisoning

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

## Scenario 3 — Model extraction through excessive querying

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

## Scenario 4 — Output integrity failure

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

## Suggested toy-code extension

In a local notebook, students can implement a tiny classifier using a small synthetic dataset.

Suggested safe exercises:

- Train a spam/not-spam classifier on toy messages.
- Change a few words and observe prediction changes.
- Flip a small number of labels and observe behavior changes.
- Compare predictions before and after poisoning.

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
