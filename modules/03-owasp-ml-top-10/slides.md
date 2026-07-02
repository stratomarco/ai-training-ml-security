# Module 03  -  OWASP ML Security Top 10

## Slide 1  -  Title

# OWASP ML Security Top 10

Classical ML attacks before LLMs, RAG, and agents.

---

## Slide 2  -  Why this module exists

Before LLMs, ML systems were already used for:

- Fraud detection
- Spam and phishing detection
- Credit scoring
- Recommender systems
- Computer vision
- Intrusion detection
- Medical triage
- Risk scoring

These systems make or influence decisions.

If attackers can influence the model, they can influence the decision.

---

## Slide 3  -  Key message

# Accuracy is not security

A model can perform well on a benchmark and still fail under adversarial pressure.

Security asks different questions:

- Who can influence the input?
- Who can influence the training data?
- Who can query the model?
- Who can access the model artifact?
- Who can change post-processing logic?
- What happens when the model is wrong?

---

## Slide 4  -  OWASP ML Top 10 map

| Category | Short name |
|---|---|
| ML01 | Input manipulation |
| ML02 | Data poisoning |
| ML03 | Model inversion |
| ML04 | Membership inference |
| ML05 | Model theft |
| ML06 | AI supply chain attacks |
| ML07 | Transfer learning attacks |
| ML08 | Model skewing |
| ML09 | Output integrity attacks |
| ML10 | Model poisoning |

---

## Slide 5  -  Lifecycle view

```text
Data → Labels → Features → Training → Evaluation → Registry → Deployment → Inference → Monitoring → Feedback
```

The OWASP ML risks are easier to understand when mapped to lifecycle stages.

---

## Slide 6  -  ML01: Input Manipulation Attack

Attacker changes inference-time input to manipulate the model's prediction.

Examples:

- Modified phishing email bypasses classifier.
- Slight image changes alter computer vision result.
- Fraud transaction fields are tuned to avoid detection.
- Malware features are changed to evade an ML detector.

Security connection:

- Input validation
- Abuse-case testing
- Robustness testing
- Safe fallback behavior

---

## Slide 7  -  ML01: Defensive patterns

Useful controls:

- Input normalization
- Data quality checks
- Out-of-distribution detection
- Rate limiting
- Adversarial test cases
- Human review for high-impact decisions
- Defense in depth around the model decision

Important limitation:

No input filter makes an ML model fully robust.

---

## Slide 8  -  ML02: Data Poisoning Attack

Attacker corrupts training, labeling, or feedback data.

Examples:

- Fake reviews influence a recommender.
- Fraudsters create transactions that teach the model bad patterns.
- Malicious labels degrade classifier performance.
- User feedback loops are gamed.

Security connection:

- Data integrity
- Provenance
- Change review
- Monitoring
- Separation of duties

---

## Slide 9  -  ML02: Defensive patterns

Useful controls:

- Dataset provenance
- Source trust scoring
- Label review
- Anomaly detection in training data
- Versioned datasets
- Reproducible training
- Holdout validation
- Canary datasets
- Rollback capability

Key question:

Can we explain why model behavior changed?

---

## Slide 10  -  ML03: Model Inversion Attack

Attacker uses model outputs to infer sensitive features or representative training data.

Examples:

- Inferring sensitive attributes from prediction behavior.
- Reconstructing approximate training examples.
- Using confidence scores to learn private patterns.

Security connection:

- Privacy by design
- Output minimization
- Access control
- Rate limits

---

## Slide 11  -  ML04: Membership Inference Attack

Attacker tries to determine whether a specific record was in the training data.

Why it matters:

- Training membership can itself be sensitive.
- Example: was this patient in a disease dataset?
- Example: was this employee included in an internal investigation dataset?

Security connection:

- Data minimization
- Privacy testing
- Output minimization
- Differential privacy where appropriate

---

## Slide 12  -  ML05: Model Theft

Attacker steals the model artifact or approximates the model by querying it.

Examples:

- Downloading model weights from an exposed bucket.
- Extracting a substitute model through repeated API queries.
- Stealing proprietary feature engineering or thresholds.

Security connection:

