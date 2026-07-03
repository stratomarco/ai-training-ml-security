# Module 05 Lab Path: LLM Application Security

## Role in the 40-hour course

Module 05 uses BrokenPilot for direct prompt injection, indirect prompt injection, and insecure output handling. DVAIA remains an optional external comparison lab, not a survival dependency.

## Runnable path

- BrokenPilot direct prompt injection lab
- BrokenPilot insecure output handling lab
- BrokenPilot standalone Module 05 lab

## Reasoning path

- Explain why prompt wording is not a security boundary
- Map the same root cause across user input, retrieved content, and downstream output sinks

## Graded deliverable

A Module 05 control note that identifies the trust boundary, shows the vulnerable and controlled behavior, recommends an architectural control, and states residual risk.

## Keep central

- Direct injection through user input
- Indirect injection through retrieved content
- Output handling through a downstream HTML sink

## Avoid

- Do not imply marker detection is a production control
- Do not grade students only on making the model misbehave

## Instructor note

Use this file as the first stop when deciding what to run live, what to assign as self-study, and what to grade. If a lab cannot produce observable vulnerable and controlled behavior, treat it as a reasoning lab and grade the artifact instead of pretending it is runnable.
