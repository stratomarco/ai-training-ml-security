# Student Reading Guide: Module 04: BIML Architectural Risk Analysis

## What this module is really about

BIML-style analysis asks students to reason before testing. The goal is to find structural security risk early, when it is cheaper to change the architecture than to patch symptoms after launch.

## Question to keep in mind

What can go wrong because of the architecture, even if the model appears to perform well in normal tests?

## Decisions students must learn to make

- Choose which components and trust boundaries deserve review depth.
- Turn abuse cases into architecture changes, not generic warnings.
- Prioritize risks by consequence, exposure, and control feasibility.
- Decide which assumptions must be validated before launch.

## Lab or exercise connection

Use the DocOps architecture review lab as a reasoning lab. The deliverable is an architecture risk review with clear findings, recommended controls, and explicit residual risk.

## What a strong submission looks like

A strong submission connects a system path to a failure mode, names a concrete control, and explains how the team would know the control works.

## Common misreadings to avoid

- Treating the exercise like a checklist completion task.
- Writing risk statements that do not point to a system path.
- Proposing policy-only fixes for architecture-level failures.

## Exit ticket

Write one architecture finding in this shape: path, failure, consequence, control, validation.
