# Lab  -  Broken ML Pipeline Supply Chain Review

## Purpose

Review an intentionally weak ML pipeline and design a secure MLOps control model.

This lab is a tabletop exercise. It does not require attacking real systems or running unsafe artifacts.

## Scenario

The ML team built **TriageRanker**, an internal incident prioritization model. It predicts incident severity and recommends which team should respond.

The model is currently trained and deployed through a loosely controlled process:

```text
external dataset + internal ticket export
  -> shared spreadsheet labels
  -> research notebook
  -> unpinned dependencies
  -> GPU workstation training
  -> model.pkl
  -> shared bucket
  -> model registry
  -> automatic production deployment
  -> operator feedback
  -> retraining
```

## Provided evidence

Students receive these fictional artifacts:

### `requirements.txt`

```text
pandas
numpy
scikit-learn
joblib
requests
incident-helper
```

### `train.ipynb` observations

- Contains exploratory cells.
- Contains `!pip install incident-helper`.
- Contains a commented API key.
- Reads data from `s3://shared-ml-data/tickets/`.
- Exports `model.pkl`.
- Pushes the artifact to a shared bucket.

### Registry behavior

- Any ML engineer can register a new model.
- Any ML engineer can change model stage to `production`.
- Production stage triggers deployment.
- Registry metadata does not require dataset version, code commit, dependency lockfile, evaluation result, or approver.

### Evaluation behavior

- Random train/test split.
- Accuracy threshold only.
- No security tests.
- No privacy tests.
- No drift or abuse monitoring.

## Student tasks

### Task 1  -  Artifact inventory

Create an inventory of all artifacts that influence model behavior.

Include:

- dataset;
- labels;
- notebook;
- dependencies;
- training environment;
- model artifact;
- registry metadata;
- deployment pipeline;
- feedback data.

### Task 2  -  Risk identification

Find at least twelve risks.

Use this structure:

| Risk | Asset | Root cause | Impact | Mitigation |
|---|---|---|---|---|
| Example | Model artifact | No provenance | Cannot trust production model origin | Require signed provenance before promotion |

### Task 3  -  Secure pipeline redesign

Redesign the pipeline with security gates:

```text
approved data
  -> reviewed training code
  -> locked dependencies
  -> controlled training job
  -> artifact integrity metadata
  -> model registry
  -> security/evaluation gates
  -> approval
  -> deployment
  -> monitoring
  -> rollback
```

### Task 4  -  Minimum viable controls

The team says it needs to ship in two weeks.

Define:

- controls required before first deployment;
- controls that can follow in the next release;
- risks that require explicit acceptance.

## Expected findings

Strong answers should identify:

- external dataset provenance risk;
- internal ticket sensitivity risk;
- editable label spreadsheet risk;
- notebook secret leakage;
- unpinned dependency risk;
- unclear dependency source risk;
- shared service account risk;
- unsafe `model.pkl` artifact pattern;
- no artifact hash/signature;
- shared bucket write risk;
- weak registry promotion permissions;
- automatic deployment from stage change;
- no security/privacy evaluation;
- no rollback;
- feedback poisoning risk;
- lack of auditability.

## Mitigation examples

| Risk area | Mitigation |
|---|---|
| Dataset | Data source approval, lineage, immutable versions, access control. |
| Labels | Restricted write access, review sampling, labeler identity, change logs. |
| Notebook | Secret scanning, reviewed pipeline extraction, no direct production artifact creation. |
| Dependencies | Lockfile, scanning, approved package sources. |
| Training | Scoped service account, controlled runner, network and data access limits. |
| Model artifact | Safe format where possible, hash/signature, provenance, sandboxed loading. |
| Registry | RBAC, promotion approval, immutable versions, audit logs. |
| Evaluation | Security, privacy, robustness, and abuse-case gates. |
| Deployment | Staged rollout, monitoring, rollback, kill switch. |
| Feedback | Quarantine, provenance, abuse detection, review before retraining. |

## Discussion questions

1. Which single control would reduce the most risk quickly?
2. Which risk is most likely to be ignored by ML teams?
3. Which control best balances security and developer velocity?
4. Which controls belong in CI/CD and which require human review?
5. What evidence should leadership require before allowing production deployment?

## Evidence-pack option

This tabletop can be run with the static evidence pack in `evidence-pack-review/`. That pack gives students concrete artifacts to inspect: notebook, dependency file, registry metadata, storage policy, promotion workflow, and artifact hash evidence. The intended learning outcome is a review decision and remediation backlog, not successful execution of a toy pipeline.
