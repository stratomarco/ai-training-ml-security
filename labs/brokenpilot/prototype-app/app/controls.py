import os
from dataclasses import dataclass


def _env_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Controls:
    retrieval_authz: bool
    prompt_injection_filter: bool
    tool_authz: bool
    tool_approval: bool
    memory_review: bool
    memory_isolation: bool
    audit_log: bool
    output_encoding: bool

    @classmethod
    def from_env(cls) -> "Controls":
        return cls(
            retrieval_authz=_env_bool("ENABLE_RETRIEVAL_AUTHZ", False),
            prompt_injection_filter=_env_bool("ENABLE_PROMPT_INJECTION_FILTER", False),
            tool_authz=_env_bool("ENABLE_TOOL_AUTHZ", False),
            tool_approval=_env_bool("ENABLE_TOOL_APPROVAL", False),
            memory_review=_env_bool("ENABLE_MEMORY_REVIEW", False),
            memory_isolation=_env_bool("ENABLE_MEMORY_ISOLATION", False),
            audit_log=_env_bool("ENABLE_AUDIT_LOG", True),
            output_encoding=_env_bool("ENABLE_OUTPUT_ENCODING", False),
        )

    def as_dict(self) -> dict:
        return {
            "ENABLE_RETRIEVAL_AUTHZ": self.retrieval_authz,
            "ENABLE_PROMPT_INJECTION_FILTER": self.prompt_injection_filter,
            "ENABLE_TOOL_AUTHZ": self.tool_authz,
            "ENABLE_TOOL_APPROVAL": self.tool_approval,
            "ENABLE_MEMORY_REVIEW": self.memory_review,
            "ENABLE_MEMORY_ISOLATION": self.memory_isolation,
            "ENABLE_AUDIT_LOG": self.audit_log,
            "ENABLE_OUTPUT_ENCODING": self.output_encoding,
        }
