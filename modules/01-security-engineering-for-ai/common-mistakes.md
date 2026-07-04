# Common Mistakes: Security Engineering for AI

## Mistake 1: Treating the model as the security boundary

A model can refuse, warn, classify, or recommend. It should not be the only thing preventing unauthorized access, unsafe execution, or cross-tenant data exposure.

Better approach: use the model for interpretation and assistance, then enforce sensitive boundaries with deterministic application controls.

## Mistake 2: Starting with attack names instead of system behavior

Prompt injection, poisoning, extraction, and evasion are useful categories, but they are not the starting point. The starting point is what the system can read, write, decide, and trigger.

Better approach: map assets, trust boundaries, actions, and downstream effects first. Then map attack categories to those boundaries.

## Mistake 3: Confusing model evaluation with security validation

A model that passes a prompt test is not necessarily safe. The security question is whether the system prevents the unsafe outcome.

Better approach: validate controls directly. Test that retrieval authorization blocks the document. Test that tool authorization blocks the action. Test that output encoding escapes the sink.

## Mistake 4: Ignoring logs and recovery

Teams often focus on preventing the first failure and forget investigation and rollback. AI systems can create ambiguous incidents because the cause may involve prompt, context, retrieved data, memory, tool output, model version, or artifact provenance.

Better approach: log enough structured evidence to reconstruct the path from input to effect.

## Mistake 5: Treating every AI feature as equally risky

A grammar assistant and an operations agent should not have the same control set. Over-controlling low-risk features slows delivery. Under-controlling action-taking agents creates incidents.

Better approach: classify the feature by impact, data access, action authority, and reversibility.

## Mistake 6: Writing vague findings

"The AI can be tricked" is not a useful finding. It does not say what boundary failed, what evidence proves it, what control is needed, or how to validate the fix.

Better approach: write findings with evidence, root cause, impact, control, validation, residual risk, and owner.
