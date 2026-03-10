from __future__ import annotations

import pytest

from return_estimation_methods import (
    discounted_return,
    first_visit_returns,
    n_step_return,
    n_step_td_target,
    td_lambda_returns,
)


def test_discounted_return_matches_definition() -> None:
    assert discounted_return([1.0, 1.0], 0.5) == pytest.approx(1.5)


def test_n_step_return_adds_bootstrap_value() -> None:
    value = n_step_return(rewards=[1.0, 2.0], gamma=0.9, bootstrap_value=10.0)

    assert value == pytest.approx(1.0 + 0.9 * 2.0 + 0.9 * 0.9 * 10.0)


def test_n_step_td_target_matches_n_step_return_shape() -> None:
    target = n_step_td_target(rewards=[1.0, 2.0, 3.0], bootstrap_value=4.0, gamma=0.5)

    assert target == pytest.approx(3.25)


def test_td_lambda_interpolates_between_td_and_monte_carlo() -> None:
    one_step = td_lambda_returns(rewards=[1.0, 2.0], next_state_values=[10.0, 20.0], gamma=0.9, lam=0.0)
    monte_carlo = td_lambda_returns(rewards=[1.0, 2.0], next_state_values=[10.0, 20.0], gamma=0.9, lam=1.0)

    assert one_step == pytest.approx([10.0, 20.0])
    assert monte_carlo == pytest.approx([2.8, 2.0])


def test_first_visit_returns_use_first_occurrence() -> None:
    returns = first_visit_returns(states=["A", "B", "A"], rewards=[1.0, 2.0, 3.0], gamma=1.0)

    assert returns == {"B": 5.0, "A": 6.0}


def test_return_methods_require_valid_inputs() -> None:
    with pytest.raises(ValueError, match="gamma"):
        discounted_return([1.0], gamma=1.5)
    with pytest.raises(ValueError, match="same length"):
        first_visit_returns(["A"], [1.0, 2.0], gamma=0.9)
