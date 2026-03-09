import pytest

from majority_vote_margin import majority_vote_margin


def test_majority_vote_margin_computes_gap_between_top_two_vote_shares() -> None:
    score = majority_vote_margin(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(0.25)


def test_majority_vote_margin_is_one_when_all_votes_match() -> None:
    assert majority_vote_margin(["Answer", "answer", "the answer"]) == pytest.approx(1.0)


def test_majority_vote_margin_returns_zero_for_empty_answers() -> None:
    assert majority_vote_margin([]) == pytest.approx(0.0)
