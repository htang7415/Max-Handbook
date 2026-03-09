import pytest

from agreement_rate import agreement_rate


def test_agreement_rate_returns_modal_fraction() -> None:
    score = agreement_rate(["accept", "accept", "reject", "accept"])

    assert score == pytest.approx(0.75)


def test_agreement_rate_supports_numeric_judge_outcomes() -> None:
    score = agreement_rate([1, 0, 1, -1, 1])

    assert score == pytest.approx(3 / 5)


def test_agreement_rate_returns_zero_for_empty_input() -> None:
    assert agreement_rate([]) == pytest.approx(0.0)
