from __future__ import annotations

import pytest

from retrieval_backed_memory import index_memories, memory_context, retrieve_memory_hits


def test_retrieval_backed_memory_indexes_retrieves_and_formats_context() -> None:
    store = index_memories(["User prefers CSV", "Weekly report due Friday", "Use concise tone"])
    hits = retrieve_memory_hits("csv report", store, k=2)
    assert hits == ["User prefers CSV", "Weekly report due Friday"]
    assert memory_context(hits, max_items=2) == "- User prefers CSV\n- Weekly report due Friday"


def test_retrieval_backed_memory_validation() -> None:
    assert index_memories(["", "  "]) == []
    with pytest.raises(ValueError):
        retrieve_memory_hits("query", [], k=0)
    with pytest.raises(ValueError):
        memory_context(["A"], max_items=0)
