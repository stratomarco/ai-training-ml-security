# MLOps Evidence Pack Review Lab

## Purpose

This is the concrete Module 08 review lab. It is intentionally a reasoning lab, not a runnable pipeline. Students inspect a static evidence pack and decide whether a model candidate should be promoted.

## Why this is not a runnable pipeline

The security decision in this module is not whether a toy pipeline can execute. The decision is whether the evidence around an ML artifact is strong enough to trust the artifact in production. A static evidence pack is closer to how engineers review real ML supply-chain risk: notebooks, dependency files, registry metadata, storage permissions, promotion logs, and review records.

## Evidence pack

Review:

```text
labs/mlops-supply-chain-labs/evidence-pack-review/
```

## Scenario

An ML team wants to promote `customer-risk-classifier` to a production-candidate registry. The model has acceptable aggregate accuracy, but the evidence pack contains weak or missing supply-chain controls.

## Student steps

1. Inspect `train.ipynb` and identify notebook-level risks.
2. Inspect `requirements.txt` and dependency evidence.
3. Inspect `metadata/training-run.json` and decide whether the training run is reproducible.
4. Inspect `registry/model_registry.json` and decide whether the promotion gate is acceptable.
5. Inspect `storage/bucket-policy.json` and identify who can overwrite training data or model artifacts.
6. Inspect `ci/promotion-workflow.yml` and identify whether the workflow proves artifact integrity.
7. Produce a review using the MLOps evidence-pack review template.

## Required findings

A strong submission should identify at least these issues:

- dependencies are unpinned and no lockfile is provided;
- the notebook installs dependencies at runtime;
- a fake inline secret appears in the notebook;
- the model artifact is a mutable pickle path rather than a content-addressed signed artifact;
- recorded and observed artifact hashes do not match;
- dataset hash, schema version, feature manifest, and split manifest are missing;
- the promotion policy allows auto-promotion with no approval;
- storage write permissions allow shared identities to overwrite artifacts;
- aggregate accuracy is treated as a release gate without robustness, privacy, slice, or rollback evidence.

## Deliverable

Submit one review memo with:

- recommendation: promote, limited pilot, or block;
- evidence table;
- root causes;
- required controls;
- validation plan;
- residual risk.

## Success criteria

The student should not merely say that the pipeline is insecure. The review must explain what evidence is missing, why that evidence matters, what control should replace it, and how the team would know the control works.
