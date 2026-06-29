from __future__ import annotations

from itertools import count
from typing import Any

from fastapi import HTTPException

from .controls import Controls

APPROVAL_TOKEN = "APPROVED-FOR-LAB"
_MEMORY: list[dict[str, Any]] = []
_IDS = count(1)


def reset_memory() -> list[dict[str, Any]]:
    _MEMORY.clear()
    return list_memory()


def list_memory() -> list[dict[str, Any]]:
    return [entry.copy() for entry in _MEMORY]


def add_memory_entry(
    *,
    user: dict[str, Any],
    content: str,
    scope: str,
    approval_token: str | None,
    controls: Controls,
) -> dict[str, Any]:
    normalized_scope = scope.lower().strip() or "global"
    if normalized_scope not in {"global", "tenant", "user"}:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "invalid_memory_scope",
                "allowed_scopes": ["global", "tenant", "user"],
            },
        )

    review_decision = "not_required"
    approved = True
    if controls.memory_review:
        approved = approval_token == APPROVAL_TOKEN
        review_decision = "approved_by_lab_token" if approved else "pending_review"

    entry = {
        "id": f"MEM-{next(_IDS):04d}",
        "created_by": user["id"],
        "creator_tenant": user["tenant"],
        "scope": normalized_scope,
        "content": content,
        "approved": approved,
        "review_decision": review_decision,
    }
    _MEMORY.append(entry)
    return entry.copy()


def visible_memory_for_user(*, user: dict[str, Any], controls: Controls) -> list[dict[str, Any]]:
    visible: list[dict[str, Any]] = []
    for entry in _MEMORY:
        if controls.memory_review and not entry.get("approved"):
            continue

        if controls.memory_isolation:
            if entry.get("scope") == "global":
                # In the hardened lab mode, global memories are not trusted as cross-tenant
                # instructions. They must be reviewed and re-scoped before use.
                continue
            if entry.get("scope") == "tenant" and entry.get("creator_tenant") != user.get("tenant"):
                continue
            if entry.get("scope") == "user" and entry.get("created_by") != user.get("id"):
                continue

        visible.append(entry.copy())
    return visible


def find_memory_instruction(memories: list[dict[str, Any]]) -> str | None:
    for entry in memories:
        content = entry.get("content", "")
        marker = "MEMORY_INSTRUCTION:"
        if marker in content:
            return content.split(marker, 1)[1].strip()
    return None
