from __future__ import annotations

import pytest

from memory_retention_policy import (
    evicted_memory_items,
    retain_top_memory_items,
    score_memory_items,
)


def test_memory_retention_policy_scores_and_keeps_top_items() -> None:
    scored = score_memory_items(
        ["User prefers CSV", "Weekly report due Friday", "Use concise tone"],
        {"csv": 2, "report": 1},
    )
    assert scored == [
        ("User prefers CSV", 2),
        ("Weekly report due Friday", 1),
        ("Use concise tone", 0),
    ]
    assert retain_top_memory_items(scored, max_items=2) == [
        "User prefers CSV",
        "Weekly report due Friday",
    ]
    assert evicted_memory_items(scored, max_items=2) == ["Use concise tone"]


def test_memory_retention_policy_validation() -> None:
    with pytest.raises(ValueError):
        retain_top_memory_items([], max_items=0)
    with pytest.raises(ValueError):
        evicted_memory_items([], max_items=0)
