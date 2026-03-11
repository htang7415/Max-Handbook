from consistency_and_quorum_mental_model import (
    majority_quorum,
    quorums_overlap,
    read_your_write_possible,
    stale_read_risk,
)
import pytest


def test_majority_quorum_for_odd_and_even_replication_factors() -> None:
    assert majority_quorum(3) == 2
    assert majority_quorum(4) == 3


def test_overlap_rule_predicts_read_your_write_behavior() -> None:
    assert quorums_overlap(2, 2, 3) is True
    assert read_your_write_possible(2, 2, 3) is True


def test_non_overlapping_quorums_leave_stale_read_risk() -> None:
    assert quorums_overlap(1, 1, 3) is False
    assert stale_read_risk(1, 1, 3) is True


def test_quorums_must_fit_inside_replication_factor() -> None:
    with pytest.raises(ValueError, match="read_quorum"):
        quorums_overlap(4, 2, 3)

    with pytest.raises(ValueError, match="write_quorum"):
        quorums_overlap(2, 0, 3)
