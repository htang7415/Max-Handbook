from __future__ import annotations


def weighted_retrieval_fusion(
    sparse_scores: dict[str, float],
    dense_scores: dict[str, float],
    alpha: float = 0.5,
) -> list[tuple[str, float]]:
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must satisfy 0 <= alpha <= 1")

    fused: dict[str, float] = {}
    for doc_id in set(sparse_scores) | set(dense_scores):
        fused[doc_id] = alpha * sparse_scores.get(doc_id, 0.0) + (1.0 - alpha) * dense_scores.get(doc_id, 0.0)

    return sorted(fused.items(), key=lambda item: item[1], reverse=True)
