import pytest

from rerank_gain import rerank_gain


def test_rerank_gain_is_positive_when_reranker_moves_relevant_item_earlier() -> None:
    gain = rerank_gain(baseline_relevance=[0, 0, 1], reranked_relevance=[0, 1, 0])

    assert gain == pytest.approx(1.0 / 2.0 - 1.0 / 3.0)


def test_rerank_gain_is_zero_when_rankings_have_same_first_hit() -> None:
    gain = rerank_gain(baseline_relevance=[1, 0], reranked_relevance=[1, 0])

    assert gain == pytest.approx(0.0)


def test_rerank_gain_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="binary"):
        rerank_gain(baseline_relevance=[2], reranked_relevance=[1])
