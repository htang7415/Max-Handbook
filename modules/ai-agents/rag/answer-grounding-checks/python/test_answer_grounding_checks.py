from __future__ import annotations

import pytest

from answer_grounding_checks import (
    claim_support_map,
    grounded_claim_rate,
    unsupported_claims,
)


def test_answer_grounding_checks_find_supported_and_unsupported_claims() -> None:
    claims = ["csv required", "weekly report due friday", "need manager approval"]
    evidence = ["csv required for exports", "weekly report due friday"]
    support = claim_support_map(claims, evidence)
    assert support == {
        "csv required": True,
        "weekly report due friday": True,
        "need manager approval": False,
    }
    assert grounded_claim_rate(support) == pytest.approx(2 / 3)
    assert unsupported_claims(support) == ["need manager approval"]


def test_answer_grounding_checks_validation() -> None:
    assert claim_support_map(["", "   "], ["evidence"]) == {}
    with pytest.raises(ValueError):
        grounded_claim_rate({})
