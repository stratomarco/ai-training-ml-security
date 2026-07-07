from __future__ import annotations

from hashlib import sha256
from app.schemas import AgentDescriptor


def descriptor_hash(agent_id: str, capabilities: list[str]) -> str:
    material = agent_id + "|" + ",".join(sorted(capabilities))
    return sha256(material.encode("utf-8")).hexdigest()


DESCRIPTORS: dict[str, AgentDescriptor] = {
    "retrieval-agent": AgentDescriptor(
        agent_id="retrieval-agent",
        display_name="Retrieval Agent",
        role="Find tenant-scoped operational context.",
        capabilities=["docs.search", "docs.read"],
        descriptor_id="mcp-desc-retrieval-agent-v1",
        descriptor_hash=descriptor_hash("retrieval-agent", ["docs.search", "docs.read"]),
        trusted=True,
    ),
    "ticket-agent": AgentDescriptor(
        agent_id="ticket-agent",
        display_name="Ticket Action Agent",
        role="Prepare safe ticket updates through the tool broker.",
        capabilities=["ticket.read", "ticket.update"],
        descriptor_id="mcp-desc-ticket-agent-v1",
        descriptor_hash=descriptor_hash("ticket-agent", ["ticket.read", "ticket.update"]),
        trusted=True,
    ),
}


def list_descriptors() -> list[AgentDescriptor]:
    return list(DESCRIPTORS.values())


def get_descriptor(agent_id: str) -> AgentDescriptor | None:
    return DESCRIPTORS.get(agent_id)
