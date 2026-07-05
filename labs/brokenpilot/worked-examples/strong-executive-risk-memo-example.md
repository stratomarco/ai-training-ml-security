# Strong Example  -  Executive Risk Memo

## Decision memo: Internal AI operations assistant pilot

**Audience:** CISO and VP of Engineering  
**Prepared by:** Security Architecture  
**Recommendation:** Proceed with a limited pilot after launch blockers are fixed.

## Decision needed

Decide whether the AI operations assistant can begin a limited internal pilot next week.

## Recommendation

Proceed with a limited pilot only after four launch blockers are fixed: remove exposed secrets from notebooks, restrict model-registry permissions, sign the model artifact, and disable automatic feedback-to-training. These controls preserve the business value of the pilot while reducing the highest-risk failure modes.

## Business value

The assistant can reduce operational load by summarizing incidents, searching documentation, and helping engineers triage tickets faster. A limited pilot is useful because it will generate evidence about workflow value, model quality, and security controls before wider rollout.

## Top risks

| Risk | Impact | Why it matters |
|---|---|---|
| Sensitive data in training and feedback | Privacy breach, regulatory exposure, employee/customer trust loss | The system may memorize, retrieve, or log sensitive data beyond the original access context. |
| Weak model artifact provenance | Tampered or wrong model deployed | Without signing and registry controls, the team cannot prove which artifact is running. |
| Untrusted feedback loop | Poisoned behavior over time | User corrections may become training input without review, allowing accidental or malicious behavior changes. |

## Launch blockers

| Blocker | Required control | Owner |
|---|---|---|
| Plaintext API key in notebook | Rotate exposed key and move secrets to managed secret store | Platform Engineering |
| Broad model-registry permissions | Restrict write/deploy permissions to release owners | ML Platform |
| Unsigned model artifact | Sign model artifact and record provenance | ML Platform |
| Automatic feedback-to-training | Require human review before feedback enters training data | ML Engineering |

## Manageable pilot risks

Some model quality and overreliance risks can be managed during the pilot if the assistant is limited to internal engineering users, cannot perform destructive actions, and all outputs remain advisory. The pilot should have a clear rollback path and weekly review of logs, user feedback, and control effectiveness.

## Residual risk

Even after the launch blockers are fixed, the model may still produce incorrect recommendations or expose sensitive information through poor retrieval design. This is acceptable only for a limited pilot where the assistant cannot directly modify production systems and users are instructed to verify outputs before acting.

## Evidence to collect

During the pilot, collect evidence of retrieval scope, sensitive-data exposure attempts, model artifact version, feedback submissions, user corrections, and any attempted unsafe actions.

## Final recommendation

Launch a limited internal pilot after the four launch blockers are fixed. Do not approve broad deployment or autonomous action until the team demonstrates retrieval authorization, feedback review, artifact provenance, monitoring, and rollback are working in practice.
