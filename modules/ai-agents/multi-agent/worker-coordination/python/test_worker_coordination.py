from __future__ import annotations

import pytest

from worker_coordination import merge_worker_outputs, select_worker, worker_handoff


def test_worker_coordination_routes_hands_off_and_merges() -> None:
    worker_keywords = {
        "researcher": ["investigate", "research"],
        "writer": ["write", "summarize"],
    }
    worker = select_worker("investigate billing issue", worker_keywords)
    assert worker == "researcher"
    handoff = worker_handoff(worker, "investigate invoice mismatch", {"invoice_id": "inv_7"})
    assert handoff == {
        "worker": "researcher",
        "task": "investigate invoice mismatch",
        "context": {"invoice_id": "inv_7"},
    }
    merged = merge_worker_outputs(
        [
            {"worker": "researcher", "result": "Found invoice mismatch"},
            {"worker": "writer", "result": "Drafted summary"},
        ]
    )
    assert merged == {
        "workers": ["researcher", "writer"],
        "results": ["Found invoice mismatch", "Drafted summary"],
        "count": 2,
    }


def test_worker_coordination_validation() -> None:
    assert select_worker("", {"writer": ["write"]}) is None
    with pytest.raises(ValueError):
        worker_handoff("", "task", {})
    with pytest.raises(ValueError):
        worker_handoff("writer", "", {})
