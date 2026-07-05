# Strong Example: DocOps Architecture Risk Review

## Scope

The review covers an internal AI assistant that reads operational documentation and helps engineers summarize or update procedures.

## Evidence used

- The assistant retrieves internal documents.
- Some documents may describe production procedures or configuration.
- The assistant can influence operational decisions.
- The trust boundary between retrieved content and system instruction must be explicit.

## Risk statement

If retrieved documentation is treated as authority rather than untrusted content, a poisoned or incorrect document can steer the assistant into unsafe operational guidance.

## Naive fix that is not enough

A stronger system prompt is not enough. The assistant still consumes untrusted text, and operational safety cannot depend on the model ignoring hostile or stale content.

## Recommended controls

| Control | Owner | Validation |
|---|---|---|
| Retrieval authorization by user, tenant, and document class | Platform | Attempt cross-scope retrieval and confirm denial |
| Source trust labels and freshness metadata | Documentation platform | Verify stale or low-trust docs are flagged in output |
| Human approval for write or production-impacting actions | Operations | Confirm no write path runs without approval |
| Audit log for retrieval and action proposals | Security | Review logs for source IDs and proposed action details |

## Defense-in-depth

Retrieval authorization limits what the assistant can read. Approval gates limit what it can change or recommend as an action even if retrieval returns bad content.

## Residual risk

The assistant can still summarize stale or incomplete but authorized documentation. Users must see source citations, freshness, and confidence limits.

## Decision

Pilot only for read-only summarization. Defer write or production-action features until approval gates and audit logging are implemented.