- Access control
- API abuse prevention
- Secrets management
- Artifact protection
- Monitoring

---

## Slide 13  -  ML06: AI Supply Chain Attacks

The ML supply chain includes more than code.

It includes:

- Datasets
- Labels
- Notebooks
- Dependencies
- Containers
- Model files
- Adapters
- Evaluation scripts
- Registries
- Deployment pipelines

If any artifact is compromised, the model behavior may be compromised.

---

## Slide 14  -  ML07: Transfer Learning Attack

Transfer learning reuses a pretrained model as a starting point.

Risk appears when inherited behavior is unsafe:

- Backdoored base model
- Untrusted fine-tuning dataset
- Hidden trigger behavior
- License or provenance issues
- Model reused outside intended context

Security connection:

- Third-party risk
- Provenance
- Security review before reuse
- Fit-for-purpose validation

---

## Slide 15  -  ML08: Model Skewing

Attacker manipulates production inputs or feedback to gradually skew behavior.

Examples:

- Gaming recommender feedback.
- Manipulating abuse reports.
- Creating many fake interactions.
- Shaping feedback loops over time.

Security connection:

- Monitoring
- Abuse detection
- Feedback integrity
- Drift detection
- Anti-fraud controls

---

## Slide 16  -  ML09: Output Integrity Attack

Attacker tampers with the model result, explanation, post-processing, or downstream use of the output.

Examples:

- Changing a risk score after inference.
- Tampering with thresholds.
- Manipulating explanation text.
- Altering the decision wrapper around the model.

Security connection:

- Integrity protection
- Complete mediation
- Audit logs
- Secure pipelines
- Separation of duties

---

## Slide 17  -  ML10: Model Poisoning

Model poisoning targets the learned behavior or model artifact directly.

Examples:

- A backdoored model behaves normally except on a trigger.
- A model artifact is replaced in the registry.
- Training process is manipulated to embed unsafe behavior.

Security connection:

- Artifact signing
- Registry access control
- Reproducible builds
- Independent evaluation
- Rollback

---

## Slide 18  -  Grouping the risks

| Group | OWASP categories |
|---|---|
| Input-time attacks | ML01 |
| Training/data attacks | ML02, ML08, ML10 |
| Privacy attacks | ML03, ML04 |
| IP/extraction attacks | ML05 |
| Supply chain attacks | ML06, ML07 |
| Decision integrity attacks | ML09 |

This grouping helps students reason instead of memorize.

---

## Slide 19  -  Same system, different attackers

Example: fraud scoring model.

| Attacker | Goal | Relevant risks |
|---|---|---|
| Fraudster | Avoid detection | ML01, ML08 |
| Insider | Manipulate training data | ML02, ML10 |
| Competitor | Copy model | ML05 |
| Privacy attacker | Infer training membership | ML03, ML04 |
| Supply chain attacker | Replace artifact | ML06, ML10 |

---

## Slide 20  -  Mitigation pattern

Do not ask only:

> How do we make the model better?

Ask:

> How do we make the system resilient when the model is attacked, wrong, stale, stolen, or manipulated?

---

## Slide 21  -  Defense in depth for ML

Controls should exist around the model:

- Data provenance
- Dataset review
- Model registry controls
- Artifact signing
- Input validation
- Output integrity checks
- Query monitoring
- Rate limits
- Human review
- Rollback
- Incident response

---

## Slide 22  -  Lab setup

Scenario options:

- Spam classifier
- Fraud scoring model
- Image classifier
- Support-ticket classifier

Student tasks:

1. Choose one OWASP ML category.
2. Identify attacker control.
3. Explain the attack path.
4. Propose detection.
5. Propose mitigations.
6. State residual risk.

---

## Slide 23  -  What good looks like

A strong answer includes:

- Clear asset
- Clear attacker
- Clear trust boundary
- Clear lifecycle stage
- Clear business impact
- Practical mitigation
- Honest residual risk

---

## Slide 24  -  Key takeaway

# ML Security is lifecycle security

Protecting the model is not enough.

You must protect:

- Data
- Labels
- Features
- Training
- Artifacts
- APIs
- Outputs
- Feedback loops
- Decisions
