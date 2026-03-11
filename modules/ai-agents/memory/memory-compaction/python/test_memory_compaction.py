from __future__ import annotations

import pytest

from memory_compaction import (
    append_compacted_summary,
    compact_memories,
    compacted_item_count,
)


def test_memory_compaction_builds_and_extends_summary() -> None:
    summary = compact_memories(
        ["User prefers CSV", "Weekly report due Friday", "Use concise tone"],
        max_items=2,
    )
    assert summary == "Weekly report due Friday | Use concise tone"
    updated = append_compacted_summary(summary, "Send report before noon")
    assert updated == "Weekly report due Friday | Use concise tone | Send report before noon"
    assert compacted_item_count(updated) == 3


def test_memory_compaction_validation() -> None:
    with pytest.raises(ValueError):
        compact_memories(["A"], max_items=0)
    assert append_compacted_summary("", "A") == "A"
    assert compacted_item_count("") == 0
