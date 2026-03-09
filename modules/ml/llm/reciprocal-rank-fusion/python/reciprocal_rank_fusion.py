from __future__ import annotations


def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> list[tuple[str, float]]:
    if k <= 0:
        raise ValueError("k must be positive")

    fused_scores: dict[str, float] = {}
    for ranking in rankings:
        for rank, document_id in enumerate(ranking, start=1):
            fused_scores[document_id] = fused_scores.get(document_id, 0.0) + 1.0 / (k + rank)

    return sorted(fused_scores.items(), key=lambda item: (-item[1], item[0]))
