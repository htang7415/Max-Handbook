from __future__ import annotations

import math


def _dcg_at_k(relevance: list[float], k: int) -> float:
    total = 0.0
    for rank, gain in enumerate(relevance[:k], start=1):
        total += (2.0**gain - 1.0) / math.log2(rank + 1.0)
    return total


def ndcg_at_k(relevance: list[float], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if any(gain < 0.0 for gain in relevance):
        raise ValueError("relevance gains must be non-negative")

    actual = _dcg_at_k(relevance, k)
    ideal = _dcg_at_k(sorted(relevance, reverse=True), k)
    if ideal == 0.0:
        return 0.0
    return actual / ideal
