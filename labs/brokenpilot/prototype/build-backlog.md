# BrokenPilot Prototype Build Backlog

This backlog tracks the future implementation work for the minimal runnable BrokenPilot prototype.

## Phase 0 — Design package

- [x] Prototype README
- [x] Architecture design
- [x] API contract
- [x] Fake data plan
- [x] Mock LLM plan
- [x] Vulnerability implementation plan
- [x] Control toggle plan
- [x] Docker Compose plan
- [x] Student lab flow
- [x] Instructor runbook
- [x] Safety notes

## Phase 1 — Skeleton app

- [ ] Create `brokenpilot-prototype/` application folder
- [ ] Add FastAPI app skeleton
- [ ] Add static UI or simple HTML template
- [ ] Add `/health` endpoint
- [ ] Add fake user selector
- [ ] Add JSON fixture loading
- [ ] Add reset script
- [ ] Add Dockerfile
- [ ] Add Docker Compose file

## Phase 2 — Retrieval and chat

- [ ] Add `/retrieve` endpoint
- [ ] Add keyword retrieval over fake documents
- [ ] Add `/chat` endpoint
- [ ] Add mock LLM provider
- [ ] Show retrieved document IDs in response
- [ ] Add vulnerable-mode retrieval behavior
- [ ] Add hardened retrieval authorization toggle

## Phase 3 — Tool execution

- [ ] Add fake ticket store
- [ ] Add `/tools/tickets/update` endpoint
- [ ] Add vulnerable tool execution path
- [ ] Add tool permission matrix
- [ ] Add approval gate toggle
- [ ] Add ticket before/after display

## Phase 4 — Memory

- [ ] Add `/memory/write` endpoint
- [ ] Add memory fixture store
- [ ] Add vulnerable direct memory write path
- [ ] Add memory review toggle
- [ ] Add memory provenance fields

## Phase 5 — Audit and evidence

- [ ] Add JSONL audit log
- [ ] Log retrieval document IDs
- [ ] Log tool intents
- [ ] Log policy decisions
- [ ] Add `/audit` endpoint
- [ ] Add evidence export helper

## Phase 6 — Labs and docs

- [ ] Add startup instructions
- [ ] Add Module 06 BrokenPilot hands-on lab
- [ ] Add Module 07 BrokenPilot hands-on lab
- [ ] Add Module 12 runnable capstone lab
- [ ] Add troubleshooting notes
- [ ] Add instructor demo script

## Phase 7 — Optional enhancements

- [ ] Add Chroma or Qdrant retrieval option
- [ ] Add Ollama local real-LLM mode
- [ ] Add OpenAI-compatible endpoint option
- [ ] Add automated tests
- [ ] Add GitHub Actions smoke test

## First implementation rule

Do not build everything.

The first implementation is successful when it can demonstrate:

1. Indirect prompt injection through retrieved content.
2. Unauthorized retrieval.
3. Tool confused deputy.
4. A control toggle that blocks at least one failure.
5. An audit log entry that supports a student finding.
