# MLOps Evidence Pack Review

This directory is a static, synthetic evidence pack for Module 08. It is not a runnable ML pipeline. Students review the evidence as if they were assessing whether a model candidate should be promoted.

## Learning objective

The goal is to identify whether the training and promotion evidence is strong enough to trust the model artifact. Students should focus on provenance, dependency control, artifact integrity, identity, approval gates, rollback, and monitoring readiness.

## Files

| File | What to review |
|---|---|
| `train.ipynb` | Notebook training smells: inline install, fake inline secret, shared bucket, pickle export, missing manifests |
| `requirements.txt` | Unpinned dependencies and missing lockfile |
| `metadata/training-run.json` | Missing dataset hash, schema version, feature manifest, and dependency lockfile |
| `registry/model_registry.json` | Weak promotion policy and artifact hash mismatch |
| `storage/bucket-policy.json` | Shared write permissions and mutable model path |
| `ci/promotion-workflow.yml` | Accuracy-only promotion and no signed artifact check |
| `artifacts/model.pkl.README.md` | Placeholder explaining why the real binary artifact is not shipped |

## Student task

Write a short MLOps supply-chain review that answers:

1. Can this candidate be promoted as-is?
2. Which evidence is missing or untrustworthy?
3. Which controls must be implemented before promotion?
4. How would the team validate the fix?
5. What residual risk remains after remediation?

## Safety note

This evidence pack is intentionally fake and local. Do not connect it to real buckets, registries, notebooks, or credentials.
