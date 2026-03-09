import pytest

from off_policy_correction import weighted_importance_sampling_estimate


def test_weighted_importance_sampling_normalizes_weights() -> None:
    estimate = weighted_importance_sampling_estimate(
        rewards=[1.0, 0.0],
        target_probs=[0.6, 0.2],
        behavior_probs=[0.3, 0.4],
    )

    assert estimate == pytest.approx(0.8)


def test_weighted_importance_sampling_returns_zero_when_all_target_probabilities_are_zero() -> None:
    estimate = weighted_importance_sampling_estimate(
        rewards=[1.0, 2.0],
        target_probs=[0.0, 0.0],
        behavior_probs=[0.5, 0.5],
    )

    assert estimate == pytest.approx(0.0)


def test_weighted_importance_sampling_requires_positive_behavior_probabilities() -> None:
    with pytest.raises(ValueError, match="strictly positive"):
        weighted_importance_sampling_estimate(
            rewards=[1.0],
            target_probs=[0.5],
            behavior_probs=[0.0],
        )
