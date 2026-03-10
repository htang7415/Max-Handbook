from __future__ import annotations

import pytest

from policy_gradient_methods import clip_ratio, generalized_advantages, ppo_objective_term, reinforce_update


def test_reinforce_update_matches_reward_weighted_gradient() -> None:
    assert reinforce_update(grad_logp=2.0, reward=1.0, lr=0.1) == pytest.approx(0.2)


def test_clip_ratio_limits_large_policy_ratio() -> None:
    assert clip_ratio(1.5, 0.2) == pytest.approx(1.2)


def test_ppo_objective_term_uses_clipped_branch_for_large_positive_advantage() -> None:
    assert ppo_objective_term(ratio=1.5, advantage=2.0, eps=0.2) == pytest.approx(2.4)


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


def test_policy_gradient_methods_validate_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        generalized_advantages(rewards=[1.0], values=[0.0, 0.0], gamma=0.9, lam=0.95)
    with pytest.raises(ValueError, match="non-negative"):
        clip_ratio(1.0, -0.1)
