# Weak Example: DocOps Architecture Risk Review

The AI assistant should be careful with documents and should not follow bad instructions. The team should add guardrails and logging.

## Why this is weak

- No trust boundary is named.
- It does not distinguish read behavior from write behavior.
- "Guardrails" is not an implementable control.
- No validation test is described.
- No launch decision is made.
