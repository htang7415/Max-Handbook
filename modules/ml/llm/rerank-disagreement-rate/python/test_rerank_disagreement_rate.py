import pytest

from rerank_disagreement_rate import rerank_disagreement_rate


def test_rerank_disagreement_rate_counts_position_changes() -> None:
    rate = rerank_disagreement_rate(
        baseline_ids=["d1", "d2", "d3"],
        reranked_ids=["d1", "d3", "d2"],
    )

    assert rate == pytest.approx(2.0 / 3.0)


def test_rerank_disagreement_rate_can_compare_prefix_only() -> None:
    rate = rerank_disagreement_rate(
        baseline_ids=["d1", "d2", "d3"],
        reranked_ids=["d1", "d3", "d2"],
        k=1,
    )

    assert rate == pytest.approx(0.0)


def test_rerank_disagreement_rate_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        rerank_disagreement_rate(baseline_ids=["d1"], reranked_ids=["d1", "d2"])
