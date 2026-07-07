from __future__ import annotations

from app.schemas import AgentResult, MessageEnvelope


def run_retrieval_agent(envelope: MessageEnvelope) -> AgentResult:
    return AgentResult(
        agent_id="retrieval-agent",
        status="completed",
        summary=f"Found tenant-scoped context for tenant '{envelope.tenant_id}'.",
        evidence={
            "tenant_id": envelope.tenant_id,
            "documents": ["deployment-notes", "runbook-summary"],
        },
    )


def run_ticket_agent(envelope: MessageEnvelope) -> AgentResult:
    return AgentResult(
        agent_id="ticket-agent",
        status="completed",
        summary="Prepared ticket update through the broker-controlled action path.",
        evidence={
            "tenant_id": envelope.tenant_id,
            "ticket_action": "prepare_update",
            "requires_approval_for_state_change": True,
        },
    )


def dispatch(envelope: MessageEnvelope) -> AgentResult:
    if envelope.target_agent == "retrieval-agent":
        return run_retrieval_agent(envelope)
    if envelope.target_agent == "ticket-agent":
        return run_ticket_agent(envelope)
    return AgentResult(
        agent_id=envelope.target_agent,
        status="denied",
        summary="Unknown agent; no dispatch performed.",
    )
