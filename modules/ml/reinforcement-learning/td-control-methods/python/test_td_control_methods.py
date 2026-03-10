from __future__ import annotations

import pytest

from td_control_methods import (
    bootstrap_target,
    double_q_target,
    expected_sarsa_target,
    q_learning_target,
    sarsa_target,
    soft_target_update,
    soft_update_gap,
    td_error,
    td_update,
)


def test_q_learning_target_uses_max_next_action_value() -> None:
    assert q_learning_target(reward=1.0, gamma=0.9, next_q_values=[2.0, 5.0, 4.0]) == pytest.approx(5.5)


def test_sarsa_target_uses_taken_next_action_value() -> None:
    assert sarsa_target(reward=1.0, gamma=0.9, next_q=4.0) == pytest.approx(4.6)


def test_expected_sarsa_target_uses_policy_weighted_next_value() -> None:
    target = expected_sarsa_target(
        reward=1.0,
        gamma=0.9,
        next_action_probs=[0.25, 0.75],
        next_q_values=[2.0, 4.0],
    )

    assert target == pytest.approx(4.15)


def test_double_q_target_decouples_selection_and_evaluation() -> None:
    target = double_q_target(
        reward=1.0,
        gamma=0.9,
        selector_values=[2.0, 5.0, 4.0],
        evaluator_values=[10.0, 3.0, 8.0],
    )

    assert target == pytest.approx(3.7)


def test_bootstrap_target_drops_next_value_for_terminal_step() -> None:
    assert bootstrap_target(reward=1.5, gamma=0.9, next_value=4.0, done=True) == pytest.approx(1.5)


def test_td_error_and_update_match_general_td_shape() -> None:
    target = q_learning_target(reward=1.0, gamma=0.9, next_q_values=[0.0])
    assert td_error(value=0.0, target=target) == pytest.approx(1.0)
    assert td_update(value=0.0, target=target, alpha=0.5) == pytest.approx(0.5)


def test_soft_target_update_and_gap_capture_target_lag() -> None:
    updated = soft_target_update(target_values=[0.0, 2.0], online_values=[2.0, 4.0], tau=0.25)
    gap = soft_update_gap(target_values=[0.0, 2.0], online_values=[2.0, 4.0], tau=0.25)

    assert updated == pytest.approx([0.5, 2.5])
    assert gap == pytest.approx(1.5)


def test_targets_require_valid_inputs() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        q_learning_target(reward=1.0, gamma=0.9, next_q_values=[])
    with pytest.raises(ValueError, match="sum to 1"):
        expected_sarsa_target(reward=1.0, gamma=0.9, next_action_probs=[0.2, 0.2], next_q_values=[1.0, 2.0])
    with pytest.raises(ValueError, match="same length"):
        double_q_target(reward=1.0, gamma=0.9, selector_values=[1.0], evaluator_values=[1.0, 2.0])
    with pytest.raises(ValueError, match="0 <= alpha <= 1"):
        td_update(value=0.0, target=1.0, alpha=1.5)
