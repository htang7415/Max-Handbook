from __future__ import annotations

import pytest

from workflow_concurrency_basics import join_ready, join_state, runnable_branches


def test_workflow_concurrency_basics_tracks_parallel_branches() -> None:
    states = {"fetch_docs": "ready", "fetch_metrics": "done", "draft": "done"}
    assert runnable_branches(states) == ["fetch_docs"]
    assert join_ready(states, required=2) is True
    assert join_state(states, required=2) == "join-ready"


def test_workflow_concurrency_basics_validation_and_blocked_state() -> None:
    with pytest.raises(ValueError):
        join_ready({}, required=0)
    blocked_states = {"a": "failed", "b": "waiting"}
    assert join_state(blocked_states, required=1) == "blocked"
