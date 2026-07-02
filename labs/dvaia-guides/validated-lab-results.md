# DVAIA Validated Lab Results

This page records the first local validation pass for DVAIA-backed labs.

## Validation baseline

Validated by: Marco Constantino  
Validation date: 2026-06-29  
Host OS: Windows / PowerShell  
Course repo commit: `1dabb81a574ca7dd420ef7ac2673832583189b13`  
DVAIA commit: `23c115252554caa445c0e6ba28641c1110c118e1`  
Docker version: `Docker version 29.5.3, build d1c06ef`  
Docker Compose version: `Docker Compose version v5.1.4`  
Run mode: Local mode  
Backend: Local / Ollama  
Default URL: `http://127.0.0.1:5000`

## Result summary

| Area | Status | Course impact |
|---|---|---|
| DVAIA starts locally | Validated | Students can run the lab dependency locally |
| Module 05 DVAIA-backed exercises | Validated | LLM application security can include hands-on tasks |
| Module 06 DVAIA-backed exercises | Validated | RAG/indirect prompt injection can include hands-on tasks where supported |
| Module 07 DVAIA-backed exercises | Validated | Agent/tool topics can use DVAIA where supported, with BrokenPilot planned for deeper coverage |
| Module 11 DVAIA-backed attack chaining | Validated | Red-team methodology can use DVAIA as an early target before BrokenPilot |

## Instructor note

This validation confirms that the DVAIA-backed course direction is practical on at least one Windows + Docker Desktop environment.

Initial per-lab walkthroughs have now been added for Modules 05, 06, 07, and 11. The next improvement should enrich them with exact local screenshots or response transcripts captured during an instructor run. Each walkthrough should continue to include:

- Exact DVAIA feature or panel
- Initial state
- Student task
- Expected observation
- Root cause explanation
- Evidence to capture
- Cleanup/reset step
- Discussion prompts
- Mitigation exercise

## Added walkthroughs

1. `module-05-direct-prompt-injection-walkthrough.md`
2. `module-06-rag-indirect-prompt-injection-walkthrough.md`
3. `module-07-agent-tool-behavior-walkthrough.md`
4. `module-11-dvaia-red-team-mini-assessment.md`
5. `course-templates/dvaia-evidence-log-template.md`

## Safety reminder

DVAIA is intentionally vulnerable. It should only run on a local, controlled training machine.
