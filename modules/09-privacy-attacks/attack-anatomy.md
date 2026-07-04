# Attack anatomy: Privacy leakage in AI systems

## Scenario

BrokenPilot stores fake internal documents for multiple tenants. `DOC-002` is an alpha restricted document with a fake token. A beta user, `chris`, searches for payment or credential information. When retrieval authorization is disabled, the retriever returns alpha material to a beta user, and the model can summarize or expose the fake sensitive fragment.

## Step-by-step failure

1. The user sends a query containing terms that match a restricted document.
2. The retriever searches across documents without enforcing tenant and role filters.
3. The restricted document appears in the context set.
4. The model treats retrieved context as available information.
5. The response includes a fake sensitive fragment or enough information to identify the restricted content.
6. Logs or traces may preserve the sensitive fragment even after retrieval authorization is fixed.

## Security property lost

The system loses tenant isolation and data minimization. The user does not need direct document access because the AI application becomes a proxy to the document store.

## Why prompt wording cannot fix this

A prompt such as "never reveal secrets" is not a reliable privacy boundary. The model should not receive unauthorized context in the first place. If the model sees restricted context, the design has already failed.

The real control is retrieval authorization before context construction, followed by output and log controls for defense in depth.

## Variant: logging still leaks

A team fixes retrieval authorization but keeps verbose traces that include previously retrieved restricted context. Support staff, developers, or analytics users may now see sensitive fragments through observability tooling. The system no longer leaks to the end user, but it still leaks to an unauthorized internal audience.

This is a realistic privacy failure. Many AI applications store prompts, retrieved context, tool arguments, and model responses for debugging. Those records need classification, redaction, retention limits, and access control.

## Good finding pattern

A strong privacy finding should include:

- the data boundary crossed;
- the user or role that crossed it;
- the system path that enabled disclosure;
- the sensitive class of data exposed;
- the control that must enforce the boundary;
- how to validate the boundary after remediation;
- what residual paths remain, especially logs and traces.

## Weak finding pattern

A weak privacy finding says only that "the AI leaked data" or "the model revealed a secret." That does not tell the team where the boundary failed or which control should be implemented.
