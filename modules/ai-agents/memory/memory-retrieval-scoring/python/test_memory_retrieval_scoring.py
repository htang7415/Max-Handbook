from __future__ import annotations

import pytest

from memory_retrieval_scoring import (
    best_memory_match,
    score_memory_for_query,
    top_scored_memories,
)


def test_memory_retrieval_scoring_ranks_memories() -> None:
    memories = [
        {"text": "User prefers CSV output", "priority": 1},
        {"text": "Weekly report due Friday", "priority": 0},
        {"text": "Need manager approval", "priority": 2},
    ]
    scored = score_memory_for_query("csv report", memories)
    assert scored == [
        ("User prefers CSV output", 2),
        ("Need manager approval", 2),
        ("Weekly report due Friday", 1),
    ]
    assert top_scored_memories(scored, k=2) == [
        "User prefers CSV output",
        "Need manager approval",
    ]
    assert best_memory_match("csv report", memories) == "User prefers CSV output"


def test_memory_retrieval_scoring_validation_and_empty_case() -> None:
    assert best_memory_match("query", []) is None
    with pytest.raises(ValueError):
        top_scored_memories([], k=0)
