# Module 08 Student Handout — Secure MLOps and AI Supply Chain

## Big idea

Secure MLOps is about protecting the path from raw data to production model behavior.

A production model is not just code. It is shaped by data, labels, features, training code, dependencies, containers, parameters, model artifacts, prompts, adapters, evaluation results, registry permissions, and deployment workflows.

## Core rule

> If an artifact can influence production model behavior, treat it as a security-relevant artifact.

## ML supply chain map

```text
data source
  -> dataset
  -> labels
  -> features
  -> training code
  -> dependencies
  -> training job
  -> model artifact
  -> evaluation
  -> model registry
  -> deployment
  -> inference
  -> monitoring
  -> feedback
  -> retraining
```

## Important artifacts

| Artifact | Why it matters |
|---|---|
| Dataset | Bad data can poison behavior or violate privacy. |
| Labels | Wrong or malicious labels can corrupt learning. |
| Features | Feature leakage or manipulation can create hidden failure modes. |
| Training code | Determines how the model is produced. |
| Dependencies | May introduce vulnerabilities or malicious behavior. |
| Container image | Carries runtime libraries, tools, and sometimes secrets. |
| Model artifact | Encodes behavior and may include unsafe serialized content. |
| Prompt template | Controls LLM behavior and tool use. |
| Adapter / LoRA | Can alter model behavior significantly. |
| Embedding/vector index | Determines what context is retrieved. |
| Evaluation set | Decides whether a model is accepted. |
| Registry metadata | Documents ownership, version, approval, and risk. |
| Monitoring feedback | May become future training input. |

## Common risks

| Risk | Example |
|---|---|
| Dataset poisoning | Attacker adds malicious examples to training data. |
| Label tampering | Insider changes labels to weaken detection. |
| Notebook leakage | API key stored in notebook output. |
| Dependency compromise | Training job installs malicious package. |
| Unsafe model loading | Model file format or loader executes code. |
| Registry abuse | User promotes unapproved model to production. |
| Missing provenance | No one knows which data/code built the model. |
| Weak evaluation | Model ships after passing only accuracy tests. |
| Feedback poisoning | User-submitted feedback enters retraining unchecked. |
| No rollback | Bad model cannot be quickly removed. |

## Questions to ask during review

### Data

- Where did the data come from?
- Who owns it?
- Is it licensed for this use?
- Does it contain sensitive data?
- Who can write to it?
- Is lineage tracked?
- Can bad records be removed?

### Code and dependencies

- Is training code reviewed?
- Are dependencies pinned?
- Are dependencies scanned?
- Are containers built from trusted images?
- Are secrets kept out of notebooks and logs?

### Model artifact

- Who built it?
- What data and code produced it?
- Is the artifact immutable?
- Is it hashed or signed?
- Does loading it execute code?
- Is it stored in an access-controlled registry?

### Evaluation and promotion

- What tests did it pass?
- Did it pass security and privacy tests?
- Who approved promotion?
- Is there a rollback plan?
- Is deployment logged?

### Monitoring

- What behavior is monitored?
- How are anomalies detected?
- Are prompts and outputs retained safely?
- Can feedback enter retraining?
- Is suspicious feedback quarantined?

## Secure pattern

```text
approved data
  + reviewed code
  + locked dependencies
  + controlled training job
  + provenance record
  + model artifact integrity
  + security/evaluation gates
  + registry approval
  + scoped deployment
  + monitoring
  + rollback
```

## Deliverable checklist

For the exercise, your final Secure MLOps review should include:

- architecture summary;
- artifact inventory;
- trust boundaries;
- dataset provenance review;
- dependency review;
- model artifact review;
- registry access-control review;
- promotion gate design;
- monitoring and rollback plan;
- risk register;
- residual risk statement.
