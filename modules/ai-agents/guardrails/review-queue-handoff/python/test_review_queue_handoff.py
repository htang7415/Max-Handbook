from __future__ import annotations

import pytest

from review_queue_handoff import review_packet, review_priority, send_to_review_queue


def test_review_queue_handoff_builds_review_packet() -> None:
    priority = review_priority("policy_review", confidence=0.42)
    assert priority == "medium"
    packet = review_packet("task_17", "policy_review", "human_review", priority)
    assert packet == {
        "task_id": "task_17",
        "reason": "policy_review",
        "route": "human_review",
        "priority": "medium",
    }
    assert send_to_review_queue(packet) is True


def test_review_queue_handoff_validation() -> None:
    assert review_priority("policy_block", confidence=0.9) == "high"
    with pytest.raises(ValueError):
        review_priority("", confidence=0.5)
    with pytest.raises(ValueError):
        review_priority("policy_review", confidence=1.1)
    with pytest.raises(ValueError):
        review_packet("task_1", "policy_review", "human_review", "urgent")
