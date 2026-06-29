import re
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .audit import clear_events, list_events, record
from .controls import Controls
from .data import get_ticket, get_user, load_documents, load_tickets, load_users, reset_tickets
from .memory import add_memory_entry, find_memory_instruction, list_memory, reset_memory, visible_memory_for_user
from .mock_llm import generate_answer
from .rag import retrieve_documents
from .schemas import AgentRunRequest, ChatRequest, MemoryAddRequest, RetrieveRequest, ToolUpdateTicketRequest
from .tools import update_ticket_tool

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
TICKET_RE = re.compile(r"\bTCK-\d{4}\b", re.IGNORECASE)

app = FastAPI(
    title="BrokenPilot Prototype",
    description="Minimal intentionally vulnerable AI application for ML Security training.",
    version="0.3.0",
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def _public_user(user: dict) -> dict:
    return {
        "id": user["id"],
        "display_name": user["display_name"],
        "tenant": user["tenant"],
        "role": user["role"],
    }


def _status_from_goal(goal: str) -> str:
    lowered = goal.lower()
    if "close" in lowered or "resolve" in lowered:
        return "closed"
    if "escalate" in lowered:
        return "escalated"
    return "updated"


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    controls = Controls.from_env()
    return {
        "status": "ok",
        "app": "brokenpilot-prototype",
        "version": "0.3.0",
        "controls": controls.as_dict(),
    }


@app.get("/controls")
def controls():
    return Controls.from_env().as_dict()


@app.get("/users")
def users():
    return {"users": [_public_user(user) for user in load_users()]}


@app.get("/tickets")
def tickets():
    return {"tickets": load_tickets()}


@app.get("/audit")
def audit_events():
    return {"events": list_events()}


@app.post("/reset")
def reset_lab_state():
    reset_tickets()
    clear_events()
    reset_memory()
    return {"status": "reset", "tickets": load_tickets(), "memory": list_memory(), "audit_events": list_events()}


@app.get("/memory")
def memory_entries():
    return {"memory": list_memory()}


@app.post("/memory/add")
def memory_add(request: MemoryAddRequest):
    user = get_user(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Unknown user_id: {request.user_id}")

    controls = Controls.from_env()
    entry = add_memory_entry(
        user=user,
        content=request.content,
        scope=request.scope,
        approval_token=request.approval_token,
        controls=controls,
    )

    if controls.audit_log:
        record(
            "memory.add",
            {
                "user_id": user["id"],
                "memory_id": entry["id"],
                "scope": entry["scope"],
                "approved": entry["approved"],
                "review_decision": entry["review_decision"],
                "controls": controls.as_dict(),
            },
        )

    return {"user": _public_user(user), "controls": controls.as_dict(), "memory": entry}


@app.post("/retrieve")
def retrieve(request: RetrieveRequest):
    user = get_user(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Unknown user_id: {request.user_id}")

    controls = Controls.from_env()
    docs = retrieve_documents(
        user=user,
        query=request.query,
        documents=load_documents(),
        controls=controls,
        top_k=request.top_k,
    )

    if controls.audit_log:
        record(
            "retrieve",
            {
                "user_id": user["id"],
                "query": request.query,
                "doc_ids": [doc["id"] for doc in docs],
                "controls": controls.as_dict(),
            },
        )

    return {
        "user": _public_user(user),
        "query": request.query,
        "controls": controls.as_dict(),
        "documents": docs,
    }


@app.post("/chat")
def chat(request: ChatRequest):
    user = get_user(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Unknown user_id: {request.user_id}")

    controls = Controls.from_env()
    docs = retrieve_documents(
        user=user,
        query=request.message,
        documents=load_documents(),
        controls=controls,
        top_k=request.top_k,
    )
    answer = generate_answer(
        user=user,
        message=request.message,
        retrieved_documents=docs,
        controls=controls,
    )

    if controls.audit_log:
        record(
            "chat",
            {
                "user_id": user["id"],
                "message": request.message,
                "doc_ids": [doc["id"] for doc in docs],
                "mode": answer["mode"],
                "controls": controls.as_dict(),
            },
        )

    return {
        "user": _public_user(user),
        "message": request.message,
        "controls": controls.as_dict(),
        "retrieved_documents": docs,
        **answer,
    }


@app.post("/tools/update-ticket")
def tool_update_ticket(request: ToolUpdateTicketRequest):
    user = get_user(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Unknown user_id: {request.user_id}")
    ticket = get_ticket(request.ticket_id.upper())
    if not ticket:
        raise HTTPException(status_code=404, detail=f"Unknown ticket_id: {request.ticket_id}")

    controls = Controls.from_env()
    result = update_ticket_tool(
        user=user,
        ticket=ticket,
        status=request.status,
        note=request.note,
        approval_token=request.approval_token,
        controls=controls,
    )

    if controls.audit_log:
        record(
            "tool.update_ticket",
            {
                "user_id": user["id"],
                "ticket_id": ticket["id"],
                "status": request.status,
                "result": result["result"],
                "authorization_decision": result["authorization_decision"],
                "approval_decision": result["approval_decision"],
                "controls": controls.as_dict(),
            },
        )

    return {"user": _public_user(user), "controls": controls.as_dict(), **result}


@app.post("/agent/run")
def agent_run(request: AgentRunRequest):
    """Deterministic agent simulation for confused-deputy testing.

    The agent retrieves context, extracts a ticket id from the user goal, and may call
    update_ticket. The default intentionally vulnerable configuration lets the agent
    update cross-tenant tickets because the tool does not enforce authorization.
    """
    user = get_user(request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"Unknown user_id: {request.user_id}")

    controls = Controls.from_env()
    docs = retrieve_documents(
        user=user,
        query=request.goal,
        documents=load_documents(),
        controls=controls,
        top_k=request.top_k,
    )
    memories = visible_memory_for_user(user=user, controls=controls)
    memory_instruction = find_memory_instruction(memories)

    goal_for_decision = request.goal
    decision_source = "user_goal"
    if memory_instruction:
        goal_for_decision = f"{request.goal}\n{memory_instruction}"
        decision_source = "memory_instruction"

    ticket_match = TICKET_RE.search(goal_for_decision)
    if not ticket_match:
        if controls.audit_log:
            record(
                "agent.run",
                {
                    "user_id": user["id"],
                    "goal": request.goal,
                    "action": "no_tool_call",
                    "memory_ids": [entry["id"] for entry in memories],
                    "decision_source": decision_source,
                },
            )
        return {
            "user": _public_user(user),
            "goal": request.goal,
            "controls": controls.as_dict(),
            "retrieved_documents": docs,
            "visible_memory": memories,
            "agent_decision": "no_tool_call",
            "decision_source": decision_source,
            "reason": "No ticket id was present in the user goal or active memory.",
        }

    ticket_id = ticket_match.group(0).upper()
    ticket = get_ticket(ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail=f"Unknown ticket_id: {ticket_id}")

    status = _status_from_goal(goal_for_decision)
    result = update_ticket_tool(
        user=user,
        ticket=ticket,
        status=status,
        note=f"Agent executed goal: {request.goal} | decision_source={decision_source}",
        approval_token=request.approval_token,
        controls=controls,
    )

    if controls.audit_log:
        record(
            "agent.run",
            {
                "user_id": user["id"],
                "goal": request.goal,
                "ticket_id": ticket_id,
                "action": "tool_call_update_ticket",
                "authorization_decision": result["authorization_decision"],
                "approval_decision": result["approval_decision"],
                "decision_source": decision_source,
                "memory_ids": [entry["id"] for entry in memories],
                "controls": controls.as_dict(),
            },
        )

    return {
        "user": _public_user(user),
        "goal": request.goal,
        "controls": controls.as_dict(),
        "retrieved_documents": docs,
        "visible_memory": memories,
        "agent_decision": "tool_call_update_ticket",
        "decision_source": decision_source,
        **result,
    }
