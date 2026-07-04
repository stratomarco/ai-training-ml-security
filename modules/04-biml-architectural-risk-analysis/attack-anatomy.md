# Attack Anatomy: Architectural Risk Paths

## The pattern

Architectural risk paths are design-level paths from assumption to impact. They often exist before an attacker arrives.

1. The design makes an assumption.
2. The assumption is not enforced by a control.
3. An input, data source, model behavior, user, or pipeline step violates the assumption.
4. The system has no boundary to stop the effect.
5. Impact occurs in data exposure, state change, bad promotion, privacy leakage, or operational decision.

## Risk path 1: "Retrieved docs are safe"

Assumption: documents in the retrieval index are safe to place into model context.

Reality: documents may contain restricted data, cross-tenant content, stale procedures, or malicious instructions.

Missing control: source trust, classification, retrieval authorization, and instruction/data separation.

Impact: data leakage or model behavior influenced by untrusted document text.

## Risk path 2: "The model will only call safe tools"

Assumption: the model will choose safe actions because the prompt says so.

Reality: prompts, retrieved context, memory, or user pressure can steer tool selection.

Missing control: tool broker authorization, approval policy, target-object checks, and audit.

Impact: unauthorized update or unsafe operational action.

## Risk path 3: "The artifact came from our notebook"

Assumption: the model artifact is trustworthy because a team member produced it.

Reality: dependencies, data, notebook state, artifact path, and promotion decision may be untracked or tampered.

Missing control: reproducible build, dependency lock, dataset hash, artifact digest, approval, and registry policy.

Impact: wrong or malicious model reaches production.

## Risk path 4: "Human review solves it"

Assumption: a human will catch unsafe output.

Reality: the human sees a polished answer without sources, uncertainty, policy context, or evidence.

Missing control: review interface, source display, risk explanation, approval criteria, and escalation path.

Impact: rubber-stamp approval or missed risk.

## Risk path 5: "Logs are internal"

Assumption: logs are safe because they are internal.

Reality: logs may be broadly accessible, long-retained, exported, or used for training and analytics.

Missing control: redaction, access control, retention, purpose limitation, and sensitive trace handling.

Impact: secondary privacy or confidentiality breach.

## Defensive lesson

Architectural risk analysis finds the missing enforcement point before the failure is implemented. The best time to fix a trust boundary is before the model, data, tool, and pipeline have been coupled together.
