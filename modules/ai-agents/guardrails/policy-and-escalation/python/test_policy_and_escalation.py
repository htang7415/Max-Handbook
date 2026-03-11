from __future__ import annotations

import pytest

from policy_and_escalation import action_message, escalation_reason, policy_decision


def test_policy_and_escalation_decides_and_explains() -> None:
    blocked_terms = ["private key", "password"]
    review_terms = ["medical advice", "legal advice"]
    assert policy_decision("share the private key", blocked_terms, review_terms) == "block"
    assert policy_decision("give medical advice", blocked_terms, review_terms) == "review"
    assert policy_decision("summarize this note", blocked_terms, review_terms) == "allow"
    assert escalation_reason("block", model_confidence=0.9, threshold=0.7) == "policy_block"
    assert escalation_reason("review", model_confidence=0.9, threshold=0.7) == "policy_review"
    assert escalation_reason("allow", model_confidence=0.4, threshold=0.7) == "low_confidence"
    assert action_message("review") == "Escalate for review."


def test_policy_and_escalation_validation() -> None:
    with pytest.raises(ValueError):
        escalation_reason("allow", model_confidence=-0.1, threshold=0.7)
    with pytest.raises(ValueError):
        escalation_reason("allow", model_confidence=0.5, threshold=1.1)
    with pytest.raises(ValueError):
        action_message("unknown")
