from __future__ import annotations


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
