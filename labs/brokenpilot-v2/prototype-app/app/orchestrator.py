from __future__ import annotations

from uuid import uuid4

from app import audit
from app.agents import dispatch
from app.broker import decide
from app.registry import get_descriptor
from app.schemas import MessageEnvelope, OrchestrationRequest, OrchestrationResponse


def select_agent(task: str) -> str:
    lowered = task.lower()
    if any(token in lowered for token in ["ticket", "update", "close", "assign"]):
        return "ticket-agent"
    return "retrieval-agent"


def orchestrate(request: OrchestrationRequest) -> OrchestrationResponse:
    trace_id = str(uuid4())
    target_agent = select_agent(request.task)

    envelope = MessageEnvelope(
        envelope_id=str(uuid4()),
        trace_id=trace_id,
        source_agent="orchestrator",
        target_agent=target_agent,
        tenant_id=request.tenant_id,
        user_id=request.user_id,
        task=request.task,
        requested_capability=request.requested_capability,
        sequence=1,
    )

    audit.record(
        "envelope_created",
        trace_id,
        envelope_id=envelope.envelope_id,
        source_agent=envelope.source_agent,
        target_agent=envelope.target_agent,
        tenant_id=envelope.tenant_id,
        user_id=envelope.user_id,
    )

    descriptor = get_descriptor(target_agent)
    audit.record(
        "descriptor_resolved",
        trace_id,
        target_agent=target_agent,
        descriptor_id=descriptor.descriptor_id if descriptor else None,
        descriptor_hash=descriptor.descriptor_hash if descriptor else None,
        trusted=descriptor.trusted if descriptor else False,
    )

    broker_decision = decide(envelope)
    audit.record(
        "tool_broker_decision",
        trace_id,
        allowed=broker_decision.allowed,
        reason=broker_decision.reason,
        capability=broker_decision.capability,
        target_agent=broker_decision.target_agent,
    )

    if not broker_decision.allowed:
        audit.record("orchestration_denied", trace_id, target_agent=target_agent)
        return OrchestrationResponse(
            trace_id=trace_id,
            selected_agent=target_agent,
            broker_decision=broker_decision,
            result=None,
            audit_event_count=len(audit.events_for_trace(trace_id)),
        )

    audit.record("agent_invoked", trace_id, target_agent=target_agent)
    result = dispatch(envelope)
    audit.record(
        "orchestration_completed",
        trace_id,
        target_agent=target_agent,
        result_status=result.status,
    )

    return OrchestrationResponse(
        trace_id=trace_id,
        selected_agent=target_agent,
        broker_decision=broker_decision,
        result=result,
        audit_event_count=len(audit.events_for_trace(trace_id)),
    )
