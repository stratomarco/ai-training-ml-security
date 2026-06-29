# DVAIA Module Mapping

This page maps course modules to DVAIA-backed hands-on validation. The goal is to make every DVAIA dependency explicit.

## Mapping table

| Course module | Course concept | DVAIA target area | Validation status | Notes |
|---|---|---|---|---|
| Module 05 | Direct prompt injection | Direct Injection panel | Not validated | Verify prompt bypass and evidence capture |
| Module 05 | Unsafe model output handling | Output/rendering behavior or generated payloads | Not validated | Validate exact DVAIA behavior before writing hard claims |
| Module 06 | Indirect prompt injection | RAG/document injection flow | Not validated | Highest priority validation item |
| Module 06 | Retrieval trust boundary | RAG settings/data reset | Not validated | Document exact ingestion/retrieval steps |
| Module 07 | Tool misuse | Agentic panel | Not validated | Verify available tools and dangerous-by-design behavior |
| Module 07 | Memory or multi-turn manipulation | Agentic or multi-turn behavior | Not validated | Validate persistence/reset behavior |
| Module 11 | Attack chaining | Multiple panels | Not validated | Use after Modules 05–07 are validated |

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

## Validation output format

Each validated lab should add a short block like this:

```text
Validated on: YYYY-MM-DD
DVAIA commit: <commit hash>
OS: Windows 11
Docker Desktop: <version>
Backend: OpenAI-only / Gemini-only / Ollama
Model: <model>
Panel: <panel name>
Expected behavior reproduced: yes/no
Known issues: <notes>
```
