import pytest

from answer_stability import answer_stability


def test_answer_stability_uses_pairwise_agreement_over_normalized_answers() -> None:
    score = answer_stability(["Paris", "the paris", "London", "Paris"])

    assert score == pytest.approx(0.5)


def test_answer_stability_returns_zero_for_no_answers() -> None:
    assert answer_stability([]) == pytest.approx(0.0)


def test_answer_stability_returns_one_for_single_answer() -> None:
    assert answer_stability(["Only one"]) == pytest.approx(1.0)
