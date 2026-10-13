# Module 08 Lab Path: Secure MLOps and AI Supply Chain

## Role in the 40-hour course

Module 08 is intentionally a reasoning and evidence-review module. It should not be forced into BrokenPilot. Students inspect realistic supply-chain evidence and produce a concrete promotion-control review.

## Runnable path

- Optional [offline artifact-promotion gate](../../labs/mlops-supply-chain-labs/artifact-promotion/artifact-promotion-lab.md): compare approved, tampered, and unapproved fake artifacts without deserializing them.
- Optional [BrokenPilot Mock Hub](../../labs/brokenpilot/prototype-app/MOCK_HUB_LAB.md): compare a leaked write-scoped worker token with redaction and least privilege. This is a separate extension, not the primary Module 08 path.

## Reasoning path

- MLOps evidence-pack review lab
- Broken ML pipeline tabletop
- Model artifact provenance and promotion-gate review

## Practice deliverable

An MLOps supply-chain review memo with evidence, risk rating, required controls, validation checks, and a launch/pilot/delay recommendation.

## Keep central

- Artifact integrity
- Dependency pinning and lockfiles
- Dataset provenance
- Promotion gates and rollback

## Avoid

- Do not build a fake pipeline just to make the module runnable
- Do not reduce supply-chain review to package scanning only
- Do not load suspicious checkpoints or use real model-registry credentials in a student lab

## Instructor note

Use this file as the first stop when deciding what to run live and what to assign as self-study. If a lab cannot produce observable vulnerable and controlled behavior, treat it as a reasoning lab with a written artifact. Rubrics are optional feedback guidance.
