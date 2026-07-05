# Deep dive: Secure MLOps and AI supply chain

## The decision this module teaches

This module teaches one core decision:

> Can this model artifact be promoted, deployed, and operated with enough evidence that we trust where it came from, what it depends on, and how it can be rolled back?

That is a different question from whether the model is accurate. Accuracy says something about observed behavior on an evaluation set. Supply-chain security says something about provenance, integrity, repeatability, access control, and operational control over the path from data to production.

In a real organization, most AI supply-chain failures are not dramatic. They look like normal engineering shortcuts:

- a notebook installs packages at runtime;
- a dataset is pulled from a shared bucket without a stable hash;
- a model is exported as a mutable `latest` artifact;
- a registry allows promotion without independent approval;
- a training secret is copied into a notebook or log;
- a CI job evaluates accuracy but never verifies artifact identity;
- rollback depends on someone remembering which file was good.

The security problem is that these shortcuts remove evidence. When evidence disappears, a team cannot answer basic launch and incident questions: what changed, who approved it, what data was used, what code ran, what artifact is deployed, and how to return to a known-good state.

## The supply chain is the security boundary

Traditional application security often focuses on code review, dependency scanning, identity, and runtime hardening. ML systems still need those controls, but the trust boundary expands. The model artifact, training data, feature code, evaluation logic, prompts, retrieval index, registry metadata, and deployment pipeline all become part of the system that can change production behavior.

A model does not have to be malicious to be risky. It can be stale, trained on the wrong slice, evaluated with the wrong metric, exported from a compromised environment, loaded from a mutable path, or promoted by a workflow that checks the wrong thing. The lesson is not that every model artifact is hostile. The lesson is that production behavior depends on a chain of artifacts, and the team needs evidence for the chain.

## What students should stop believing

A common mistake is to treat MLOps supply-chain security as dependency scanning plus a model registry. Those are useful, but not sufficient. A registry that stores a model without signed metadata, immutable versioning, training-data references, approval evidence, evaluation reports, and rollback linkage is mostly a filing cabinet.

Another mistake is to assume that reproducibility is a research nicety. In production security, reproducibility is an incident-response control. If the model behaves badly and the team cannot reconstruct the training run or identify the promoted artifact, the team cannot do root-cause analysis with confidence.

## Good evidence looks boring

Strong supply-chain evidence is not flashy. It usually looks like boring records:

- dataset identifiers and hashes;
- dependency lockfiles;
- training code commit;
- image digest;
- model artifact digest;
- evaluation report tied to that exact artifact;
- promotion approval;
- deployment record;
- rollback target;
- monitoring plan.

The evidence pack lab is designed around this reality. Students are not asked to run a toy pipeline. They inspect a realistic set of weak artifacts and decide whether promotion should proceed. That is how many engineers, security reviewers, and platform teams encounter MLOps risk in practice.

## The main engineering tradeoff

The tradeoff is not "security versus speed". The real tradeoff is between fast undocumented movement and fast repeatable movement.

A mature platform makes the secure path the easy path: default lockfiles, default artifact digests, default registry metadata, default approval gates, default rollback records, and default evaluation templates. Security work should reduce custom review burden over time, not add a bespoke meeting to every model release.

## Lab transfer

When students move from this reading to the evidence-pack lab, they should look for missing evidence before looking for exotic attacks. Ask:

1. Can we identify the exact artifact proposed for production?
2. Can we identify the exact data and code used to create it?
3. Can we tell whether the artifact was tampered with after training?
4. Can we tell who approved promotion and on what basis?
5. Can we roll back to a known-good version?
6. Can we explain the residual risk to a product or engineering leader?

If the answer to any of these is no, the finding should focus on the broken control path, not only the suspicious file.
