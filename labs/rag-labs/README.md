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

<!-- LAB_QUALITY_STANDARD_RAG_CONSOLIDATION:START -->
## Runnable path

The runnable RAG-security path is BrokenPilot, not this paper folder.

Use these labs for hands-on work:

- `../brokenpilot/prototype-app/LAB_GUIDE.md`
- `../brokenpilot/STANDALONE_CORE_LAB_PATH.md`
- `../../modules/06-rag-security/brokenpilot-standalone-lab.md`

This folder remains as a scenario and discussion index only. Do not maintain a second paper version of the same RAG lab when BrokenPilot can demonstrate retrieval authorization and indirect prompt injection directly.

## Required deliverable

Students should produce a retrieval authorization and source-trust control note covering identity, tenant, document visibility, source trust, instruction/data separation, logging, validation, and residual risk.

The graded artifact is the retrieval control and validation, not the fact that a poisoned document can influence an answer.
<!-- LAB_QUALITY_STANDARD_RAG_CONSOLIDATION:END -->
