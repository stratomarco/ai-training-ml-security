# DVAIA Local Validation Plan

This page defines how to validate DVAIA before using it in this course. The purpose is to move DVAIA from a linked prerequisite to a verified lab dependency.

!!! warning "Scope"
    This course does not vendor, fork, or redistribute DVAIA. Students and instructors should install DVAIA from the upstream project and follow the upstream license and usage guidance.

## Why this matters

A lab guide is only useful if the target environment actually runs and the expected behavior can be observed. Before teaching any DVAIA-backed module, instructors should validate:

1. The app starts locally.
2. The required model backend works.
3. The relevant attack panel exists.
4. The expected vulnerable behavior can be reproduced.
5. Evidence can be captured.
6. Cleanup/reset works.

## Upstream project facts to verify

As of the current upstream README, DVAIA describes itself as an interactive web interface for manual LLM security testing, similar to DVWA but focused on LLM vulnerabilities. It supports local Ollama models, Google Gemini, or OpenAI cloud backends and runs as a Flask app on `http://127.0.0.1:5000` by default.

The upstream repository documents Docker Compose as the recommended quick-start path and includes Windows PowerShell support through `run_docker.ps1`.

## Recommended validation environments

| Environment | Priority | Notes |
|---|---:|---|
| Windows 11 + Docker Desktop + PowerShell + cloud backend | High | Lowest friction for many students |
| Windows 11 + Docker Desktop + WSL2 + Ollama profile | Medium | Closer to Linux path but heavier |
| Linux/macOS + Docker Compose + Ollama profile | Medium | Good instructor environment |
| Python virtual environment local dev | Low | Useful for contributors, not first-time students |

## Minimal Windows PowerShell validation path

Use this path first because it avoids local model downloads.

```powershell
git clone https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application.git
cd DVAIA-Damn-Vulnerable-AI-Application
copy .env.example .env
```

Edit `.env` and configure one cloud backend, for example OpenAI or Gemini. Then run the PowerShell helper according to the upstream instructions:

```powershell
.\run_docker.ps1 -OpenAIOnly
```

or:

```powershell
.\run_docker.ps1 -GeminiOnly
```

Then open:

```text
http://127.0.0.1:5000
```

## Local Ollama validation path

Only use this path if the machine has enough disk, RAM, and time for local model downloads.

```powershell
git clone https://github.com/airtasystems/DVAIA-Damn-Vulnerable-AI-Application.git
cd DVAIA-Damn-Vulnerable-AI-Application
copy .env.example .env
.\run_docker.ps1 -Local
```

Expected constraints:

- Docker Desktop must be running.
- First start may take several minutes.
- Local models can require significant disk space.
- Some panels may need specific models or settings.

## Validation checklist

| Check | Expected result | Status |
|---|---|---|
| Repository clones | No authentication required | TODO |
| `.env` can be created | `.env` exists and contains backend settings | TODO |
| Docker build starts | Containers build without fatal errors | TODO |
| App starts | Browser opens `127.0.0.1:5000` | TODO |
| Settings page works | Backend can be selected | TODO |
| Direct Injection panel works | Prompt produces model response | TODO |
| RAG/indirect panel works | Retrieved or uploaded content can affect response | TODO |
| Agentic panel works | Tool behavior can be observed | TODO |
| Reset works | Lab data can be reset between students | TODO |
| Evidence capture works | Screenshots/logs can be collected | TODO |

## Module validation matrix

| Course module | DVAIA area to validate | Required for v1.1? |
|---|---|---:|
| Module 05 — LLM Application Security | Direct injection, insecure output, model behavior testing | Yes |
| Module 06 — RAG Security | Indirect prompt injection, document/RAG behavior | Yes |
| Module 07 — Agent and Tool Security | Agentic panel and tool behavior | Yes |
| Module 11 — AI Red Team Methodology | Evidence capture and attack chaining | Yes |
| Module 12 — BrokenPilot Capstone | Not DVAIA-backed; separate prototype needed | No |

## Evidence instructors should collect

For each validated lab, save:

- Date tested
- DVAIA commit hash
- Operating system
- Docker version
- Backend used
- Model used
- Exact command used
- Screenshot of app running
- Screenshot or transcript of vulnerable behavior
- Known issues
- Cleanup command

## Troubleshooting notes to fill after validation

| Problem | Likely cause | Fix |
|---|---|---|
| Docker command fails | Docker Desktop not running | Start Docker Desktop |
| Port 5000 unavailable | Another service bound to port | Change `PORT` in `.env` if supported |
| Model call fails | Missing API key or backend setting | Recheck `.env` and Settings page |
| Ollama profile slow | Model download | Use cloud-only mode for class |
| RAG panel fails | Embedding backend not configured | Check backend-specific embedding settings |

## Course rule

A DVAIA-backed lab should not be marked as "validated" until an instructor has reproduced the expected behavior locally and recorded the environment details.
