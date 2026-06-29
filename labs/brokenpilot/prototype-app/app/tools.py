from typing import Any
from fastapi import HTTPException

from .controls import Controls
from .data import update_ticket

APPROVAL_TOKEN = "APPROVED-FOR-LAB"
ALLOWED_TOOL_ROLES = {"ops"}


def update_ticket_tool(
    *,
    user: dict[str, Any],
    ticket: dict[str, Any],
    status: str,
    note: str,
    approval_token: str | None,
    controls: Controls,
) -> dict[str, Any]:
    """Update a ticket, intentionally vulnerable unless tool controls are enabled.

    Default lab behavior demonstrates a confused-deputy style failure: the tool trusts
    that the caller/model already made the correct authorization decision.
    """
    authorization_decision = "not_checked"
    approval_decision = "not_required"

    if controls.tool_authz:
        same_tenant = ticket.get("tenant") == user.get("tenant")
        allowed_role = user.get("role") in ALLOWED_TOOL_ROLES
        if not same_tenant or not allowed_role:
            raise HTTPException(
                status_code=403,
                detail={
                    "error": "tool_authorization_denied",
                    "reason": "User must be an ops user in the same tenant as the ticket.",
                    "user_tenant": user.get("tenant"),
                    "ticket_tenant": ticket.get("tenant"),
                    "user_role": user.get("role"),
                },
            )
        authorization_decision = "allowed_same_tenant_ops"

    if controls.tool_approval and status.lower() in {"closed", "resolved", "deleted"}:
        if approval_token != APPROVAL_TOKEN:
            raise HTTPException(
                status_code=403,
                detail={
                    "error": "approval_required",
                    "reason": "Destructive or workflow-ending ticket updates require human approval.",
                    "required_for_status": status,
                },
            )
        approval_decision = "approved_by_lab_token"

    updated = update_ticket(
        ticket["id"],
        status=status,
        note=note or "Updated by BrokenPilot training tool.",
        actor=user["id"],
    )
    return {
        "tool": "update_ticket",
        "result": "updated",
        "authorization_decision": authorization_decision,
        "approval_decision": approval_decision,
        "ticket": updated,
    }
