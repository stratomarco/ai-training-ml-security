from __future__ import annotations

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def setup_function() -> None:
    client.post("/reset")


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_descriptors_have_identity_and_hashes() -> None:
    response = client.get("/mcp/descriptors")
    assert response.status_code == 200
    descriptors = response.json()
    assert {item["agent_id"] for item in descriptors} == {"retrieval-agent", "ticket-agent"}
    for descriptor in descriptors:
        assert descriptor["trusted"] is True
        assert descriptor["descriptor_id"].startswith("mcp-desc-")
        assert len(descriptor["descriptor_hash"]) == 64
        assert descriptor["capabilities"]


def test_orchestrator_routes_document_task_to_retrieval_agent() -> None:
    response = client.post(
        "/orchestrate",
        json={"user_id": "alice", "tenant_id": "alpha", "task": "find deployment notes"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["selected_agent"] == "retrieval-agent"
    assert body["broker_decision"]["allowed"] is True
    assert body["result"]["status"] == "completed"
    assert body["result"]["evidence"]["tenant_id"] == "alpha"


def test_orchestrator_routes_ticket_task_to_ticket_agent() -> None:
    response = client.post(
        "/orchestrate",
        json={"user_id": "alice", "tenant_id": "alpha", "task": "prepare a ticket update"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["selected_agent"] == "ticket-agent"
    assert body["broker_decision"]["capability"] == "ticket.update"
    assert body["result"]["evidence"]["requires_approval_for_state_change"] is True


def test_broker_denies_capability_not_in_descriptor() -> None:
    response = client.post(
        "/orchestrate",
        json={
            "user_id": "alice",
            "tenant_id": "alpha",
            "task": "find deployment notes",
            "requested_capability": "ticket.update",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["selected_agent"] == "retrieval-agent"
    assert body["broker_decision"]["allowed"] is False
    assert body["broker_decision"]["reason"] == "capability_not_advertised_by_descriptor"
    assert body["result"] is None


def test_audit_trace_records_delegation_path() -> None:
    response = client.post(
        "/orchestrate",
        json={"user_id": "alice", "tenant_id": "alpha", "task": "prepare a ticket update"},
    )
    trace_id = response.json()["trace_id"]

    audit_response = client.get("/audit")
    events = [event for event in audit_response.json() if event["trace_id"] == trace_id]
    event_types = [event["event_type"] for event in events]

    assert event_types == [
        "envelope_created",
        "descriptor_resolved",
        "tool_broker_decision",
        "agent_invoked",
        "orchestration_completed",
    ]
