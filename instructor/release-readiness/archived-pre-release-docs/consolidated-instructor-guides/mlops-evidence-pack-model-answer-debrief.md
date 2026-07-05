# Instructor Debrief Guide: MLOps Evidence-Pack Review

## Purpose

This debrief helps instructors turn the Module 08 evidence-pack review from a checklist exercise into a security-engineering discussion. Students should leave understanding that model promotion is a risk decision based on evidence, not a ceremony based on file names and accuracy metrics.

## Opening question

Ask:

> If this model caused a production incident next week, what would we be able to prove?

Good answers should mention artifact digest, training data version, training code commit, dependency set, approval record, deployment target, and rollback path.

## Expected student findings

Most strong submissions should identify at least four of the following:

1. Mutable artifact reference or missing immutable artifact identity.
2. Hash mismatch or missing digest verification.
3. Unpinned dependencies and weak environment reproducibility.
4. Runtime package installation in notebook.
5. Missing dataset hash or schema evidence.
6. Inline fake secret in notebook.
7. Shared mutable storage or weak bucket policy.
8. No signed manifest or model package attestation.
9. No human approval or separation of duties for promotion.
10. No rollback evidence.

## What separates strong from weak submissions

Weak submissions list smells:

> The notebook has bad practices and should be cleaned.

Strong submissions connect evidence to a decision:

> Because the registry points to a mutable artifact and the observed digest does not match the recorded digest, the team cannot prove that the reviewed model is the one being promoted. Promotion should fail until digest verification and signed model manifests are enforced.

## Naive fixes to challenge

Challenge these if students propose them:

- "Rename the model file." Ask how the system prevents overwrite.
- "Tell engineers not to use notebooks." Ask what production training path replaces it.
- "Add an approval checkbox." Ask what evidence the approver reviews.
- "Pin dependencies." Ask where the lockfile hash is stored and how promotion verifies it.
- "Use a private bucket." Ask who can write to production artifact paths.

## Defense-in-depth moment

Use artifact integrity as the layered-control discussion:

- Immutable URI helps identify the artifact.
- Digest check detects change.
- Signature links the artifact to a trusted build or promotion process.
- Least-privilege storage prevents direct overwrite.
- Approval gate makes promotion accountable.
- Runtime verification confirms what is actually deployed.

No single layer is enough. The point is not to add controls for decoration. The point is to close the gap between reviewed artifact and deployed artifact.

## Real engineering tradeoff

Students may argue that strict promotion gates slow ML teams down. A good answer acknowledges that risk. The better framing is:

- ad hoc review slows teams repeatedly
- standardized evidence makes review faster over time
- automation should collect evidence, not skip review
- exceptions should be explicit, time-bounded, and visible

## Debrief prompts

1. Which missing evidence would make you block production promotion immediately?
2. Which issues could be allowed in a limited internal pilot?
3. What is the smallest control set that changes the launch decision?
4. What evidence would you require from the model owner?
5. What evidence would you require from the platform team?
6. What residual risk remains even after supply-chain controls are fixed?

## Grading anchors

High-scoring submissions:

- cite specific evidence-pack files
- explain the security property at risk
- recommend a decision
- propose implementable controls
- include validation steps
- discuss residual risk
- avoid treating accuracy as the only launch gate

Low-scoring submissions:

- list vague best practices
- recommend "more guardrails" without control placement
- ignore validation
- ignore approval and rollback
- fail to explain why the finding matters to promotion

## Suggested timing

For a 40-hour course:

- 10 minutes: individual evidence review
- 20 minutes: small-group finding selection
- 20 minutes: remediation design
- 15 minutes: executive recommendation drafting
- 20 minutes: debrief and comparison against model answer

## Closing message

Model supply-chain review should answer four questions:

1. What exactly are we promoting?
2. Where did it come from?
3. Who approved it, based on what evidence?
4. How do we recover if it is wrong?

If the evidence pack cannot answer those questions, the promotion process is not ready for production.
