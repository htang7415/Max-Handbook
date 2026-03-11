"""agent_memory_retrieval - scoped memory ranking for agent systems."""

from __future__ import annotations

import re


def token_overlap_score(query: str, text: str) -> float:
    query_tokens = set(re.findall(r"[a-z0-9]+", query.lower()))
    text_tokens = set(re.findall(r"[a-z0-9]+", text.lower()))
    if not query_tokens:
        return 0.0
    return len(query_tokens & text_tokens) / len(query_tokens)


def matches_scope(memory: dict[str, object], workspace_id: int, agent_id: str) -> bool:
    if int(memory["workspace_id"]) != workspace_id:
        return False
    owner = memory.get("agent_id")
    return owner in (None, agent_id)


def memory_retrieval_score(
    query: str,
    memory: dict[str, object],
    now: int,
    recency_window: int = 3600,
) -> float:
    overlap = token_overlap_score(query, str(memory["text"]))
    if overlap == 0.0:
        return 0.0
    age = max(now - int(memory["created_at"]), 0)
    recency = max(0.0, 1.0 - (age / recency_window))
    importance = float(memory.get("importance", 0.5))
    return (0.6 * overlap) + (0.25 * recency) + (0.15 * importance)


def retrieve_agent_memories(
    query: str,
    memories: list[dict[str, object]],
    workspace_id: int,
    agent_id: str,
    now: int,
    top_k: int,
    min_score: float = 0.2,
) -> list[tuple[str, float]]:
    scored: list[tuple[str, float]] = []
    for memory in memories:
        if not matches_scope(memory, workspace_id, agent_id):
            continue
        score = memory_retrieval_score(query, memory, now)
        if score < min_score:
            continue
        scored.append((str(memory["id"]), score))
    return sorted(scored, key=lambda item: (-item[1], item[0]))[:top_k]
