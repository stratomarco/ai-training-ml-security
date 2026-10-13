"""In-memory mock model registry for an offline credential-scope exercise.

This module never contacts a model hub, reads host credentials, or loads a model.
The tokens and revisions are lab-only simulation state that rotates on reset.
"""

from __future__ import annotations

from dataclasses import dataclass
from secrets import compare_digest, token_urlsafe

from fastapi import HTTPException

from .controls import Controls

MODEL_ID = "incident-triage-ranker"
APPROVED_REVISION = "approved-v1"
UNREVIEWED_REVISION = "unreviewed-v2"


@dataclass
class MockHub:
    active_revision: str
    read_token: str
    write_token: str


def _new_hub() -> MockHub:
    return MockHub(
        active_revision=APPROVED_REVISION,
        read_token="LAB-READ-" + token_urlsafe(18),
        write_token="LAB-WRITE-" + token_urlsafe(18),
    )


_hub = _new_hub()


def reset_hub() -> dict[str, str]:
    global _hub
    _hub = _new_hub()
    return model_state()


def model_state() -> dict[str, str]:
    return {"model_id": MODEL_ID, "active_revision": _hub.active_revision}


def diagnostics(controls: Controls) -> dict[str, str | None]:
    scope = "read" if controls.hub_least_privilege else "write"
    runtime_token = _hub.read_token if controls.hub_least_privilege else _hub.write_token
    return {
        "model_id": MODEL_ID,
        "runtime_credential_scope": scope,
        "debug_registry_token": None if controls.hub_diagnostic_redaction else runtime_token,
        "token_exposure": "redacted" if controls.hub_diagnostic_redaction else "exposed",
        "simulation": "lab-only fake credential",
    }


def promote_revision(*, revision: str, token: str | None) -> dict[str, str]:
    if not token:
        raise HTTPException(status_code=401, detail={"error": "mock_hub_token_missing"})
    if compare_digest(token, _hub.read_token):
        raise HTTPException(status_code=403, detail={"error": "mock_hub_write_scope_required"})
    if not compare_digest(token, _hub.write_token):
        raise HTTPException(status_code=401, detail={"error": "mock_hub_token_invalid"})
    if revision != UNREVIEWED_REVISION:
        raise HTTPException(status_code=422, detail={"error": "unknown_mock_revision"})
    _hub.active_revision = revision
    return model_state()
