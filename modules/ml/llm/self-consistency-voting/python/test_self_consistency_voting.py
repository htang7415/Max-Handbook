import pytest

from self_consistency_voting import self_consistency_vote


def test_self_consistency_vote_aggregates_normalized_answers() -> None:
    answer, share = self_consistency_vote(["The Eiffel Tower!", "eiffel tower", "Paris"])

    assert answer == "eiffel tower"
    assert share == pytest.approx(2.0 / 3.0)


def test_self_consistency_vote_breaks_ties_by_first_seen_answer() -> None:
    answer, share = self_consistency_vote(["Yes", "No"])

    assert answer == "yes"
    assert share == pytest.approx(0.5)


def test_self_consistency_vote_handles_empty_input() -> None:
    assert self_consistency_vote([]) == ("", 0.0)
