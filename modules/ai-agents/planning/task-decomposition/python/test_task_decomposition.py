from __future__ import annotations

import pytest

from task_decomposition import (
    decomposition_is_actionable,
    decompose_goal,
    numbered_checkpoints,
)


def test_task_decomposition_builds_actionable_checkpoints() -> None:
    parts = decompose_goal("launch report", ["collect", "write", "send"])
    assert parts == ["collect launch report", "write launch report", "send launch report"]
    checkpoints = numbered_checkpoints(parts)
    assert checkpoints == [
        {"id": 1, "text": "collect launch report", "done": False},
        {"id": 2, "text": "write launch report", "done": False},
        {"id": 3, "text": "send launch report", "done": False},
    ]
    assert decomposition_is_actionable(checkpoints, min_count=2) is True


def test_task_decomposition_validation() -> None:
    with pytest.raises(ValueError):
        decompose_goal("", ["collect"])
    with pytest.raises(ValueError):
        decomposition_is_actionable([], min_count=0)
