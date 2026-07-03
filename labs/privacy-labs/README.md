# Privacy Labs

This folder contains lab guides for Module 09  -  Privacy Attacks and Data Protection.

The labs are designed as local, fake-data exercises. They should not be run against real systems or real personal data.

## Labs

| Lab | Purpose |
|---|---|
| `brokenpilot-cross-tenant-leakage-lab.md` | Runnable BrokenPilot lab showing cross-tenant retrieval leakage and the retrieval authorization fix. |
| `privacy-leakage-cross-tenant-rag-lab.md` | Review a RAG assistant with cross-tenant retrieval and logging privacy failures. |
| `membership-inference-model-inversion-tabletop.md` | Tabletop exercise for membership inference, model inversion, and training data extraction risk. |

## Lab philosophy

Privacy labs should teach students to reason about data flows and controls, not merely to extract sensitive examples.

Every lab should end with:

- root cause;
- secure design;
- residual risk;
- operational trade-offs;
- communication to engineering and leadership.

<!-- LAB_QUALITY_STANDARD_PRIVACY_ANCHORS:START -->
## Worked examples

Use the membership inference worked examples to calibrate reasoning-lab grading:

- `worked-examples/strong-membership-inference-risk-review.md`
- `worked-examples/weak-membership-inference-risk-review.md`

The cross-tenant leakage lab is runnable in BrokenPilot. The membership inference and model inversion lab remains a reasoning lab and should be graded on evidence, control design, validation, and residual risk.
<!-- LAB_QUALITY_STANDARD_PRIVACY_ANCHORS:END -->
