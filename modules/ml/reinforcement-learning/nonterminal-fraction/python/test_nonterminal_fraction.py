import pytest

from nonterminal_fraction import nonterminal_fraction


def test_nonterminal_fraction_returns_fraction_of_false_done_flags() -> None:
    score = nonterminal_fraction([False, True, False, False])

    assert score == pytest.approx(0.75)


def test_nonterminal_fraction_returns_zero_for_empty_input() -> None:
    assert nonterminal_fraction([]) == pytest.approx(0.0)


def test_nonterminal_fraction_is_zero_when_all_transitions_are_terminal() -> None:
    assert nonterminal_fraction([True, True]) == pytest.approx(0.0)
