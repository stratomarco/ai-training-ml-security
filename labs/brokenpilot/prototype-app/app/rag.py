import re
from typing import Any
from .controls import Controls

TOKEN_RE = re.compile(r"[a-zA-Z0-9_\-]+")


def tokenize(text: str) -> set[str]:
    return {t.lower() for t in TOKEN_RE.findall(text)}


def is_authorized_for_document(user: dict[str, Any], document: dict[str, Any]) -> bool:
    if document.get("visibility") == "public":
        return True

    tenant_ok = document.get("tenant") in {"global", user.get("tenant")}
    role_ok = user.get("role") in set(document.get("allowed_roles", []))
    user_ok = user.get("id") in set(document.get("allowed_users", []))

    return tenant_ok and (role_ok or user_ok)


def score_document(query: str, document: dict[str, Any]) -> int:
    query_tokens = tokenize(query)
    doc_text = " ".join(
        [
            document.get("id", ""),
            document.get("title", ""),
            document.get("body", ""),
            " ".join(document.get("tags", [])),
        ]
    )
    doc_tokens = tokenize(doc_text)
    score = len(query_tokens.intersection(doc_tokens))

    # Small boost for title matches to make demos stable.
    title_tokens = tokenize(document.get("title", ""))
    score += 2 * len(query_tokens.intersection(title_tokens))

    return score


def retrieve_documents(
    *,
    user: dict[str, Any],
    query: str,
    documents: list[dict[str, Any]],
    controls: Controls,
    top_k: int = 3,
) -> list[dict[str, Any]]:
    candidates = documents

    if controls.retrieval_authz:
        candidates = [doc for doc in documents if is_authorized_for_document(user, doc)]

    scored: list[tuple[int, dict[str, Any]]] = []
    for doc in candidates:
        score = score_document(query, doc)
        if score > 0:
            scored.append((score, doc))

    scored.sort(key=lambda item: (item[0], item[1].get("id", "")), reverse=True)

    results = []
    for score, doc in scored[: max(1, min(top_k, 10))]:
        # Do not return full internal object references. This is a training app,
        # but keeping API output explicit makes the lab easier to reason about.
        copy = dict(doc)
        copy["score"] = score
        results.append(copy)

    return results
