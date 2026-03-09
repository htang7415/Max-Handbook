import pytest

from terminal_share import terminal_share


def test_terminal_share_returns_fraction_of_terminal_transitions() -> None:
    score = terminal_share([False, True, False, True])

    assert score == pytest.approx(0.5)


def test_terminal_share_returns_zero_for_empty_input() -> None:
    assert terminal_share([]) == pytest.approx(0.0)


def test_terminal_share_is_one_when_all_transitions_are_terminal() -> None:
    assert terminal_share([True, True]) == pytest.approx(1.0)
