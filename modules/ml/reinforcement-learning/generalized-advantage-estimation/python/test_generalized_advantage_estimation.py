import pytest

from generalized_advantage_estimation import generalized_advantages


def test_generalized_advantages_reduce_to_td_residuals_when_lambda_is_zero() -> None:
    advantages = generalized_advantages(
        rewards=[1.0, 2.0],
        values=[0.5, 1.0],
        gamma=0.9,
        lam=0.0,
        next_value=0.2,
    )

    assert advantages == pytest.approx([1.4, 1.18])


def test_generalized_advantages_accumulate_future_residuals_when_lambda_is_positive() -> None:
    advantages = generalized_advantages(
        rewards=[1.0, 2.0],
        values=[0.5, 1.0],
        gamma=0.9,
        lam=0.5,
        next_value=0.2,
    )

    assert advantages == pytest.approx([1.931, 1.18])


def test_generalized_advantages_require_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        generalized_advantages(rewards=[1.0], values=[0.0, 0.0], gamma=0.9, lam=0.95)
