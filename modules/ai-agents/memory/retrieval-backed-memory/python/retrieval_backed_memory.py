from __future__ import annotations


def _tokens(text: str) -> set[str]:
    return {token for token in text.lower().split() if token}


def index_memories(items: list[str]) -> list[dict[str, object]]:
    indexed: list[dict[str, object]] = []
    for item in items:
        cleaned = item.strip()
        if not cleaned:
            continue
        indexed.append({"text": cleaned, "tokens": _tokens(cleaned)})
    return indexed


def retrieve_memory_hits(query: str, memory_index: list[dict[str, object]], k: int) -> list[str]:
    if k <= 0:
        raise ValueError("k must be positive")
    query_tokens = _tokens(query)
    scored: list[tuple[int, int, str]] = []
    for index, item in enumerate(memory_index):
        text = str(item.get("text", "")).strip()
        tokens = item.get("tokens", set())
        if not text or not isinstance(tokens, set):
            continue
        overlap = len(query_tokens & tokens)
        if overlap > 0:
            scored.append((overlap, -index, text))
    ranked = sorted(scored, reverse=True)
    return [text for _overlap, _index, text in ranked[:k]]


def memory_context(items: list[str], max_items: int) -> str:
    if max_items <= 0:
        raise ValueError("max_items must be positive")
    cleaned = [item.strip() for item in items[:max_items] if item.strip()]
    return "\n".join(f"- {item}" for item in cleaned)
