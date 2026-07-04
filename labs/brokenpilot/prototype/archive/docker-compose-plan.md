# BrokenPilot Docker Compose Plan

This document defines how the first runnable BrokenPilot prototype should run locally.

## Goal

A student should be able to start the prototype with one command:

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:8080
```

## MVP compose services

Start with one service only.

```yaml
services:
  brokenpilot:
    build: .
    ports:
      - "8080:8080"
    environment:
      BROKENPILOT_MODE: vulnerable
      ENABLE_RETRIEVAL_AUTHZ: "false"
      ENABLE_TOOL_APPROVAL: "false"
      ENABLE_MEMORY_REVIEW: "false"
      ENABLE_TOOL_AUDIT: "true"
      ENABLE_OUTPUT_ENCODING: "false"
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
```

## Later optional services

Only add these after the one-container MVP works.

| Service | When to add |
|---|---|
| Chroma or Qdrant | When moving from keyword search to vector retrieval |
| Ollama | When adding optional real local LLM mode |
| SQLite volume | When JSON fixtures become limiting |
| Frontend container | When UI complexity justifies separation |

## Reset flow

The prototype must support reset.

Recommended commands:

```bash
docker compose down
python scripts/reset_lab.py
```

or container-only:

```bash
docker compose down -v
docker compose up --build
```

## Local-only warning

BrokenPilot is intentionally vulnerable.

The compose file should bind to localhost by default and documentation should warn students not to expose it to the internet.

## Windows note

Windows users should run Docker Desktop and PowerShell. The course should include equivalent commands:

```powershell
docker compose up --build
```

and cleanup:

```powershell
docker compose down
```
