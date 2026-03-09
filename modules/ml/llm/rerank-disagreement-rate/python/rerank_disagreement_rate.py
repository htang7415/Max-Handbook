from __future__ import annotations


def rerank_disagreement_rate(baseline_ids: list[str], reranked_ids: list[str], k: int | None = None) -> float:
    if len(baseline_ids) != len(reranked_ids):
        raise ValueError("baseline_ids and reranked_ids must have the same length")
    if k is None:
        k = len(baseline_ids)
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(baseline_ids):
        raise ValueError("k cannot exceed ranking length")

    disagreements = sum(
        baseline_id != reranked_id
        for baseline_id, reranked_id in zip(baseline_ids[:k], reranked_ids[:k])
    )
    return disagreements / k
