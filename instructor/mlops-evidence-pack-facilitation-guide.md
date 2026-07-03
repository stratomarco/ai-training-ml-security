# Instructor Guide: MLOps Evidence Pack Review

## Teaching goal

Students should learn that ML supply-chain security is an evidence problem. A model should not move toward production just because a notebook runs or aggregate accuracy is high.

## Facilitation plan

1. Start with the promotion question: would you promote this model?
2. Give students 20 minutes to inspect the evidence pack.
3. Ask them to identify the first blocker, not every possible issue.
4. Force each finding into the pattern: evidence, root cause, control, validation, residual risk.
5. Compare one strong and one weak example.

## Common student mistakes

- Saying "pin dependencies" but not requiring a lockfile validation step.
- Saying "review the model" without naming artifact signing, hash checks, or registry gates.
- Treating a fake inline secret as the only issue.
- Ignoring the mutable `latest` artifact path.
- Ignoring rollback and monitoring readiness.

## Anchor answer

The strongest decision is to block promotion until the team can prove dependency provenance, dataset provenance, artifact integrity, registry approval, storage least privilege, and rollback readiness.
