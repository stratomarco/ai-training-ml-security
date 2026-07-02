# Lab  -  Model Artifact Provenance and Registry Review

## Purpose

Teach students to review model artifacts as production supply chain artifacts.

The goal is not to execute suspicious files. The goal is to reason about trust, provenance, safe loading, registry controls, and promotion gates.

## Scenario

A team wants to deploy a model artifact called:

```text
incident-triage-ranker-v3.pkl
```

It was uploaded to the model registry with this metadata:

| Field | Value |
|---|---|
| Model name | incident-triage-ranker |
| Version | v3 |
| Uploaded by | ml-engineer-2 |
| Source commit | unknown |
| Dataset version | latest |
| Training job ID | manual-run |
| Artifact hash | missing |
| Signature | missing |
| Evaluation | accuracy=0.91 |
| Security review | not performed |
| Privacy review | not performed |
| Promotion status | staging |

The team asks security to approve promotion to production.

## Student tasks

### Task 1  -  Trust assessment

Answer:

1. Can this artifact be trusted for production?
2. What evidence is missing?
3. Which risks are artifact-specific?
4. Which risks are registry-specific?
5. Which risks are process-specific?

### Task 2  -  Required metadata

Define the minimum metadata required for production promotion.

Recommended fields:

- model owner;
- business owner;
- source code commit;
- training pipeline ID;
- dataset versions;
- feature set version;
- dependency lockfile;
- container image digest;
- training parameters;
- artifact hash;
- artifact signature or provenance attestation;
- evaluation results;
- security test results;
- privacy test results;
- approver;
- rollback target.

### Task 3  -  Safe loading decision

Assume the model uses a serialized format that may be unsafe if untrusted.

Define a safe loading policy:

- which formats are allowed;
- which sources are trusted;
- when sandboxing is required;
- whether network access is allowed during load;
- whether secrets are available during load;
- how loading errors are handled;
- how suspicious artifacts are quarantined.

### Task 4  -  Registry promotion policy

Define who can move a model through these stages:

```text
experiment -> candidate -> staging -> production -> deprecated -> quarantined
```

Include required approvals and checks for each stage.

## Expected conclusion

Students should not approve production deployment based on the provided metadata.

The right conclusion is not simply “block forever.” The right conclusion is:

1. identify missing evidence;
2. define what must be fixed before production;
3. allow safe experimentation where appropriate;
4. require explicit risk acceptance if the business insists on deployment;
5. define monitoring and rollback if deployment proceeds.

## Instructor discussion

Ask:

- What does an artifact hash prove?
- What does signing prove?
- What does signing not prove?
- Can a signed model still be unsafe?
- What should happen if a model was built from poisoned data?
- How do you make registry controls developer-friendly?
- Should security approve every model manually?
- How can high-risk models be separated from low-risk experiments?
