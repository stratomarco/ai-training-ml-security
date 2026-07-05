# MLOps Evidence Pack Instructor Guide

This is the single instructor entry point for the Module 08 MLOps and AI supply-chain evidence-pack lab.

## What the lab teaches

The lab teaches students to review an ML delivery path as a security evidence problem. Students should identify where artifact identity, dependency provenance, dataset provenance, storage controls, promotion gates, validation, rollback, and approval are weak.

This is intentionally a reasoning lab, not a fake CI/CD system. The evidence pack gives students enough material to produce a realistic review without spending the session debugging infrastructure.

## Instructor preparation

Review the evidence pack and model answer before class:

- `Evidence pack README`
- `Student lab`
- `Complete model answer`
- `Evidence map`
- `Executive readout`
- `Model-answer rubric`

## How to run the session

1. Start from the release decision: should this model be promoted?
2. Give students time to inspect the evidence pack before naming controls.
3. Ask them to separate facts from assumptions.
4. Require every finding to cite a concrete artifact in the pack.
5. Push students beyond dependency pinning. The strongest reviews connect artifact identity, training data, evaluation, promotion, rollback, and ownership.
6. End with a go/no-go recommendation and a staged remediation plan.

## Debrief prompts

- Which finding would stop release immediately, and why?
- Which risks are supply-chain risks, and which are governance or operational risks?
- What evidence is missing but required for a defensible promotion decision?
- Which control gives the highest risk reduction with the least developer friction?
- What would you monitor after deployment if leadership accepted the residual risk?

## Common instructor corrections

- Do not let the lab become a checklist exercise. Students must explain why each weakness matters to release integrity.
- Do not reward generic advice without evidence. Every strong finding should point to a file, field, or workflow in the pack.
- Do not make perfect security the target. The target is a defensible release decision with prioritized remediation.

## Expected student output

A strong submission includes:

- release recommendation
- prioritized findings
- evidence references
- remediation sequence
- residual risk
- owner or decision point
- one executive-readable summary
