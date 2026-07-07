from __future__ import annotations

from fastapi import FastAPI

from app import audit
from app.orchestrator import orchestrate
from app.registry import list_descriptors
from app.schemas import OrchestrationRequest, OrchestrationResponse

app = FastAPI(title="BrokenPilot v2 Minimal Skeleton", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "app": "brokenpilot-v2"}


@app.get("/agents")
def agents() -> list[dict[str, object]]:
    return [descriptor.model_dump() for descriptor in list_descriptors()]


@app.get("/mcp/descriptors")
def mcp_descriptors() -> list[dict[str, object]]:
    return [descriptor.model_dump() for descriptor in list_descriptors()]


@app.get("/audit")
def audit_events() -> list[dict[str, object]]:
    return audit.list_events()


@app.post("/reset")
def reset() -> dict[str, str]:
    audit.reset()
    return {"status": "reset"}


@app.post("/orchestrate", response_model=OrchestrationResponse)
def orchestrate_endpoint(request: OrchestrationRequest) -> OrchestrationResponse:
    return orchestrate(request)
