# Controls and Remediations: Security Engineering for AI

## Control objective

The objective is to make AI-assisted workflows safe enough for their role. That means defining what the model can influence, which boundaries must be enforced outside the model, and how to validate that the system fails safely.

## Strong controls

### Explicit system boundaries

Document what the model can read, write, decide, and trigger. Separate "drafting text" from "changing state." Separate "retrieving public content" from "retrieving restricted content." Separate "suggesting an action" from "executing an action."

A design is not reviewable until those boundaries are explicit.

### Deterministic authorization at action points

Every sensitive action must be authorized at the point of execution. The authorization check should consider user identity, role, tenant, target object, action, policy, approval state, and risk level.

The model's statement that something is allowed is not authorization.

### Instruction/data separation

System instructions, developer instructions, user input, retrieved documents, tool results, memory, and external content should be treated as different trust classes. The application should preserve those classes in prompts, logs, policy checks, and downstream processing.

### Output validation and context-specific encoding

Model output must be validated for the context where it is used. HTML needs HTML encoding. Tool arguments need schema validation and authorization. Queries need parameterization and allowlists. Stored memory needs trust classification and review.

### Human review for high-impact actions

Approval should be required when the action is irreversible, cross-tenant, high-value, externally visible, legally sensitive, or operationally risky. The approval should show evidence, not only the model's conclusion.

### Audit and recovery

Logs should capture request, user, retrieved sources, proposed action, authorization decision, approval state, output sink, and final result. Recovery plans should exist for bad actions, poisoned memory, leaked data, and bad model promotions.

## Weak controls

### Stronger prompt wording

Better prompts can improve behavior, but they are not enough for security boundaries. A prompt can be ignored, contradicted, bypassed, or overwhelmed by retrieved context.

### A blacklist of suspicious strings

Signature checks can help teach the concept or detect known examples. They are not a complete control. Attackers can rephrase, encode, split, translate, or hide instructions.

### One-time red team testing

A one-time test provides useful evidence, but the system changes. Data changes, models change, tools change, policies change, and attackers adapt. Security-critical AI systems need regression tests and monitoring.

### Accuracy-only evaluation

Accuracy measures task performance, not security. A model can be accurate on normal examples and unsafe under adversarial inputs, cross-tenant retrieval, output sink misuse, or bad tool authorization.

## Remediation workflow

1. Name the security property that failed.
2. Identify the trust boundary that was crossed.
3. Move enforcement outside the model when the property is critical.
4. Add a deterministic test that proves the boundary.
5. Add monitoring for residual risk.
6. Document the remaining uncertainty.

## Validation examples

A retrieval authorization control is validated when a user from tenant beta cannot retrieve tenant alpha restricted documents, regardless of model wording.

A tool authorization control is validated when a model-generated request to update another tenant's ticket receives a deny response at the tool boundary.

An output handling control is validated when model output containing HTML-like content is escaped before rendering.

A supply-chain control is validated when an artifact cannot be promoted without dataset hash, dependency lock, artifact digest, approval, and rollback metadata.

## Residual risk

Even after strong controls, some risk remains. The model may still produce misleading summaries, incomplete reasoning, or low-quality recommendations. Users may over-trust the output. Monitoring may miss rare failures. Logs may be incomplete. The goal is to ensure that residual risk is known, bounded, and owned.
