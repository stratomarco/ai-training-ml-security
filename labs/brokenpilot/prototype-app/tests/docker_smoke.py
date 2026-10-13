"""Exercise the published loopback API of a running Docker Compose lab."""

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


def main() -> None:
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
    print("BrokenPilot Docker smoke passed")


if __name__ == "__main__":
    main()
