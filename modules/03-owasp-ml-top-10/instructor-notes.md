# Module 03  -  Instructor Notes

## Teaching intent

This module should make students comfortable with classical ML security before they encounter LLM-specific issues.

The risk in this module is that students may treat OWASP ML Top 10 as a memorization exercise. Avoid that. The purpose is not to recite ten names. The purpose is to understand the lifecycle stages where attackers can influence ML behavior.

Keep returning to this question:

> What can the attacker influence, and what decision does the model influence?

## Suggested flow

### 1. Start with a non-LLM example

Use fraud detection, spam filtering, or intrusion detection.

Ask:

- What is the model deciding?
- Who benefits from a wrong decision?
- Who can influence the input?
- Who can influence the data used for future training?
- Who can query the model?
- Who can access the artifact?

This immediately grounds the discussion in security engineering.

### 2. Introduce OWASP ML Top 10 as a map

Present the ten categories quickly, then group them:

- Input-time attacks
- Training/data attacks
- Privacy attacks
- Model extraction/IP attacks
- Supply chain attacks
- Output/decision integrity attacks

This is easier than teaching them as ten isolated items.

### 3. Use the lifecycle diagram

Draw this repeatedly:

```text
Data → Labels → Features → Training → Evaluation → Registry → Deployment → Inference → Monitoring → Feedback
```

Ask where each OWASP category appears.

Important nuance: some categories appear in multiple places. For example, supply chain risk can affect dependencies, datasets, model artifacts, containers, notebooks, or registries.

### 4. Connect back to classic security

Examples:

- Data poisoning is a data integrity problem.
- Model theft is an access-control and abuse-monitoring problem.
- Model inversion and membership inference are privacy problems.
- Output integrity is a decision pipeline integrity problem.
- Model poisoning is an artifact integrity and training-process problem.
- Model skewing is monitoring and feedback-loop integrity.

This reinforces the course philosophy: ML Security extends security engineering; it does not replace it.

## Instructor talking points by category

### ML01  -  Input Manipulation Attack

Explain this as inference-time manipulation. The attacker does not need to compromise the model. They only need to craft an input that causes a useful misclassification.

Use examples:

- Slightly edited spam message.
- Changed transaction fields.
- Modified malware features.
- Image perturbation.

Avoid going too deep into math. The goal is practitioner understanding.

Key point:

> The input is attacker-controlled, but the decision may be trusted by the business.

### ML02  -  Data Poisoning Attack

Explain that training data is part of the system's behavior. Poisoning can be obvious or subtle.

Use examples:

- Fake user feedback.
- Manipulated labels.
- Injected training samples.
- Bad records entering through a weak ingestion pipeline.

Key point:

> If you do not know where your data came from, you do not know why your model behaves the way it does.

### ML03  -  Model Inversion Attack

Explain as privacy leakage through model behavior.

Students may confuse inversion with model theft. Clarify:

- Model theft targets the model.
- Model inversion targets sensitive information represented in or inferred from the model.

Key point:

> Outputs, confidence scores, and repeated queries may leak more than intended.

### ML04  -  Membership Inference Attack

Explain that training membership can be sensitive even if the record itself is not revealed.

Example:

- A health model trained on patients with a specific condition.
- An internal HR model trained on disciplinary cases.

Key point:

> The fact that a person was in the dataset can itself be sensitive.

### ML05  -  Model Theft

Split into two forms:

1. Direct theft of the artifact.
2. Approximation through queries.

Connect direct theft to cloud security and registry controls. Connect extraction to API abuse monitoring, rate limiting, and output minimization.

Key point:

> Model IP is an asset, and query access can become an extraction channel.

### ML06  -  AI Supply Chain Attacks

Emphasize that ML supply chain is bigger than package dependencies.

It includes:

- Datasets
- Labeling processes
- Notebooks
- Training scripts
- Model artifacts
- Registries
- Containers
- Evaluation tools
- Third-party base models

Key point:

> Treat models and datasets as build artifacts with provenance, ownership, and integrity requirements.

### ML07  -  Transfer Learning Attack

Explain this through inherited risk.

A model reused from a third party may carry:

- Backdoors
- Unsafe behavior
- Dataset issues
- Licensing issues
- Unclear provenance
- Weak evaluation for the new context

Key point:

> Transfer learning transfers capability and risk.

### ML08  -  Model Skewing

Explain this as gradual manipulation through production behavior, especially feedback loops.

Examples:

- Fake accounts shaping recommendations.
- Attackers repeatedly marking something as benign.
- Coordinated manipulation of user feedback.

Key point:

> The feedback loop is an attack surface.

### ML09  -  Output Integrity Attack

This is often easier for AppSec students to understand.

The attacker may not attack the model. They may attack:

- The output parser.
- The threshold logic.
- The business decision wrapper.
- The explanation layer.
- The report or UI.

Key point:

> The model output is only one part of the decision pipeline.

### ML10  -  Model Poisoning

Distinguish from ML02:

- Data poisoning corrupts data used for training.
- Model poisoning corrupts the model or its learned behavior directly.

In practice these can overlap.

Key point:

> The deployed artifact must be trusted, verifiable, and recoverable.

## Common student misconceptions

### Misconception 1: “This only matters for image classifiers.”

Correction: These risks also affect fraud, spam, recommender systems, risk scoring, abuse detection, and operational decision systems.

### Misconception 2: “Adversarial ML is only academic.”

Correction: Some attack forms are academic or difficult in specific settings, but the underlying problem  -  adversarial input and data manipulation  -  is practical.

### Misconception 3: “Better model accuracy solves it.”

Correction: Accuracy on a test set does not measure adversarial robustness, privacy leakage, supply chain integrity, or access control.

### Misconception 4: “The ML team owns all of this.”

Correction: ML security is shared across AppSec, platform, cloud, data engineering, ML engineering, privacy, and product teams.

### Misconception 5: “The model is the only asset.”

Correction: Datasets, labels, feature pipelines, evaluation sets, model cards, prompts, notebooks, registries, secrets, outputs, and decisions are also assets.

## Lab facilitation

The lab can be run as a tabletop without code or as a toy coding exercise.

Recommended tabletop systems:

- Spam classifier
- Fraud detection model
- Loan-risk scoring model
- Support-ticket classifier
- Product recommender

Ask each group to choose one system and fill out:

1. Business decision.
2. Attacker goal.
3. OWASP ML category.
4. Lifecycle stage.
5. Attack path.
6. Impact.
7. Detection.
8. Mitigation.
9. Residual risk.

## Scoring guidance

A strong answer should include:

- A specific attacker.
- A specific model-assisted decision.
- A clear trust boundary.
- A realistic attack path.
- At least one preventive control.
- At least one detective control.
- At least one recovery control.
- A trade-off discussion.

A weak answer usually says only:

- “Use better data.”
- “Use a more secure model.”
- “Add monitoring.”
- “Retrain frequently.”

Push students to explain how the control works and what risk remains.

## Instructor close

End with this:

> The OWASP ML Top 10 is not a checklist that makes a model secure. It is a map of ways attackers can influence the ML lifecycle. The security job is to turn that map into engineering controls, monitoring, and risk decisions.
