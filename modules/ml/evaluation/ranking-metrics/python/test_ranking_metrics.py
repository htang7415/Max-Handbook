import pytest

from ranking_metrics import coverage_error, dcg_at_k, lift_at_k, mean_reciprocal_rank, ndcg_at_k


def test_mean_reciprocal_rank_averages_first_hit_position() -> None:
    assert mean_reciprocal_rank([[0, 1, 0], [1, 0, 0]]) == pytest.approx((0.5 + 1.0) / 2.0)


def test_ndcg_is_one_for_ideal_ordering() -> None:
    assert ndcg_at_k([3.0, 2.0, 1.0], k=3) == pytest.approx(1.0)


def test_dcg_at_k_matches_discounted_gain_formula() -> None:
    value = dcg_at_k([3.0, 2.0, 1.0], k=2)
    assert value == pytest.approx((2.0**3 - 1.0) / 1.0 + (2.0**2 - 1.0) / 1.5849625007)


def test_coverage_error_averages_last_relevant_rank() -> None:
    assert coverage_error([[0, 1, 0], [1, 0, 1]]) == pytest.approx((2.0 + 3.0) / 2.0)


def test_lift_at_k_compares_prefix_density_to_base_rate() -> None:
    assert lift_at_k([1, 1, 0, 0], k=2) == pytest.approx(2.0)


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="binary"):
        mean_reciprocal_rank([[2]])

    with pytest.raises(ValueError, match="positive"):
        ndcg_at_k([1.0], k=0)
