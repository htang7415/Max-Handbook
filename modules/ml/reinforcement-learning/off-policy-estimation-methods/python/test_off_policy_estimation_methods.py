from __future__ import annotations

import pytest

from off_policy_estimation_methods import (
    importance_sampling_estimate,
    importance_weights,
    off_policy_estimates,
    weighted_importance_sampling_estimate,
)


def test_importance_sampling_estimate_matches_weighted_average() -> None:
    estimate = importance_sampling_estimate(
        rewards=[1.0, 0.0, 2.0],
        target_probs=[0.5, 0.25, 0.5],
        behavior_probs=[0.25, 0.5, 0.25],
    )

    assert estimate == pytest.approx(2.0)


def test_weighted_importance_sampling_normalizes_weights() -> None:
    estimate = weighted_importance_sampling_estimate(
        rewards=[1.0, 0.0],
        target_probs=[0.6, 0.2],
        behavior_probs=[0.3, 0.4],
    )

    assert estimate == pytest.approx(0.8)


def test_importance_weights_match_target_over_behavior_ratio() -> None:
    weights = importance_weights([0.6, 0.2], [0.3, 0.4])
    assert weights == pytest.approx([2.0, 0.5])


def test_off_policy_estimates_return_both_versions() -> None:
    ordinary, weighted = off_policy_estimates(
        rewards=[1.0, 0.0],
        target_probs=[0.6, 0.2],
        behavior_probs=[0.3, 0.4],
    )

    assert ordinary == pytest.approx(1.0)
    assert weighted == pytest.approx(0.8)


def test_estimators_return_zero_for_empty_inputs() -> None:
    assert importance_sampling_estimate([], [], []) == 0.0
    assert weighted_importance_sampling_estimate([], [], []) == 0.0
    assert off_policy_estimates([], [], []) == (0.0, 0.0)


def test_estimators_validate_behavior_probabilities() -> None:
    with pytest.raises(ValueError, match="strictly positive"):
        off_policy_estimates(rewards=[1.0], target_probs=[0.5], behavior_probs=[0.0])
