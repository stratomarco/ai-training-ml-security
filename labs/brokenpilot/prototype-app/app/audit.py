from datetime import datetime, timezone
from typing import Any

_EVENTS: list[dict[str, Any]] = []


def record(event_type: str, details: dict[str, Any]) -> None:
    _EVENTS.append(
        {
            "ts": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "details": details,
        }
    )


def list_events() -> list[dict[str, Any]]:
    return list(_EVENTS)


def clear_events() -> None:
    _EVENTS.clear()
