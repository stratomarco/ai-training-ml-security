# DVAIA Local Validation

This page records the local validation status for DVAIA as an external lab dependency for this course.

DVAIA is not vendored into this repository. It is used as an external vulnerable AI application for selected labs, especially in Modules 05, 06, 07, and 11.

!!! warning "Scope"
    This course does not vendor, fork, or redistribute DVAIA. Students and instructors should install DVAIA from the upstream project and follow the upstream license and usage guidance.

## Validation status

Status: **Validated locally**

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

## Startup validation

| Check | Expected result | Status |
|---|---|---|
| Repository clones | DVAIA can be cloned locally | Validated |
| `.env` can be created | `.env.example` can be copied to `.env` | Validated |
| Docker is available | `docker --version` returns successfully | Validated |
| Docker Compose is available | `docker compose version` returns successfully | Validated |
| Local mode starts | `run_docker.ps1 -Local` starts the environment | Validated |
| App starts | Browser can reach `http://127.0.0.1:5000` | Validated |
| DVAIA-backed course labs run | Relevant labs were tested locally | Validated |
| No blocking startup issue | No blocking issue observed during validation | Validated |

## Validated module coverage

| Course module | DVAIA-backed coverage | Validation status | Notes |
|---|---|---|---|
| Module 05 — LLM Application Security | Direct prompt injection and LLM application-security behavior | Validated locally | Use for first hands-on DVAIA exercise path |
| Module 06 — RAG Security | RAG / indirect prompt injection style exercises where supported by the local DVAIA environment | Validated locally | Use to move the module from tabletop-only to hands-on where applicable |
| Module 07 — Agent and Tool Security | Agent/tool-use behavior where supported by the local DVAIA environment | Validated locally | Some agent exercises may still require adjacent vulnerable-agent labs or BrokenPilot later |
| Module 11 — AI Red Team Methodology | Evidence capture and attack-chain practice across DVAIA-backed scenarios | Validated locally | Use after students complete Modules 05–07 |

## Course usage

DVAIA is now a **validated external lab dependency** for this course.

Students should install and run DVAIA locally before attempting DVAIA-backed labs in this course.

This course provides:

- Learning objectives
- Security explanations
- Lab framing
- Attack reasoning
- Mitigation guidance
- Reporting templates
- Discussion questions

DVAIA provides:

- The vulnerable AI application runtime
- The interactive lab target
- The local hands-on environment

## Validation notes

The local DVAIA environment is working and can be used to turn selected paper labs into validated hands-on labs.

The next improvement is to capture more precise instructor notes for each DVAIA-backed exercise:

1. Exact DVAIA panel or feature used
2. Exact setup steps
3. Expected visible behavior
4. Screenshot or transcript guidance
5. Reset/cleanup instructions
6. Known issues and workarounds
7. Mapping to OWASP / BIML / NIST / MITRE ATLAS where applicable

## Safety note

DVAIA is intentionally vulnerable. It should only be run locally in a controlled lab environment.

Do not expose the DVAIA service to the internet.  
Do not connect it to real internal systems.  
Do not use real customer data, production credentials, production tickets, or production tools.  
Do not reuse DVAIA configuration as a production pattern.
