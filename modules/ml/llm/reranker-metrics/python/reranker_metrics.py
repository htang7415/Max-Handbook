from __future__ import annotations


def reranker_metrics(relevance: list[int], k: int) -> tuple[float, float]:
    if k <= 0:
        raise ValueError("k must be positive")
    if any(label not in {0, 1} for label in relevance):
        raise ValueError("relevance labels must be binary")
    if not relevance:
        return 0.0, 0.0

    top_k = relevance[:k]
    first_rank = next((index + 1 for index, label in enumerate(top_k) if label == 1), None)
    mrr = 0.0 if first_rank is None else 1.0 / first_rank

    total_relevant = sum(relevance)
    recall = 0.0 if total_relevant == 0 else sum(top_k) / total_relevant
    return mrr, recall
