# Module 09 Student Handout  -  Privacy Attacks and Data Protection

## Core idea

AI privacy risk is a system problem.

Sensitive data can appear in places that traditional application reviews may miss:

- prompts;
- completions;
- retrieved context;
- embeddings;
- vector databases;
- model traces;
- tool outputs;
- logs;
- memory;
- feedback loops;
- evaluation datasets;
- training datasets;
- exported reports.

## Key terms

| Term | Meaning |
|---|---|
| Sensitive data | Data that can harm a person, organization, or group if exposed or misused. |
| Membership inference | Inferring whether a record or person was part of a model's training data. |
| Model inversion | Reconstructing sensitive attributes or representative samples from model behavior. |
| Training data extraction | Getting a model to reveal memorized training content. |
| Prompt leakage | Exposure of sensitive user input or system context. |
| Embedding leakage | Exposure or inference through vector representations or semantic search. |
| Cross-tenant retrieval | One tenant or user retrieving another tenant's data. |
| Memory leakage | Sensitive information stored and reused by an agent or assistant without proper controls. |

## What to look for

When reviewing an AI system, ask:

1. What sensitive data is collected?
2. What sensitive data is generated?
3. What sensitive data is embedded?
4. What sensitive data is logged?
5. What sensitive data is retained?
6. What sensitive data is used for feedback or retraining?
7. What sensitive data can be inferred?
8. What sensitive data can be retrieved by the wrong user?
9. What sensitive data can the model expose in output?
10. What sensitive data can an agent store in memory?

## Privacy attack surfaces

| Surface | Example risk |
|---|---|
| Training data | Private records used without minimization. |
| Model output | Memorized or inferred private data is revealed. |
| Prompt store | Users paste secrets or personal data. |
| Vector DB | Sensitive chunks retrievable across users. |
| Logs | Full prompts, retrieved context, and tool outputs are retained. |
| Agent memory | Private data persists across sessions. |
| Feedback | Sensitive corrections become training data. |
| Evaluation | Sensitive examples copied into test sets. |
| Monitoring | Debug traces include private context. |

## Privacy controls

| Control | Purpose |
|---|---|
| Data minimization | Reduce what can leak. |
| Purpose limitation | Prevent secondary use outside the original reason. |
| Classification | Identify sensitive data early. |
| Redaction/masking | Remove or reduce sensitive data before storage or model use. |
| Retrieval authorization | Ensure users can retrieve only what they are allowed to see. |
| Tenant isolation | Prevent cross-customer or cross-user leakage. |
| Retention limits | Avoid keeping sensitive prompts and logs forever. |
| Deletion propagation | Remove data from indexes, caches, logs where appropriate. |
| Restricted log access | Prevent operators from browsing sensitive prompts. |
| Privacy testing | Detect inference, extraction, and retrieval exposure. |
| Auditability | Show who accessed what and why. |

## Good design pattern

```text
classify input
  -> minimize data
  -> check policy
  -> retrieve only authorized chunks
  -> send minimal context to model
  -> check output
  -> log safely
  -> apply retention and deletion rules
```

## Bad design pattern

```text
store all prompts forever
  -> embed every document without ACL metadata
  -> retrieve globally
  -> send full chunks to the model
  -> log prompt + context + answer
  -> reuse feedback for training without review
```

## Deliverable

For the exercise, produce a privacy risk assessment with:

1. Sensitive data inventory.
2. Data-flow summary.
3. Privacy abuse cases.
4. Attack paths.
5. Control gaps.
6. Recommended mitigations.
7. Residual risk statement.
