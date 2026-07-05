
# Round 3 Content Quality Fixes

This pass closes the small quality gaps found after the final content review.

## Decisions

- BrokenPilot is the primary runnable target for LLM, RAG, agent, privacy, red-team, and capstone labs.
- DVAIA is optional appendix material, not a critical-path lab dependency.
- Legacy paper RAG and agent labs are consolidated into BrokenPilot-primary guidance.
- Toy-classifier evasion must preserve malicious intent while changing the model decision.
- Module 05 output handling must be student-facing through `POST /render` and `ENABLE_OUTPUT_ENCODING`.
- Modules 01 and 02 must end in explicit graded artifacts.

## Not part of this pass

- MkDocs strict navigation
- final CI cleanup
- removal of temporary apply scripts
- broad prose normalization

Those belong to the release-hardening phase.
