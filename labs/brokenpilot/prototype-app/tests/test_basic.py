from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def reset():
    response = client.post("/reset")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_users():
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()["users"]
    assert any(user["id"] == "alice" for user in users)


def test_vulnerable_retrieval_default_allows_cross_tenant_context():
    response = client.post(
        "/retrieve",
        json={"user_id": "eve", "query": "payment api credential rotation token", "top_k": 3},
    )
    assert response.status_code == 200
    doc_ids = [doc["id"] for doc in response.json()["documents"]]
    assert "DOC-002" in doc_ids


def test_indirect_prompt_injection_default_mode():
    response = client.post(
        "/chat",
        json={"user_id": "alice", "message": "vendor onboarding incident token runbook", "top_k": 4},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "vulnerable"
    assert "VULNERABLE_BEHAVIOR_DETECTED" in body["answer"]


def test_tool_update_default_allows_cross_tenant_ticket_update():
    reset()
    response = client.post(
        "/tools/update-ticket",
        json={
            "user_id": "alice",
            "ticket_id": "TCK-2001",
            "status": "closed",
            "note": "training update from alpha user to beta ticket",
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["ticket"]["status"] == "closed"
    assert body["authorization_decision"] == "not_checked"


def test_tool_authz_blocks_cross_tenant_ticket_update(monkeypatch):
    reset()
    monkeypatch.setenv("ENABLE_TOOL_AUTHZ", "true")
    response = client.post(
        "/tools/update-ticket",
        json={
            "user_id": "alice",
            "ticket_id": "TCK-2001",
            "status": "closed",
            "note": "should be blocked by tenant control",
        },
    )
    assert response.status_code == 403
    assert response.json()["detail"]["error"] == "tool_authorization_denied"
    monkeypatch.delenv("ENABLE_TOOL_AUTHZ", raising=False)


def test_agent_run_default_executes_tool_call():
    reset()
    response = client.post(
        "/agent/run",
        json={"user_id": "alice", "goal": "Resolve the vendor onboarding issue and close TCK-2001"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["agent_decision"] == "tool_call_update_ticket"
    assert body["ticket"]["status"] == "closed"
