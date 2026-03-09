from __future__ import annotations


def _reciprocal_rank(relevance: list[int]) -> float:
    if any(label not in {0, 1} for label in relevance):
        raise ValueError("relevance labels must be binary")

    first_rank = next((index + 1 for index, label in enumerate(relevance) if label == 1), None)
    return 0.0 if first_rank is None else 1.0 / first_rank


def rerank_gain(baseline_relevance: list[int], reranked_relevance: list[int]) -> float:
    return _reciprocal_rank(reranked_relevance) - _reciprocal_rank(baseline_relevance)
