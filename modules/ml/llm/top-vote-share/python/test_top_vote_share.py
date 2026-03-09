import pytest

from top_vote_share import top_vote_share


def test_top_vote_share_returns_top_normalized_vote_fraction() -> None:
    score = top_vote_share(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(0.5)


def test_top_vote_share_is_one_when_all_votes_match() -> None:
    assert top_vote_share(["Answer", "answer", "the answer"]) == pytest.approx(1.0)


def test_top_vote_share_returns_zero_for_empty_answers() -> None:
    assert top_vote_share([]) == pytest.approx(0.0)
