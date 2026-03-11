from __future__ import annotations


def score_memory_items(items: list[str], keyword_weights: dict[str, int]) -> list[tuple[str, int]]:
    scored: list[tuple[str, int]] = []
    for item in items:
        cleaned = item.strip()
        if not cleaned:
            continue
        lowered = cleaned.lower()
        score = sum(weight for keyword, weight in keyword_weights.items() if keyword.strip().lower() in lowered)
        scored.append((cleaned, score))
    return scored


def retain_top_memory_items(scored_items: list[tuple[str, int]], max_items: int) -> list[str]:
    if max_items <= 0:
        raise ValueError("max_items must be positive")
    ranked = sorted(scored_items, key=lambda item: (-item[1], item[0]))
    return [text for text, _score in ranked[:max_items]]


def evicted_memory_items(scored_items: list[tuple[str, int]], max_items: int) -> list[str]:
    if max_items <= 0:
        raise ValueError("max_items must be positive")
    ranked = sorted(scored_items, key=lambda item: (-item[1], item[0]))
    return [text for text, _score in ranked[max_items:]]
