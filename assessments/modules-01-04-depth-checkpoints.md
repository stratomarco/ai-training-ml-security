# Modules 01 to 04 Depth Checkpoints

## Purpose

These checkpoints verify that students can apply the foundation before moving into advanced labs.

## Checkpoint 1: Boundary sentence

Prompt: In one paragraph, explain why a model refusal is not the same as a security control.

Strong answer: names a security property, identifies the enforcement point outside the model, and gives a validation example.

Weak answer: says the model should be prompted better.

## Checkpoint 2: Architecture sketch

Prompt: Draw or describe an AI assistant architecture that includes user input, retrieval, model, tool broker, output sink, logs, and artifact promotion path.

Strong answer: marks trust boundaries and names controls at each boundary.

Weak answer: shows only user, model, and answer.

## Checkpoint 3: OWASP ML finding

Prompt: Choose one OWASP ML category and write a finding with evidence, root cause, control, validation, and residual risk.

Strong answer: maps the category to a concrete failure path.

Weak answer: only names the category.

## Checkpoint 4: Architecture risk recommendation

Prompt: Given a design with mixed-trust documents and future write actions, recommend whether to proceed, pilot, or delay.

Strong answer: separates read-only risk from write-action risk and defines required controls.

Weak answer: says to add guardrails without specifying enforcement.
