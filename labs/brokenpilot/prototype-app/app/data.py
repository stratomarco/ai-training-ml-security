from functools import lru_cache
from pathlib import Path
import json
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def _load_json(name: str) -> list[dict[str, Any]]:
    path = DATA_DIR / name
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


@lru_cache
def load_users() -> list[dict[str, Any]]:
    return _load_json("users.json")


@lru_cache
def load_documents() -> list[dict[str, Any]]:
    return _load_json("documents.json")


@lru_cache
def load_tickets() -> list[dict[str, Any]]:
    return _load_json("tickets.json")


def reset_tickets() -> list[dict[str, Any]]:
    load_tickets.cache_clear()
    return load_tickets()


def reset_documents() -> list[dict[str, Any]]:
    load_documents.cache_clear()
    return load_documents()


def get_user(user_id: str) -> dict[str, Any] | None:
    for user in load_users():
        if user["id"] == user_id:
            return user
    return None


def get_ticket(ticket_id: str) -> dict[str, Any] | None:
    for ticket in load_tickets():
        if ticket["id"] == ticket_id:
            return ticket
    return None


def create_ticket(*, user: dict[str, Any], title: str, summary: str) -> dict[str, Any]:
    next_number = max(int(ticket["id"].split("-")[1]) for ticket in load_tickets()) + 1
    ticket_id = f"TCK-{next_number:04d}"
    ticket = {
        "id": ticket_id,
        "tenant": user["tenant"],
        "title": title,
        "status": "open",
        "owner": user["id"],
        "summary": summary,
    }
    load_tickets().append(ticket)
    load_documents().append(
        {
            "id": f"DOC-{ticket_id}",
            "title": title,
            "tenant": user["tenant"],
            "visibility": "restricted",
            "classification": "internal",
            "allowed_roles": ["ops", "developer", "viewer", "contractor"],
            "allowed_users": [],
            "tags": ["ticket"],
            "body": summary,
            "source": "user_ticket",
            "source_ticket_id": ticket_id,
        }
    )
    return ticket.copy()


def update_ticket(ticket_id: str, *, status: str | None = None, note: str | None = None, actor: str | None = None) -> dict[str, Any] | None:
    ticket = get_ticket(ticket_id)
    if not ticket:
        return None
    if status:
        ticket["status"] = status
    if note:
        ticket.setdefault("notes", []).append({"actor": actor or "unknown", "note": note})
    return ticket
