from __future__ import annotations

import pytest

from debate_and_arbitration import (
    agreement_rate,
    arbitrate_majority,
    normalize_candidate,
    vote_counts,
)


def test_debate_and_arbitration_counts_votes_and_selects_winner() -> None:
    candidates = ["Ship now", "ship   now", "Delay"]
    assert normalize_candidate("  Ship   now ") == "ship now"
    assert vote_counts(candidates) == {"ship now": 2, "delay": 1}
    assert agreement_rate(candidates) == pytest.approx(2 / 3)
    assert arbitrate_majority(candidates) == "ship now"


def test_debate_and_arbitration_handles_empty_inputs() -> None:
    assert vote_counts(["", "   "]) == {}
    assert arbitrate_majority(["", "   "]) is None
    with pytest.raises(ValueError):
        agreement_rate(["", "   "])
