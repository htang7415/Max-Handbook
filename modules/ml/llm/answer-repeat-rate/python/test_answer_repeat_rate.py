import pytest

from answer_repeat_rate import answer_repeat_rate


def test_answer_repeat_rate_returns_complement_of_uniqueness_rate() -> None:
    score = answer_repeat_rate(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(0.25)


def test_answer_repeat_rate_is_zero_when_all_answers_differ() -> None:
    assert answer_repeat_rate(["A", "B", "C"]) == pytest.approx(0.0)


def test_answer_repeat_rate_returns_zero_for_empty_answers() -> None:
    assert answer_repeat_rate([]) == pytest.approx(0.0)
