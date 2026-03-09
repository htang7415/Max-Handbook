import pytest

from ndcg import ndcg_at_k


def test_ndcg_is_one_for_perfect_ranking() -> None:
    assert ndcg_at_k([3.0, 2.0, 1.0], k=3) == pytest.approx(1.0)


def test_ndcg_discounts_late_relevant_items() -> None:
    score = ndcg_at_k([0.0, 3.0, 2.0], k=3)

    assert score == pytest.approx(0.6653, abs=1e-4)


def test_ndcg_is_zero_when_all_relevance_is_zero() -> None:
    assert ndcg_at_k([0.0, 0.0], k=2) == pytest.approx(0.0)
