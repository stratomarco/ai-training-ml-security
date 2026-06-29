from pydantic import BaseModel, Field


class RetrieveRequest(BaseModel):
    user_id: str = Field(..., examples=["alice"])
    query: str = Field(..., min_length=1, examples=["vendor onboarding incident token runbook"])
    top_k: int = Field(3, ge=1, le=10)


class ChatRequest(BaseModel):
    user_id: str = Field(..., examples=["alice"])
    message: str = Field(..., min_length=1, examples=["vendor onboarding incident token runbook"])
    top_k: int = Field(4, ge=1, le=10)


class ToolUpdateTicketRequest(BaseModel):
    user_id: str = Field(..., examples=["alice"])
    ticket_id: str = Field(..., examples=["TCK-2001"])
    status: str = Field(..., min_length=2, examples=["closed"])
    note: str = Field("", examples=["Updated by the BrokenPilot training agent."])
    approval_token: str | None = Field(None, examples=["APPROVED-FOR-LAB"])


class AgentRunRequest(BaseModel):
    user_id: str = Field(..., examples=["alice"])
    goal: str = Field(..., min_length=1, examples=["Resolve the vendor onboarding issue and close TCK-2001"])
    top_k: int = Field(4, ge=1, le=10)
    approval_token: str | None = Field(None, examples=["APPROVED-FOR-LAB"])
