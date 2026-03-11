from __future__ import annotations


def _tokens(text: str) -> set[str]:
    return {token for token in text.lower().split() if token}


def score_memory_for_query(query: str, memories: list[dict[str, object]]) -> list[tuple[str, int]]:
    query_tokens = _tokens(query)
    scored: list[tuple[str, int, int]] = []
    for item in memories:
        text = str(item.get("text", "")).strip()
        if not text:
            continue
        tokens = item.get("tokens")
        if isinstance(tokens, set):
            memory_tokens = tokens
        else:
            memory_tokens = _tokens(text)
        priority = int(item.get("priority", 0))
        overlap = len(query_tokens & memory_tokens)
        score = overlap + priority
        scored.append((text, score, overlap))
    ranked = sorted(scored, key=lambda item: (-item[1], -item[2], item[0]))
    return [(text, score) for text, score, _overlap in ranked]


def top_scored_memories(scored_items: list[tuple[str, int]], k: int) -> list[str]:
    if k <= 0:
        raise ValueError("k must be positive")
    return [text for text, _score in scored_items[:k]]


def best_memory_match(query: str, memories: list[dict[str, object]]) -> str | None:
    scored = score_memory_for_query(query, memories)
    if not scored:
        return None
    return scored[0][0]
