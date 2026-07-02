# AI Privacy Control Checklist

Use this as a compact review checklist for AI systems.

## Data minimization

- [ ] Collect only necessary data.
- [ ] Avoid unnecessary free text.
- [ ] Minimize retrieved context.
- [ ] Minimize tool output sent to the model.
- [ ] Avoid storing full prompts by default.

## Sensitive data handling

- [ ] Classify prompts and completions.
- [ ] Detect PII and secrets where appropriate.
- [ ] Redact or mask before storage where possible.
- [ ] Encrypt sensitive stores.
- [ ] Restrict access to logs and traces.

## RAG and embeddings

- [ ] Preserve source ACLs.
- [ ] Enforce retrieval authorization server-side.
- [ ] Separate or strongly filter tenants.
- [ ] Test cross-tenant retrieval.
- [ ] Propagate deletion to indexes.

## Model privacy

- [ ] Assess membership inference risk.
- [ ] Assess model inversion risk.
- [ ] Assess training data extraction risk.
- [ ] Limit unnecessary confidence or explanation detail.
- [ ] Monitor repeated query abuse.

## Agent memory

- [ ] Scope memory to user/session/purpose.
- [ ] Store provenance.
- [ ] Set expiry.
- [ ] Provide deletion path.
- [ ] Prevent cross-user memory reuse.

## Logs, traces, and feedback

- [ ] Define retention periods.
- [ ] Limit who can access logs.
- [ ] Audit access.
- [ ] Govern feedback reuse.
- [ ] Exclude sensitive feedback from training unless approved.

## Governance

- [ ] Privacy owner identified.
- [ ] Release gate includes privacy review.
- [ ] Residual risk accepted by owner.
- [ ] Reassessment triggers defined.
- [ ] Incident response covers AI data exposure.
