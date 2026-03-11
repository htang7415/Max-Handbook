from __future__ import annotations

import pytest

from memory_patterns import (
    append_memory,
    retrieve_relevant_memories,
    summarize_recent_memory,
)


def test_memory_patterns_append_summarize_and_retrieve() -> None:
    memory = append_memory([], "User prefers CSV output", max_items=3)
    memory = append_memory(memory, "Need weekly totals", max_items=3)
    memory = append_memory(memory, "Send report on Friday", max_items=3)
    assert memory == [
        "User prefers CSV output",
        "Need weekly totals",
        "Send report on Friday",
    ]
    assert summarize_recent_memory(memory, max_items=2) == (
        "Need weekly totals | Send report on Friday"
    )
    assert retrieve_relevant_memories("csv weekly report", memory, k=2) == [
        "Need weekly totals",
        "User prefers CSV output",
    ]


def test_memory_patterns_validation_and_trimming() -> None:
    trimmed = append_memory(["A", "B"], "C", max_items=2)
    assert trimmed == ["B", "C"]
    with pytest.raises(ValueError):
        append_memory([], "A", max_items=0)
    with pytest.raises(ValueError):
        summarize_recent_memory(["A"], max_items=0)
    with pytest.raises(ValueError):
        retrieve_relevant_memories("query", ["A"], k=0)
