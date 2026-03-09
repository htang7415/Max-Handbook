import pytest

from off_policy_evaluation import off_policy_estimates


def test_off_policy_estimates_return_ordinary_and_weighted_versions() -> None:
    ordinary, weighted = off_policy_estimates(
        rewards=[1.0, 0.0],
        target_probs=[0.6, 0.2],
        behavior_probs=[0.3, 0.4],
    )

    assert ordinary == pytest.approx(1.0)
    assert weighted == pytest.approx(0.8)


def test_off_policy_estimates_return_zero_pair_for_no_data() -> None:
    assert off_policy_estimates([], [], []) == (0.0, 0.0)


def test_off_policy_estimates_require_positive_behavior_probabilities() -> None:
    with pytest.raises(ValueError, match="strictly positive"):
        off_policy_estimates(rewards=[1.0], target_probs=[0.5], behavior_probs=[0.0])
