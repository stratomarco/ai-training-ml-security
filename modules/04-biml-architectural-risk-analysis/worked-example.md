# Worked Example: Architectural Risk Analysis for DocOps Assistant

## Scenario

DocOps Assistant helps engineering teams search internal documents, summarize design notes, and draft updates to operational runbooks. Future versions may create pull requests or update documentation pages automatically.

## Architecture assumptions

The design assumes that indexed documents are safe to retrieve, that model summaries are safe to display, that users will verify drafted changes, and that future write actions can be added later.

## Risk 1: Mixed-trust documents enter model context

The document index contains public engineering docs, restricted operational notes, and user-authored pages. If retrieval is based only on semantic similarity, restricted content may enter context for unauthorized users.

Security property: confidentiality and authorization.

Recommended change: add metadata labels for tenant, owner, classification, allowed roles, and allowed users. Enforce retrieval authorization before context assembly.

Validation: a user without access to restricted operational notes receives no restricted chunks even when the query is semantically relevant.

## Risk 2: Retrieved document instructions influence the model

User-authored pages can contain instructions that conflict with application policy. If retrieved text is treated as authority, an attacker can steer the assistant.

Security property: integrity.

Recommended change: separate system instructions from retrieved content, label retrieved content as untrusted data, and keep sensitive enforcement outside model behavior.

Validation: a page containing an instruction marker does not change retrieval authorization, output handling, or tool authorization.

## Risk 3: Future write actions lack design controls

The current design discusses future pull-request creation but does not define authorization, approval, diff review, or rollback.

Security property: integrity and accountability.

Recommended change: require a tool broker for write actions. The broker should validate user authority, repository, file path, action type, approval requirement, and audit record. High-impact docs require human approval.

Validation: unauthorized write attempts are denied and approved writes create audit records with diff, approver, and rollback link.

## Risk 4: Logs may retain sensitive context

The assistant logs prompts and answers for quality improvement. If retrieved restricted content appears in logs, the logging system becomes a secondary exposure path.

Security property: privacy and confidentiality.

Recommended change: log source IDs, classifications, control decisions, and redacted excerpts instead of full restricted content. Apply retention and access controls.

Validation: known fake sensitive fragments do not appear in broad logs.

## Recommendation

Proceed with a read-only pilot only after retrieval authorization and logging controls are implemented. Do not enable write actions until the tool broker, approval workflow, audit, and rollback design are complete.

## Residual risk

Even in read-only mode, summaries may omit context or mislead users. The UI should show sources and tell users when retrieved evidence is incomplete.
