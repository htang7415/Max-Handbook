"""semantic_caching_basics - reuse responses for similar queries within a guarded scope."""

from __future__ import annotations

import re


def token_overlap_score(left: str, right: str) -> float:
    left_tokens = set(re.findall(r"[a-z0-9]+", left.lower()))
    right_tokens = set(re.findall(r"[a-z0-9]+", right.lower()))
    if not left_tokens:
        return 0.0
    return len(left_tokens & right_tokens) / len(left_tokens)


def store_semantic_entry(
    entries: list[dict[str, object]],
    query: str,
    response: str,
    workspace_id: int,
    version: str,
    now: int,
) -> None:
    entries.append(
        {
            "query": query,
            "response": response,
            "workspace_id": workspace_id,
            "version": version,
            "created_at": now,
        }
    )


def lookup_semantic_cache(
    entries: list[dict[str, object]],
    query: str,
    workspace_id: int,
    version: str,
    now: int,
    similarity_threshold: float = 0.5,
    max_age_seconds: int = 300,
) -> str | None:
    best_match: tuple[float, str] | None = None
    for entry in entries:
        if entry["workspace_id"] != workspace_id or entry["version"] != version:
            continue
        age = now - int(entry["created_at"])
        if age > max_age_seconds:
            continue
        score = token_overlap_score(query, str(entry["query"]))
        if score < similarity_threshold:
            continue
        response = str(entry["response"])
        if best_match is None or score > best_match[0]:
            best_match = (score, response)
    return None if best_match is None else best_match[1]
