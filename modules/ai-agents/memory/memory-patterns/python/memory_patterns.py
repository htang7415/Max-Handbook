from __future__ import annotations


def append_memory(memory: list[str], item: str, max_items: int | None = None) -> list[str]:
    cleaned = item.strip()
    updated = [entry for entry in memory if entry.strip()]
    if cleaned:
        updated.append(cleaned)
    if max_items is not None:
        if max_items <= 0:
            raise ValueError("max_items must be positive")
        updated = updated[-max_items:]
    return updated


def summarize_recent_memory(memory: list[str], max_items: int) -> str:
    if max_items <= 0:
        raise ValueError("max_items must be positive")
    recent = [entry.strip() for entry in memory[-max_items:] if entry.strip()]
    return " | ".join(recent)


def _tokens(text: str) -> set[str]:
    return {token for token in text.lower().split() if token}


def retrieve_relevant_memories(query: str, memory: list[str], k: int) -> list[str]:
    if k <= 0:
        raise ValueError("k must be positive")
    query_tokens = _tokens(query)
    scored: list[tuple[int, float, int, str]] = []
    for index, entry in enumerate(memory):
        cleaned = entry.strip()
        if not cleaned:
            continue
        entry_tokens = _tokens(cleaned)
        overlap = len(query_tokens & entry_tokens)
        density = overlap / max(len(entry_tokens), 1)
        scored.append((overlap, density, index, cleaned))
    ranked = sorted(scored, key=lambda item: (-item[0], -item[1], item[2]))
    return [entry for overlap, _density, _index, entry in ranked[:k] if overlap > 0]
