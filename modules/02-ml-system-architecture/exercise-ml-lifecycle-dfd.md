# Exercise  -  ML Lifecycle Data-Flow Diagram

## Scenario: LoanAssist ML

Your company is building **LoanAssist ML**, an internal loan triage system.

LoanAssist does not automatically approve or reject loans. It scores applications and sends higher-risk or unclear applications to manual review.

The company later adds an LLM assistant that helps internal analysts understand why an application received a certain score. The assistant retrieves supporting information from internal documents and customer records using a vector database.

## System description

LoanAssist uses the following data sources:

1. Customer loan application forms submitted through a web portal.
2. Uploaded documents from applicants, such as payslips and bank statements.
3. Third-party credit bureau data.
4. Historical loan repayment outcomes.
5. Internal analyst notes from previous manual reviews.
6. Customer support notes.
7. Fraud investigation outcomes.
8. User feedback from analysts after reviewing model explanations.

The ML pipeline:

1. Raw data is stored in a data lake.
2. A data preparation job removes incomplete records.
3. A labeling job uses historical outcomes as training labels.
4. A feature pipeline creates features for income stability, debt ratio, repayment history, and document consistency.
5. A training pipeline runs weekly.
6. The model is evaluated against a holdout dataset.
7. Approved model artifacts are pushed to a model registry.
8. The production inference API serves risk scores to internal analysts.
9. Analysts see a score, a short explanation, and retrieved supporting context.
10. Analyst feedback may be used in future model updates.

The LLM assistant:

1. Receives analyst questions.
2. Retrieves customer-related context from a vector database.
3. Generates a natural-language explanation of the model score.
4. Can summarize uploaded documents.
5. Can create a manual-review note.
6. Cannot approve or reject loans directly.

## Assumptions

Use these assumptions unless your instructor changes them:

- The system is internal but connected to external data sources.
- Applicants are external users and may be malicious.
- Analysts are authenticated employees with different access levels.
- The credit bureau is trusted but still external.
- The model is trained internally.
- The LLM is accessed through an external model provider API.
- The vector database stores embeddings of internal documents and customer records.
- Analyst feedback can eventually influence future training data.

## Student tasks

### Task 1  -  Draw the lifecycle DFD

Draw the system as a data-flow diagram.

Include at least:

- External applicants
- Web portal
- Uploaded documents
- Third-party credit bureau
- Raw data lake
- Labeling process
- Feature pipeline
- Training pipeline
- Evaluation gate
- Model registry
- Production inference API
- Analyst interface
- LLM provider
- Vector database
- Feedback loop
- Logs and monitoring

### Task 2  -  Identify assets

List at least ten assets.

Examples:

- Applicant PII
- Uploaded documents
- Historical repayment data
- Analyst notes
- Training dataset
- Feature pipeline code
- Model artifact
- Evaluation dataset
- Model registry
- Inference API
- Vector database
- Prompt templates
- API credentials
- Logs

### Task 3  -  Identify trust boundaries

Mark trust boundaries on your diagram.

Look for boundaries between:

- External applicant and company system
- Third-party data provider and internal data lake
- Data lake and training pipeline
- Training pipeline and model registry
- Model registry and production deployment
- Analyst user and inference API
- Internal system and external LLM provider
- Retrieval system and vector database
- Feedback loop and future training data

### Task 4  -  Identify attack paths

Find at least eight attack paths.

Use this format:

```text
Attack path:
Attacker:
Entry point:
Target asset:
Impact:
Relevant lifecycle stage:
```

Example:

```text
Attack path: Applicant uploads manipulated documents to influence risk score.
Attacker: External applicant.
Entry point: Web portal document upload.
Target asset: Model input and feature extraction.
Impact: Lower-risk score for fraudulent application.
Relevant lifecycle stage: Inference / feature processing.
```

### Task 5  -  Map controls

For each attack path, propose at least one control.

Use this format:

```text
Control:
Where enforced:
Prevent / detect / respond:
Tradeoff:
```

Example:

```text
Control: Validate uploaded document metadata and run fraud checks before feature extraction.
Where enforced: Document ingestion pipeline.
Prevent / detect / respond: Prevent and detect.
Tradeoff: More processing latency and potential false positives.
```

### Task 6  -  Residual risk statement

Write a short residual risk statement.

Use this structure:

```text
Even with the proposed controls, LoanAssist ML still has residual risk from ____.
The most important remaining risks are ____.
The organization should accept / reduce / transfer / avoid this risk by ____.
```

## Hints

Think about these questions:

- Can applicants influence training data?
- Can applicants influence inference-time input?
- Can analyst feedback poison future updates?
- Can the LLM reveal information the analyst should not see?
- Can the vector database retrieve cross-customer or cross-tenant records?
- Can a malicious document influence an LLM explanation?
- Can the model artifact be replaced or tampered with?
- Can repeated API queries reveal model behavior?
- Can logs leak sensitive applicant information?
- Can the system be rolled back if a bad model is deployed?

## Expected deliverable

Your group should submit:

1. Lifecycle DFD.
2. Asset list.
3. Trust-boundary list.
4. At least eight attack paths.
5. At least eight controls.
6. Residual risk statement.

## Instructor-only expected findings

Do not show this section to students before the exercise.

Strong submissions often include these findings:

| Area | Expected risk |
|---|---|
| Applicant input | Malicious applications and uploaded documents influence inference |
| Uploaded documents | Malicious content can affect document summarization or feature extraction |
| Third-party data | External provider quality and integrity risk |
| Historical outcomes | Training labels may encode bias, errors, or fraud history gaps |
| Analyst notes | Notes may contain sensitive data, speculation, or incorrect assumptions |
| Labeling | Historical labels treated as ground truth without review |
| Feature pipeline | Features may leak protected attributes or be easy to manipulate |
| Training pipeline | Compromised notebook, dependency, or credential can alter model |
| Evaluation | Test set may not include adversarial or edge cases |
| Model registry | Weak access control can allow unauthorized model replacement |
| Inference API | Authenticated users may probe or extract model behavior |
| LLM provider | Sensitive context sent outside the organization |
| Vector DB | Retrieval may bypass per-analyst authorization |
| Prompt construction | Retrieved malicious content can change explanation behavior |
| Feedback loop | Analyst feedback can poison future training if trusted automatically |
| Logs | Prompts, outputs, and documents may create privacy exposure |
| Monitoring | Accuracy monitoring may miss security abuse |
| Rollback | Lack of reproducibility can make incident response difficult |

## Example residual risk

```text
Even with the proposed controls, LoanAssist ML still has residual risk from adversarial applicants, imperfect third-party data, analyst overreliance, and feedback-loop manipulation. The most important remaining risks are unauthorized retrieval of sensitive applicant data and model behavior degradation caused by poisoned feedback. The organization should reduce this risk through per-user retrieval authorization, feedback review gates, abuse monitoring, model rollback capability, and periodic adversarial testing.
```
