# DVAIA Module Mapping

This page maps course modules to DVAIA-backed hands-on validation. The goal is to make every DVAIA dependency explicit.

## Validation baseline

Validated by: Marco Constantino  
Validation date: 2026-06-29  
Host OS: Windows / PowerShell  
DVAIA commit: `23c115252554caa445c0e6ba28641c1110c118e1`  
Docker version: `Docker version 29.5.3, build d1c06ef`  
Docker Compose version: `Docker Compose version v5.1.4`  
Run mode: Local mode  
Backend: Local / Ollama  
Default URL: `http://127.0.0.1:5000`

## Mapping table

| Course module | Course concept | DVAIA-backed validation | Validation status | Next refinement |
|---|---|---|---|---|
| Module 05 | Direct prompt injection | Direct model-behavior testing in DVAIA | Validated locally | Add exact instructor walkthrough and expected observation |
| Module 05 | Unsafe model output handling | Output/payload behavior where available in DVAIA | Validated locally | Add screenshot/transcript guidance |
| Module 06 | Indirect prompt injection | RAG/document/context-based manipulation where supported | Validated locally | Record exact setup and reset steps |
| Module 06 | Retrieval trust boundary | RAG-style data/source trust behavior where supported | Validated locally | Add mitigation checklist tied to observed behavior |
| Module 07 | Tool misuse | Agent/tool behavior where supported by local DVAIA version | Validated locally | Decide which parts stay DVAIA-backed and which move to BrokenPilot prototype |
| Module 07 | Memory or multi-turn manipulation | Multi-turn/agentic behavior where supported | Validated locally | Record persistence/reset assumptions |
| Module 11 | Attack chaining | Multi-step validation across DVAIA-backed scenarios | Validated locally | Add a guided red-team path and evidence log example |

## What this course should provide

For every validated DVAIA-backed lab, this course should provide:

- Learning objective
- Prerequisites
- Exact DVAIA version or commit tested
- Setup command
- Lab setup verification
- Guided attack task
- Expected observation
- Root cause explanation
- Mitigation discussion
- Report template
- Cleanup/reset instructions

## What DVAIA provides

DVAIA provides the vulnerable target environment, panels, backend toggles, and local/cloud model integration. This course should not duplicate DVAIA's upstream documentation; it should link to it and add course-specific guidance.

## Current status

DVAIA is no longer only a theoretical prerequisite. It has been validated locally as a hands-on lab dependency for the relevant course modules.

The course still needs more precise per-lab instructor walkthroughs. This is the next quality task.

## Validation output format for future lab updates

Each validated lab should add a short block like this:

```text
Validated on: YYYY-MM-DD
DVAIA commit: 23c115252554caa445c0e6ba28641c1110c118e1
OS: Windows / PowerShell
Docker: Docker version 29.5.3, build d1c06ef
Docker Compose: Docker Compose version v5.1.4
Backend: Local / Ollama
Panel or feature: <exact DVAIA area>
Expected behavior reproduced: yes
Known issues: <notes>
Cleanup: <command or reset procedure>
```
