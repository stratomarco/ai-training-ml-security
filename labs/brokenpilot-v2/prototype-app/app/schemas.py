from __future__ import annotations

from typing import Any, Literal
from pydantic import BaseModel, Field


class MessageEnvelope(BaseModel):
    envelope_id: str
    trace_id: str
    source_agent: str
    target_agent: str
    tenant_id: str
    user_id: str
    task: str
    requested_capability: str | None = None
    sequence: int = 1


class AgentDescriptor(BaseModel):
    agent_id: str
    display_name: str
    role: str
    capabilities: list[str]
    descriptor_id: str
    descriptor_hash: str
    trusted: bool = True


class OrchestrationRequest(BaseModel):
    user_id: str = Field(min_length=1)
    tenant_id: str = Field(min_length=1)
    task: str = Field(min_length=1)
    requested_capability: str | None = None


class BrokerDecision(BaseModel):
    allowed: bool
    reason: str
    capability: str | None = None
    target_agent: str | None = None


class AgentResult(BaseModel):
    agent_id: str
    status: Literal["completed", "denied"]
    summary: str
    evidence: dict[str, Any] = Field(default_factory=dict)


class OrchestrationResponse(BaseModel):
    trace_id: str
    selected_agent: str | None
    broker_decision: BrokerDecision
    result: AgentResult | None
    audit_event_count: int
