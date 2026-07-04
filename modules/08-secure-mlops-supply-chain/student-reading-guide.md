# Student Reading Guide: Module 08: Secure MLOps and AI Supply Chain

## What this module is really about

MLOps supply-chain security risk is usually visible in evidence: missing provenance, mutable artifacts, unpinned dependencies, weak promotion gates, unsafe notebooks, and registry metadata that cannot prove what was trained, tested, approved, and deployed.

## Question to keep in mind

Can the team prove where this model came from, what data and code produced it, who approved it, and how to roll it back?

## Decisions students must learn to make

- Decide which artifacts require hashes, signatures, review, and promotion gates.
- Separate experiment convenience from production promotion requirements.
- Choose what evidence is required before a model moves between environments.
- Explain supply-chain risk to leadership without exaggerating it into a generic breach story.

## Lab or exercise connection

Use the MLOps evidence-pack review. It is intentionally a reasoning lab because realistic supply-chain review is evidence review, not a fake pipeline demo.

## What a strong submission looks like

A strong submission cites specific evidence-pack files, identifies concrete integrity gaps, recommends promotion controls, and states what residual risk remains after the controls.

## Common misreadings to avoid

- Treating accuracy metrics as deployment approval.
- Fixing only dependencies while ignoring artifact identity and promotion rules.
- Equating a registry entry with trustworthy provenance.

## Exit ticket

Name three pieces of evidence you would require before production promotion.
