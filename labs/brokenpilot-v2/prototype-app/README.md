# BrokenPilot v2 Prototype App

This is the first runnable skeleton for the v2 agentic and MCP security track.

The skeleton is secure-by-default and intentionally boring. It establishes the runtime shape before adding vulnerable scenarios:

- an orchestrator agent
- a retrieval agent
- a ticket/action agent
- a shared tool broker
- an MCP-like descriptor registry
- message envelopes with correlation identifiers
- an audit trace across delegation

The current goal is not to demonstrate an attack. The current goal is to make the v2 architecture executable and testable before adding failure chains.

## Run locally

```powershell
cd labs\brokenpilot-v2\prototype-app
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload --port 8020
```

Open:

```text
http://127.0.0.1:8020/health
```

## Useful endpoints

- `GET /health`
- `GET /agents`
- `GET /mcp/descriptors`
- `GET /audit`
- `POST /orchestrate`

Example request:

```json
{
  "user_id": "alice",
  "tenant_id": "alpha",
  "task": "find the current deployment notes"
}
```

## Teaching status

This is not yet a student lab. It is the executable base for future v2 labs about:

- insecure inter-agent communication
- spoofed MCP descriptors
- rogue agent registration
- cascading delegation failure
- signed agent identity and descriptor pinning
- anti-replay controls
- tool-broker policy enforcement
