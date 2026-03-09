import pytest

from reranker_metrics import reranker_metrics


def test_reranker_metrics_return_mrr_and_recall_at_k() -> None:
    mrr, recall = reranker_metrics([0, 1, 0, 1], k=3)

    assert mrr == pytest.approx(0.5)
    assert recall == pytest.approx(0.5)


def test_reranker_metrics_return_zero_when_no_relevant_item_is_found() -> None:
    mrr, recall = reranker_metrics([0, 0, 1], k=2)

    assert mrr == 0.0
    assert recall == 0.0


def test_reranker_metrics_require_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        reranker_metrics([1], k=0)
