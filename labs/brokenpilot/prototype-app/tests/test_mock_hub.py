from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app, base_url="http://localhost")


def reset() -> None:
    assert client.post("/reset").status_code == 200


def promote(token: str | None) -> object:
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return client.post("/hub/promote", json={"revision": "unreviewed-v2"}, headers=headers)


def test_vulnerable_worker_leaks_write_token_and_can_change_only_fake_state():
    reset()
    diagnostic = client.get("/hub/diagnostics").json()
    assert diagnostic["runtime_credential_scope"] == "write"
    assert diagnostic["debug_registry_token"].startswith("LAB-WRITE-")
    result = promote(diagnostic["debug_registry_token"])
    assert result.status_code == 200
    assert result.json()["model"]["active_revision"] == "unreviewed-v2"
    assert result.json()["simulation"] == "no artifact or real hub was modified"


def test_least_privilege_token_cannot_promote(monkeypatch):
    reset()
    monkeypatch.setenv("ENABLE_HUB_LEAST_PRIVILEGE", "true")
    diagnostic = client.get("/hub/diagnostics").json()
    assert diagnostic["runtime_credential_scope"] == "read"
    assert diagnostic["debug_registry_token"].startswith("LAB-READ-")
    result = promote(diagnostic["debug_registry_token"])
    assert result.status_code == 403
    assert result.json()["detail"]["error"] == "mock_hub_write_scope_required"
    assert client.get("/hub/model").json()["active_revision"] == "approved-v1"


def test_diagnostic_redaction_removes_token_but_does_not_change_scope(monkeypatch):
    reset()
    monkeypatch.setenv("ENABLE_HUB_DIAGNOSTIC_REDACTION", "true")
    diagnostic = client.get("/hub/diagnostics").json()
    assert diagnostic["runtime_credential_scope"] == "write"
    assert diagnostic["debug_registry_token"] is None
    assert diagnostic["token_exposure"] == "redacted"
    assert promote(None).status_code == 401


def test_reset_rotates_fake_tokens_and_audit_omits_them():
    reset()
    first_token = client.get("/hub/diagnostics").json()["debug_registry_token"]
    assert promote(first_token).status_code == 200
    events = client.get("/audit").json()["events"]
    assert len(events) >= 2
    assert first_token not in str(events)
    reset()
    assert promote(first_token).status_code == 401
    assert client.get("/hub/model").json()["active_revision"] == "approved-v1"


def test_invalid_and_oversized_tokens_do_not_change_registry():
    reset()
    assert promote("LAB-WRITE-invalid").status_code == 401
    assert promote("x" * 129).status_code == 401
    assert client.get("/hub/model").json()["active_revision"] == "approved-v1"
