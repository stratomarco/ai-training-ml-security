"""Exercise both Compose teaching profiles through the published loopback API."""

import argparse
import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE = "http://127.0.0.1:8010"


def request(path: str, *, token: str | None = None, body: dict | None = None) -> dict:
    headers = {"Content-Type": "application/json"} if body is not None else {}
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    payload = json.dumps(body).encode() if body is not None else None
    with urlopen(Request(BASE + path, data=payload, headers=headers), timeout=5) as response:
        return json.load(response)


def vulnerable_profile() -> None:
    assert request("/health")["status"] == "ok"
    assert request("/hub/model")["active_revision"] == "approved-v1"
    diagnostic = request("/hub/diagnostics")
    assert diagnostic["runtime_credential_scope"] == "write"
    token = diagnostic["debug_registry_token"]
    assert token.startswith("LAB-WRITE-")
    promoted = request("/hub/promote", token=token, body={"revision": "unreviewed-v2"})
    assert promoted["model"]["active_revision"] == "unreviewed-v2"
    assert request("/reset", body={})["mock_hub"]["active_revision"] == "approved-v1"
    try:
        request("/hub/promote", token=token, body={"revision": "unreviewed-v2"})
    except HTTPError as error:
        assert error.code == 401
    else:
        raise AssertionError("A token from before reset still works")


def controlled_profile() -> None:
    controls = request("/controls")
    expected = {
        "ENABLE_RETRIEVAL_AUTHZ",
        "ENABLE_PROMPT_INJECTION_FILTER",
        "ENABLE_TOOL_AUTHZ",
        "ENABLE_TOOL_APPROVAL",
        "ENABLE_MEMORY_REVIEW",
        "ENABLE_MEMORY_ISOLATION",
        "ENABLE_OUTPUT_ENCODING",
        "ENABLE_AUDIT_LOG",
        "ENABLE_HUB_LEAST_PRIVILEGE",
        "ENABLE_HUB_DIAGNOSTIC_REDACTION",
    }
    assert all(controls[name] is True for name in expected)
    assert request("/hub/model")["active_revision"] == "approved-v1"
    diagnostic = request("/hub/diagnostics")
    assert diagnostic["runtime_credential_scope"] == "read"
    assert diagnostic["debug_registry_token"] is None

    documents = request(
        "/retrieve",
        body={"user_id": "eve", "query": "payment api credential rotation token", "top_k": 3},
    )["documents"]
    assert "DOC-002" not in {document["id"] for document in documents}

    try:
        request(
            "/tools/update-ticket",
            body={"user_id": "alice", "ticket_id": "TCK-2001", "status": "closed", "note": "lab check"},
        )
    except HTTPError as error:
        assert error.code == 403
        assert json.load(error)["detail"]["error"] == "tool_authorization_denied"
    else:
        raise AssertionError("Cross-tenant ticket update was allowed")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", choices=("vulnerable", "all-controls"))
    profile = parser.parse_args().profile
    if profile == "vulnerable":
        vulnerable_profile()
    else:
        controlled_profile()
    print(f"BrokenPilot Docker {profile} smoke passed")


if __name__ == "__main__":
    main()
