# Module 09  -  Privacy Attacks and Data Protection

## Purpose

Teach privacy failure modes in ML, LLM, RAG, and agent systems and connect them to practical engineering controls.

This module is not a legal-compliance lecture. It is a security engineering module about how AI systems can expose, infer, reconstruct, retain, or misuse sensitive information.

## Key message

AI systems often create new paths for old privacy failures.

Privacy risk is not limited to the model. It can appear in the dataset, training pipeline, model behavior, prompts, embeddings, vector database, logs, evaluation data, monitoring system, feedback loop, support tools, and agent memory.

## Learning objectives

By the end of this module, students should be able to:

1. Explain membership inference, model inversion, training data extraction, prompt leakage, log leakage, embedding leakage, and cross-tenant retrieval exposure.
2. Identify where sensitive data appears across the ML lifecycle.
3. Distinguish confidentiality risk from privacy risk.
4. Threat model privacy attacks against ML, LLM, RAG, and agent systems.
5. Evaluate whether retrieval authorization is enforced before context reaches the model.
6. Design data minimization, retention, redaction, access control, and audit controls for AI systems.
7. Explain why privacy controls must be placed outside the model, not only inside prompts.
8. Produce a privacy risk assessment for an AI-enabled application.

## Topics

- Privacy threat modeling for AI systems
- Sensitive data classification
- Training data exposure
- Membership inference
- Model inversion
- Training data extraction
- Prompt and completion leakage
- Log and telemetry leakage
- Embedding and vector database leakage
- Cross-tenant retrieval exposure
- Agent memory leakage
- Data minimization
- Purpose limitation
- Retention and deletion
- PII redaction and masking
- Differential privacy, where appropriate
- Tenant isolation
- Retrieval authorization
- Privacy monitoring and auditability
- Residual privacy risk

## Security engineering connection

Classic privacy and security principles still apply:

- Least privilege
- Need-to-know access
- Data minimization
- Purpose limitation
- Complete mediation
- Secure defaults
- Defense in depth
- Strong tenant isolation
- Secure logging
- Cryptographic protection
- Auditability
- Retention limits
- Safe deletion
- Incident response

The AI-specific challenge is that sensitive information may be transformed, summarized, embedded, memorized, inferred, or exposed through model-mediated behavior.

## Reference architecture

```text
user / attacker
  |
  v
AI application interface
  |
  +-- prompt and conversation store
  +-- model gateway
  +-- policy and authorization layer
  +-- retrieval service
  |     +-- embedding service
  |     +-- vector database
  |     +-- source document store
  |
  +-- tool layer / agent memory
  +-- telemetry and audit logs
  +-- monitoring and feedback loop
```

Privacy review must cover every component, not only the model provider.

## Core failure patterns

| Failure pattern | Example | Root cause |
|---|---|---|
| Training data exposure | Model reveals memorized personal data | Sensitive data used without minimization or protection |
| Membership inference | Attacker infers whether a person was in training data | Overfitting, excessive confidence exposure, weak privacy testing |
| Model inversion | Attacker reconstructs sensitive attributes or representative records | Model reveals too much about learned relationships |
| Prompt leakage | Prompts contain secrets or personal data | No prompt data classification or input controls |
| Log leakage | Prompts/completions stored broadly | Logging without privacy design |
| Embedding leakage | Sensitive text embedded and retrievable | Vector DB treated as harmless metadata |
| Cross-tenant retrieval | User retrieves another tenant's records | Authorization performed after retrieval or only in the UI |
| Agent memory leakage | Agent stores private data and reuses it later | Memory lacks provenance, expiry, review, and access control |
| Feedback-loop leakage | User corrections become future training data | Feedback data not classified or governed |

## Lab

Students perform a privacy review of a fake HR or customer-support AI assistant. The system uses RAG over sensitive records and logs prompts for quality analysis. Students identify leakage paths, model privacy attacks, and design controls.

See:

- `labs/privacy-labs/brokenpilot-cross-tenant-leakage-lab.md`
- `labs/privacy-labs/privacy-leakage-cross-tenant-rag-lab.md`
- `labs/privacy-labs/membership-inference-model-inversion-tabletop.md`

## Deliverable

Students complete a privacy risk assessment using:

- `course-templates/privacy-risk-assessment-template.md`

The deliverable must include:

1. Sensitive data inventory.
2. Data-flow map.
3. Privacy abuse cases.
4. Likelihood and impact assessment.
5. Existing controls.
6. Recommended mitigations.
7. Residual risk statement.

## Instructor emphasis

Keep the module practical.

Students should leave understanding that privacy in AI systems is a system property. It is not solved by telling the model to “not reveal sensitive information.”

<!-- LAB_MODALITY_PRIVACY:START -->
## Lab modality note

Module 09 has two lab styles: BrokenPilot cross-tenant leakage is runnable and observable; membership inference and model inversion is a reasoning lab and should be graded with strong and weak anchors.
<!-- LAB_MODALITY_PRIVACY:END -->

<!-- lab-routing-content-pass:start -->

## Lab routing note

Module 09 combines a runnable BrokenPilot privacy leakage lab with reasoning labs for privacy attacks that should not be forced into a toy web app.

Primary graded deliverable: A privacy leakage review with evidence, impacted data class, violated boundary, remediation, validation, and residual logging/privacy risk.

See `lab-path.md` in this module and `labs/RUNNABLE_AND_REASONING_LAB_INDEX.md` for the full lab modality map.

<!-- lab-routing-content-pass:end -->
