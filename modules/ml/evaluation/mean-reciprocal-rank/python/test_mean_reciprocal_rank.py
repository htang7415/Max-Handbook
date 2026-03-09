import pytest

from mean_reciprocal_rank import mean_reciprocal_rank


def test_mean_reciprocal_rank_averages_first_hit_reciprocals() -> None:
    score = mean_reciprocal_rank([[0, 1, 0], [1, 0, 0], [0, 0, 0]])

    assert score == pytest.approx((0.5 + 1.0 + 0.0) / 3.0)


def test_mean_reciprocal_rank_returns_zero_for_no_queries() -> None:
    assert mean_reciprocal_rank([]) == pytest.approx(0.0)


def test_mean_reciprocal_rank_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="binary"):
        mean_reciprocal_rank([[0, 2]])
