from __future__ import annotations

import pytest

from escalation_routing import escalation_packet, escalation_reason, escalation_target


def test_escalation_routing_routes_risky_or_failed_steps() -> None:
    reason = escalation_reason(
        blocked=False,
        confidence=0.4,
        threshold=0.7,
        attempt=1,
        max_attempts=2,
    )
    assert reason == "low_confidence"
    route = escalation_target(reason, {"low_confidence": "human_review"})
    assert route == "human_review"
    assert escalation_packet("task_9", reason, route) == {
        "task_id": "task_9",
        "reason": "low_confidence",
        "route": "human_review",
    }


def test_escalation_routing_validation_and_retry_exhaustion() -> None:
    assert escalation_reason(
        blocked=False,
        confidence=0.9,
        threshold=0.7,
        attempt=2,
        max_attempts=2,
    ) == "retry_exhausted"
    assert escalation_reason(
        blocked=True,
        confidence=0.9,
        threshold=0.7,
        attempt=0,
        max_attempts=2,
    ) == "policy_review"
    with pytest.raises(ValueError):
        escalation_reason(False, -0.1, 0.7, 0, 2)
    with pytest.raises(ValueError):
        escalation_packet("", "low_confidence", "human_review")
