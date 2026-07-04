# Worked Example: Architecture Review for a RAG Operations Assistant

## Scenario

A company proposes a RAG assistant for operations teams. It searches runbooks, incident tickets, and configuration notes. It can answer questions and draft ticket updates. Future versions may call tools.

## Architecture sketch in words

Users send questions through a web UI. The application sends the query to a retrieval service. The retrieval service searches a vector database built from runbooks and tickets. Retrieved chunks are inserted into a prompt. The model generates an answer. The answer is displayed and logged. Draft ticket updates can be saved by the user.

## Boundaries

User input is untrusted. Retrieved content is data, not authority. The vector database contains mixed-tenant and mixed-classification content. The model service sees prompt and context. The UI is an output sink. The logging system receives prompts, context IDs, answer text, and errors.

## Findings

### Finding 1: Retrieval authorization is not defined

If the vector database returns documents based only on semantic relevance, users may receive documents from another tenant or classification. The control should enforce tenant, role, classification, and allowed-user metadata before chunks enter context.

Validation: a beta viewer querying for an alpha restricted token should receive no alpha restricted chunks.

### Finding 2: Retrieved content can become instruction

The architecture does not separate system instructions from retrieved content. A document can contain text that tells the model to ignore policy. The control should label retrieved content as untrusted data and keep enforcement outside the model.

Validation: a document containing an instruction marker should not change authorization or tool behavior.

### Finding 3: Logs may contain sensitive context

The logging path receives prompt and answer text. If retrieved chunks or sensitive fragments are logged broadly, privacy and confidentiality risk remains even if the final UI answer is filtered.

Validation: sensitive training-only fragments should not appear in broad application logs.

## Recommended architecture changes

Add retrieval authorization before context assembly. Add context labels in prompt construction. Add output encoding for the UI. Limit logs to source IDs, classifications, control decisions, and redacted excerpts. Add audit records for draft saves and future tool actions.

## Residual risk

The assistant may still summarize incorrectly or omit important context. For high-impact operational decisions, the system should show sources, confidence indicators, and require human review.
