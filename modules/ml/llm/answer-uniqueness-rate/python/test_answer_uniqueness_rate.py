import pytest

from answer_uniqueness_rate import answer_uniqueness_rate


def test_answer_uniqueness_rate_returns_fraction_of_unique_normalized_answers() -> None:
    score = answer_uniqueness_rate(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(3 / 4)


def test_answer_uniqueness_rate_is_one_when_all_answers_differ() -> None:
    assert answer_uniqueness_rate(["A", "B", "C"]) == pytest.approx(1.0)


def test_answer_uniqueness_rate_returns_zero_for_empty_answers() -> None:
    assert answer_uniqueness_rate([]) == pytest.approx(0.0)
