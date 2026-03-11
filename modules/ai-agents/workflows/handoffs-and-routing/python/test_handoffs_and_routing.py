from __future__ import annotations

import pytest

from handoffs_and_routing import build_handoff, route_task, should_retry


def test_handoffs_and_routing_selects_route_and_builds_packet() -> None:
    routes = {
        "writer": ["summarize", "draft"],
        "ticketing": ["ticket", "issue"],
    }
    route = route_task("open a ticket for the broken docs page", routes)
    assert route == "ticketing"
    handoff = build_handoff("task_7", route, {"doc_id": "abc"})
    assert handoff == {
        "task_id": "task_7",
        "target": "ticketing",
        "payload": {"doc_id": "abc"},
    }
    assert should_retry(attempt=1, max_attempts=3, retryable=True) is True
    assert should_retry(attempt=3, max_attempts=3, retryable=True) is False


def test_handoffs_and_routing_validation() -> None:
    assert route_task("no match here", {"writer": ["draft"]}) is None
    with pytest.raises(ValueError):
        build_handoff("", "writer", {})
    with pytest.raises(ValueError):
        build_handoff("task_1", "", {})
    with pytest.raises(ValueError):
        should_retry(attempt=-1, max_attempts=3, retryable=True)
    with pytest.raises(ValueError):
        should_retry(attempt=0, max_attempts=0, retryable=True)
