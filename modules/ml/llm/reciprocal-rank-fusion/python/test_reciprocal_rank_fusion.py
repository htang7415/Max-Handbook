import pytest

from reciprocal_rank_fusion import reciprocal_rank_fusion


def test_reciprocal_rank_fusion_rewards_documents_seen_in_multiple_rankings() -> None:
    fused = reciprocal_rank_fusion(rankings=[["d1", "d2", "d3"], ["d2", "d4", "d1"]], k=60)

    assert [document_id for document_id, _ in fused[:2]] == ["d2", "d1"]
    assert [score for _, score in fused[:2]] == pytest.approx([1.0 / 62.0 + 1.0 / 61.0, 1.0 / 61.0 + 1.0 / 63.0])


def test_reciprocal_rank_fusion_returns_empty_list_for_no_rankings() -> None:
    assert reciprocal_rank_fusion(rankings=[]) == []


def test_reciprocal_rank_fusion_requires_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        reciprocal_rank_fusion(rankings=[["d1"]], k=0)
