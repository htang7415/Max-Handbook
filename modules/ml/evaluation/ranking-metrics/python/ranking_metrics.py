from __future__ import annotations

import math


def dcg_at_k(relevance: list[float], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if any(gain < 0.0 for gain in relevance):
        raise ValueError("relevance gains must be non-negative")
    total = 0.0
    for rank, gain in enumerate(relevance[:k], start=1):
        total += (2.0**gain - 1.0) / math.log2(rank + 1.0)
    return total


def mean_reciprocal_rank(relevance_lists: list[list[int]]) -> float:
    if not relevance_lists:
        return 0.0
    if any(label not in {0, 1} for relevance in relevance_lists for label in relevance):
        raise ValueError("relevance labels must be binary")

    reciprocal_ranks = 0.0
    for relevance in relevance_lists:
        first_rank = next((index + 1 for index, label in enumerate(relevance) if label == 1), None)
        reciprocal_ranks += 0.0 if first_rank is None else 1.0 / first_rank
    return reciprocal_ranks / len(relevance_lists)


def ndcg_at_k(relevance: list[float], k: int) -> float:
    actual = dcg_at_k(relevance, k)
    ideal = dcg_at_k(sorted(relevance, reverse=True), k)
    if ideal == 0.0:
        return 0.0
    return actual / ideal


def coverage_error(relevance_rankings: list[list[int]]) -> float:
    if not relevance_rankings:
        return 0.0
    if any(label not in {0, 1} for ranking in relevance_rankings for label in ranking):
        raise ValueError("relevance labels must be binary")

    total = 0.0
    for ranking in relevance_rankings:
        last_relevant_rank = max((index + 1 for index, label in enumerate(ranking) if label == 1), default=0)
        total += last_relevant_rank
    return total / len(relevance_rankings)


def lift_at_k(labels: list[int], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not labels:
        return 0.0
    if k > len(labels):
        raise ValueError("k must not exceed the number of labels")
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")

    base_rate = sum(labels) / len(labels)
    if base_rate == 0.0:
        return 0.0

    precision_at_k = sum(labels[:k]) / k
    return precision_at_k / base_rate
