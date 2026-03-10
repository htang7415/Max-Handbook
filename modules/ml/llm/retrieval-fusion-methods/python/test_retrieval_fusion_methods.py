from __future__ import annotations

import pytest

from retrieval_fusion_methods import reciprocal_rank_fusion, weighted_retrieval_fusion


def test_weighted_retrieval_fusion_combines_sparse_and_dense_scores() -> None:
    ranking = weighted_retrieval_fusion(
        sparse_scores={"a": 0.8, "b": 0.5},
        dense_scores={"a": 0.2, "c": 0.9},
        alpha=0.6,
    )

    assert [doc_id for doc_id, _ in ranking] == ["a", "c", "b"]
    assert [score for _, score in ranking] == pytest.approx([0.56, 0.36, 0.3])


def test_weighted_retrieval_fusion_requires_valid_alpha() -> None:
    with pytest.raises(ValueError, match="0 <= alpha <= 1"):
        weighted_retrieval_fusion({}, {}, alpha=1.5)


def test_reciprocal_rank_fusion_rewards_documents_seen_in_multiple_rankings() -> None:
    fused = reciprocal_rank_fusion(rankings=[["d1", "d2", "d3"], ["d2", "d4", "d1"]], k=60)

    assert [document_id for document_id, _ in fused[:2]] == ["d2", "d1"]
    assert [score for _, score in fused[:2]] == pytest.approx([1.0 / 62.0 + 1.0 / 61.0, 1.0 / 61.0 + 1.0 / 63.0])


def test_reciprocal_rank_fusion_requires_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        reciprocal_rank_fusion(rankings=[["d1"]], k=0)
