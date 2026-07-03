# Module 06 Lab Path: RAG Security

## Role in the 40-hour course

Module 06 uses BrokenPilot as the primary runnable RAG target. The core learning path is retrieval authorization, source trust, and indirect prompt injection through retrieved documents.

## Runnable path

- BrokenPilot retrieval authorization toggle
- BrokenPilot indirect prompt injection through retrieved documents
- BrokenPilot standalone Module 06 lab

## Reasoning path

- Design metadata filters and authorization checks before retrieval results enter the model context
- Explain why vector similarity is not authorization

## Graded deliverable

A retrieval security design note with tenant filters, role/user checks, logging expectations, validation tests, and residual risk.

## Keep central

- Observable cross-tenant retrieval failure and fix
- Source trust and context construction discussion

## Avoid

- Do not maintain a second paper-only RAG path that duplicates BrokenPilot
- Do not present prompt instructions as a substitute for retrieval authorization

## Instructor note

Use this file as the first stop when deciding what to run live, what to assign as self-study, and what to grade. If a lab cannot produce observable vulnerable and controlled behavior, treat it as a reasoning lab and grade the artifact instead of pretending it is runnable.
