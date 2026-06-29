# RAG Labs

RAG labs focus on retrieval-augmented generation, indirect prompt injection, retrieval authorization, source trust, and context integrity.

## Lab ideas

1. Malicious document injection
2. Cross-tenant retrieval failure
3. Sensitive document summarization
4. Poisoned knowledge base entry
5. Source spoofing
6. Retrieval over-permissioning
7. Hidden instruction in markdown or HTML
8. Prompt leakage through retrieved context

## Core lesson

Retrieved content is untrusted input. The model should not be allowed to treat retrieved data as higher-priority instructions.
