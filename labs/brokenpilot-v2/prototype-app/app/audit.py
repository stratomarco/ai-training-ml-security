from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

_EVENTS: list[dict[str, Any]] = []


def record(event_type: str, trace_id: str, **fields: Any) -> dict[str, Any]:
    event = {
        "time": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "trace_id": trace_id,
        **fields,
    }
    _EVENTS.append(event)
    return event


def list_events() -> list[dict[str, Any]]:
    return list(_EVENTS)


def events_for_trace(trace_id: str) -> list[dict[str, Any]]:
    return [event for event in _EVENTS if event.get("trace_id") == trace_id]


def reset() -> None:
    _EVENTS.clear()
