# Model Artifact Risk Review Template

## Artifact metadata

| Field | Value |
|---|---|
| Model name |  |
| Version |  |
| Artifact filename |  |
| Format |  |
| Owner |  |
| Uploaded by |  |
| Registry location |  |
| Hash |  |
| Signature/provenance |  |

## Origin

| Question | Answer |
|---|---|
| Which source code commit produced this artifact? |  |
| Which training pipeline produced it? |  |
| Which dataset versions were used? |  |
| Which feature set was used? |  |
| Which dependency lockfile was used? |  |
| Which container image digest was used? |  |
| Which training parameters were used? |  |

## Safe loading review

| Question | Answer | Risk |
|---|---|---|
| Can this format execute code during load? |  |  |
| Is the loader restricted or sandboxed? |  |  |
| Is network access disabled during load? |  |  |
| Are secrets available during load? |  |  |
| Is the artifact from a trusted source? |  |  |
| Is the artifact scanned or inspected? |  |  |

## Evaluation evidence

| Evidence | Result | Link/location |
|---|---|---|
| Functional evaluation |  |  |
| Regression tests |  |  |
| Security tests |  |  |
| Privacy tests |  |  |
| Robustness tests |  |  |
| RAG/agent tests if relevant |  |  |

## Registry decision

| Stage | Approved? | Approver | Notes |
|---|---|---|---|
| Experiment |  |  |  |
| Candidate |  |  |  |
| Staging |  |  |  |
| Production |  |  |  |

## Required actions before production

| Action | Owner | Blocking? |
|---|---|---|
|  |  |  |

## Residual risk

Document residual risk if the artifact is deployed.
