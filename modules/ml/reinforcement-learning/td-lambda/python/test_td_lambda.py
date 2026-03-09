import pytest

from td_lambda import td_lambda_returns


def test_td_lambda_reduces_to_one_step_td_when_lambda_is_zero() -> None:
    returns = td_lambda_returns(rewards=[1.0, 2.0], next_state_values=[10.0, 20.0], gamma=0.9, lam=0.0)

    assert returns == pytest.approx([10.0, 20.0])


def test_td_lambda_reduces_to_monte_carlo_when_lambda_is_one() -> None:
    returns = td_lambda_returns(rewards=[1.0, 2.0], next_state_values=[10.0, 20.0], gamma=0.9, lam=1.0)

    assert returns == pytest.approx([2.8, 2.0])


def test_td_lambda_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        td_lambda_returns(rewards=[1.0], next_state_values=[2.0, 3.0], gamma=0.9, lam=0.5)
