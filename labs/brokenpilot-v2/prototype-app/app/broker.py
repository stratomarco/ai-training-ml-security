from __future__ import annotations

from app.registry import get_descriptor
from app.schemas import BrokerDecision, MessageEnvelope


DEFAULT_CAPABILITY_BY_AGENT = {
    "retrieval-agent": "docs.search",
    "ticket-agent": "ticket.update",
}


def decide(envelope: MessageEnvelope) -> BrokerDecision:
    descriptor = get_descriptor(envelope.target_agent)
    if descriptor is None:
        return BrokerDecision(
            allowed=False,
            reason="unknown_target_agent",
            capability=envelope.requested_capability,
            target_agent=envelope.target_agent,
        )

    if not descriptor.trusted:
        return BrokerDecision(
            allowed=False,
            reason="untrusted_descriptor",
            capability=envelope.requested_capability,
            target_agent=envelope.target_agent,
        )

    capability = envelope.requested_capability or DEFAULT_CAPABILITY_BY_AGENT.get(envelope.target_agent)
    if capability not in descriptor.capabilities:
        return BrokerDecision(
            allowed=False,
            reason="capability_not_advertised_by_descriptor",
            capability=capability,
            target_agent=envelope.target_agent,
        )

    return BrokerDecision(
        allowed=True,
        reason="descriptor_and_capability_allowed",
        capability=capability,
        target_agent=envelope.target_agent,
    )
