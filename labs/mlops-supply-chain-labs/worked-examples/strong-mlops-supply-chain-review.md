# Strong Example: MLOps Evidence Pack Review

## Recommendation

Block promotion. The model may have acceptable aggregate accuracy, but the evidence pack does not establish artifact integrity, training reproducibility, dependency provenance, storage integrity, or approval control.

## Key findings

| Finding | Evidence | Required control | Validation |
|---|---|---|---|
| Mutable artifact path | Registry points to `models/latest/model.pkl` | Content-addressed artifact path and signed artifact | Registry rejects unsigned or hash-mismatched artifacts |
| Hash mismatch | Recorded and observed SHA-256 values differ | Verify artifact hash before promotion | Promotion job fails on mismatch |
| Unpinned dependencies | `requirements.txt` has no pinned versions | Lockfile with reviewed package sources | Rebuild uses identical dependency graph |
| Missing dataset evidence | Training run has no dataset hash or schema version | Dataset manifest and schema contract | Promotion requires matching dataset manifest |
| Weak promotion gate | Approval not required and zero reviewers | Human approval for production candidate | CI blocks promotion without approval record |
| Shared write permissions | Multiple identities can write to the bucket | Least-privilege storage policy and object lock | Unauthorized overwrite attempt fails |

## Residual risk

Even after these controls, the model can still fail under drift, data-quality changes, or adversarial input. Promotion should require monitoring, rollback, and periodic review of training data and model behavior.
