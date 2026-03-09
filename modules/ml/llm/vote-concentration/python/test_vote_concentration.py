import pytest

from vote_concentration import vote_concentration


def test_vote_concentration_returns_top_normalized_vote_share() -> None:
    score = vote_concentration(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(0.5)


def test_vote_concentration_is_one_when_all_votes_match() -> None:
    assert vote_concentration(["Answer", "answer", "the answer"]) == pytest.approx(1.0)


def test_vote_concentration_returns_zero_for_empty_answers() -> None:
    assert vote_concentration([]) == pytest.approx(0.0)
