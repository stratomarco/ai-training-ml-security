# Student Reading Guide: Module 06: RAG Security and Indirect Prompt Injection

## What this module is really about

RAG changes the attack surface by making retrieved content part of the model context. Retrieval is not just search quality. It is an authorization and trust decision. A bad RAG design can leak data, follow hostile document instructions, or give the model context it should never see.

## Question to keep in mind

Who is allowed to retrieve this content, why is it trusted, and what should the model be allowed to do with it?

## Decisions students must learn to make

- Apply authorization before retrieval results enter model context.
- Separate source trust from semantic relevance.
- Decide how to represent document classification, tenant, role, and user-specific access.
- Validate that restricted content is unavailable to unauthorized users, not merely hidden in the UI.

## Lab or exercise connection

Use BrokenPilot retrieval authorization and indirect prompt-injection flows. The old paper RAG lab should point to the runnable path instead of duplicating it.

## What a strong submission looks like

A strong submission includes evidence that unauthorized retrieval is blocked before model context construction, explains the root cause as authorization after retrieval or missing retrieval authorization, and adds a note on residual risk such as logging, cache, or embedding metadata leakage.

## Common misreadings to avoid

- Assuming vector similarity is a security decision.
- Filtering final answers while still placing restricted documents in context.
- Treating all internal documents as equally trusted.

## Exit ticket

Explain why the correct place to enforce retrieval authorization is before model invocation.
