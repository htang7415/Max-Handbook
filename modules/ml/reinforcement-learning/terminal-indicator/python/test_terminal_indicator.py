import pytest

from terminal_indicator import terminal_indicator


def test_terminal_indicator_returns_one_for_terminal_transition() -> None:
    assert terminal_indicator(True) == pytest.approx(1.0)


def test_terminal_indicator_returns_zero_for_nonterminal_transition() -> None:
    assert terminal_indicator(False) == pytest.approx(0.0)


def test_terminal_indicator_accepts_boolean_values_only_in_usage() -> None:
    assert terminal_indicator(bool(1)) == pytest.approx(1.0)
