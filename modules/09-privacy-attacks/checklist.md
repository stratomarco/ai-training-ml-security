# Module 09 Checklist  -  AI Privacy and Data Protection

Use this checklist when reviewing ML, LLM, RAG, or agent systems that process sensitive data.

## Data inventory

- [ ] Sensitive data types are identified.
- [ ] Personal data is classified.
- [ ] Confidential business data is classified.
- [ ] Secrets and credentials are classified.
- [ ] Training data sensitivity is documented.
- [ ] Evaluation data sensitivity is documented.
- [ ] Prompt and completion sensitivity is documented.
- [ ] Retrieved context sensitivity is documented.
- [ ] Tool output sensitivity is documented.
- [ ] Memory and feedback sensitivity is documented.

## Data minimization

- [ ] The system collects only necessary data.
- [ ] Training data is minimized.
- [ ] Prompt context is minimized.
- [ ] Retrieved chunks are minimized.
- [ ] Tool results are minimized before reaching the model.
- [ ] Logs avoid storing full sensitive context by default.
- [ ] Feedback does not silently include sensitive data.

## Authorization and tenant isolation

- [ ] Source ACLs are preserved during ingestion.
- [ ] Chunks include user, role, tenant, purpose, and source metadata where needed.
- [ ] Retrieval authorization happens before context reaches the model.
- [ ] Cross-tenant retrieval tests exist.
- [ ] Role-based and purpose-based access are enforced.
- [ ] Admin/debug access to prompts and logs is restricted.
- [ ] Tool access follows least privilege.

## RAG and vector database privacy

- [ ] Vector DB is treated as a sensitive data store.
- [ ] Embedding indexes are separated by tenant or strongly filtered.
- [ ] Metadata filters are enforced server-side.
- [ ] Ingestion preserves deletion and retention metadata.
- [ ] Retrieval logs do not overexpose sensitive chunks.
- [ ] Citations do not reveal unauthorized metadata.
- [ ] Deleted source records are removed from indexes where required.

## Prompt, log, and trace governance

- [ ] Prompt logging is intentional and justified.
- [ ] Completion logging is intentional and justified.
- [ ] Retrieved context logging is minimized.
- [ ] Tool-result logging is minimized.
- [ ] Sensitive traces are access-controlled.
- [ ] Retention periods are defined.
- [ ] Deletion workflows exist.
- [ ] Incident response covers prompt/log exposure.

## Model privacy attacks

- [ ] Membership inference risk has been considered.
- [ ] Model inversion risk has been considered.
- [ ] Training data extraction risk has been considered.
- [ ] Output confidence and detail levels are reviewed.
- [ ] Repeated query abuse is monitored.
- [ ] Rate limits and anomaly detection exist.
- [ ] High-risk models receive privacy testing before release.

## Agent memory and feedback

- [ ] Memory has provenance.
- [ ] Memory has expiry.
- [ ] Memory has user visibility where appropriate.
- [ ] Memory can be deleted.
- [ ] Memory is not shared across users without policy.
- [ ] Feedback is classified before reuse.
- [ ] Fine-tuning/evaluation reuse requires approval.
- [ ] Sensitive feedback can be excluded or redacted.

## Output controls

- [ ] Output is checked for sensitive data in high-risk flows.
- [ ] The system avoids exposing raw retrieved context unnecessarily.
- [ ] Summaries do not reveal unauthorized personal details.
- [ ] The model is not used as the only privacy enforcement mechanism.
- [ ] Human review exists for high-risk disclosures.

## Residual risk

- [ ] Remaining privacy risks are documented.
- [ ] Business owner accepts residual risk.
- [ ] Privacy/security monitoring is defined.
- [ ] Review cadence is defined.
- [ ] Release criteria include privacy gates.
