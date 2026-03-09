import pytest

from runner_up_vote_share import runner_up_vote_share


def test_runner_up_vote_share_returns_second_highest_normalized_share() -> None:
    score = runner_up_vote_share(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(0.25)


def test_runner_up_vote_share_is_zero_when_all_votes_match() -> None:
    assert runner_up_vote_share(["Answer", "answer", "the answer"]) == pytest.approx(0.0)


def test_runner_up_vote_share_returns_zero_for_empty_answers() -> None:
    assert runner_up_vote_share([]) == pytest.approx(0.0)
