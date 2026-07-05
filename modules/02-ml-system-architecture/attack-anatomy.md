# Attack Anatomy: Architecture-Level Failure Paths

## The pattern

Architecture-level attacks happen when a system allows untrusted influence to cross into a sensitive component without the right control at the boundary.

The attacker may not attack the model directly. They may place text in a document, influence a data pipeline, abuse a broad service account, manipulate metadata, poison feedback, or exploit a weak output sink.

## Failure path 1: Cross-tenant retrieval

A user from tenant beta asks a broad question. The retrieval layer searches documents across tenants. Metadata filters are missing or applied after retrieval. A restricted tenant alpha document enters model context. The model includes a sensitive fragment in the answer.

The failed component is the retrieval boundary. The model only made the exposure visible.

## Failure path 2: Tool confused deputy

A user asks the agent to update a ticket. The model creates a plausible tool call. The tool endpoint trusts the model-generated target ticket and uses a broad service account. No target-object authorization is performed. The ticket is updated even though the user should not be able to update it.

The failed component is the tool broker or action endpoint. The model proposed the action, but the system executed it.

## Failure path 3: Output sink misuse

A model answer includes HTML-like text. The UI embeds it directly into a dashboard. The output is treated as display-safe even though it came from untrusted context.

The failed component is the rendering boundary. Output must be encoded for the sink.

## Failure path 4: Artifact promotion without provenance

A notebook trains a model and exports a pickle file to a shared bucket. The registry records accuracy but not dataset hash, dependency lock, artifact digest, approval, or rollback plan. The model is promoted because it appears to perform well.

The failed component is the release process. The model's performance does not prove artifact integrity.

## Failure path 5: Logging creates a second data leak

The system correctly blocks restricted data from the final answer, but logs full prompts, retrieved context, and model outputs to a broad analytics system. Sensitive data is no longer visible to the user, but it is visible to log readers.

The failed component is the observability path. Logs are part of the architecture, not an afterthought.

## What students should learn to trace

For each failure path, trace:

1. Entry point.
2. Trust boundary crossed.
3. Missing control.
4. Downstream effect.
5. Evidence that proves the path.
6. Control that breaks the path.
7. Residual risk after the fix.

This is the same method students will use in BrokenPilot, the toy-classifier app, and the evidence-pack review.
