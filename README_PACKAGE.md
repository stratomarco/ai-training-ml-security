# Release Cleanup Phase 3 Package

This package cleans the workflow and validation layer for the v1.1-dev branch.

It does not change course content, lab behavior, MkDocs navigation, or student-facing prose.

## Purpose

During content buildout the repository accumulated strict release checks too early. This package resets the validation baseline to what should be protected now:

- repository structure
- content readiness
- lab target presence
- BrokenPilot tests
- toy-classifier tests
- non-strict MkDocs build as a smoke test only

Strict MkDocs navigation and final release checks remain postponed until the final release-hardening phase.
