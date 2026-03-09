import math

import pytest

from vote_entropy import vote_entropy


def test_vote_entropy_reflects_spread_of_normalized_votes() -> None:
    score = vote_entropy(["Paris", "the paris", "London", "Rome"])

    expected = -(0.5 * math.log(0.5) + 0.25 * math.log(0.25) + 0.25 * math.log(0.25))
    assert score == pytest.approx(expected)


def test_vote_entropy_is_zero_when_all_votes_match() -> None:
    assert vote_entropy(["Answer", "answer", "the answer"]) == pytest.approx(0.0)


def test_vote_entropy_returns_zero_for_empty_answers() -> None:
    assert vote_entropy([]) == pytest.approx(0.0)
