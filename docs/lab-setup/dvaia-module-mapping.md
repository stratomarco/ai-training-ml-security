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
| Module 05 | Direct prompt injection | Direct model-behavior testing in DVAIA | Validated locally | Walkthrough added: `labs/dvaia-guides/module-05-direct-prompt-injection-walkthrough.md` |
| Module 05 | Unsafe model output handling | Output/payload behavior where available in DVAIA | Validated locally | Use DVAIA evidence log template; add screenshots only where locally captured |
| Module 06 | Indirect prompt injection | RAG/document/context-based manipulation where supported | Validated locally | Walkthrough added: `labs/dvaia-guides/module-06-rag-indirect-prompt-injection-walkthrough.md` |
| Module 06 | Retrieval trust boundary | RAG-style data/source trust behavior where supported | Validated locally | Covered in Module 06 walkthrough mitigation section |
| Module 07 | Tool misuse | Agent/tool behavior where supported by local DVAIA version | Validated locally | Walkthrough added: `labs/dvaia-guides/module-07-agent-tool-behavior-walkthrough.md`; BrokenPilot prototype remains future work |
| Module 07 | Memory or multi-turn manipulation | Multi-turn/agentic behavior where supported | Validated locally | Covered as hybrid lab; exact persistence behavior should be recorded when observed |
| Module 11 | Attack chaining | Multi-step validation across DVAIA-backed scenarios | Validated locally | Mini-assessment added: `labs/dvaia-guides/module-11-dvaia-red-team-mini-assessment.md` and `course-templates/dvaia-evidence-log-template.md` |

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

Initial validated walkthroughs have been added for Modules 05, 06, 07, and 11. The next refinement is to add exact screenshots or transcripts from a local instructor run without inventing UI labels or responses.

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
