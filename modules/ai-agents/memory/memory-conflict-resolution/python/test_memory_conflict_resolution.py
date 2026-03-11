from __future__ import annotations

import pytest

from memory_conflict_resolution import (
    memory_conflict_route,
    memory_evidence_score,
    rank_conflicting_memories,
)


def test_memory_conflict_resolution_ranks_memories_by_evidence() -> None:
    memories = [
        {"memory_id": "m1", "recency_score": 0.9, "source_trust": 0.8, "confirmations": 2},
        {"memory_id": "m2", "recency_score": 0.6, "source_trust": 0.9, "confirmations": 3},
    ]

    assert memory_evidence_score(0.9, 0.8, 2) == pytest.approx(0.8133333333)
    assert rank_conflicting_memories(memories) == [
        {"memory_id": "m1", "score": pytest.approx(0.8133333333)},
        {"memory_id": "m2", "score": pytest.approx(0.8)},
    ]
    assert memory_conflict_route(memories, min_score=0.7, min_margin=0.01) == "m1"


def test_memory_conflict_resolution_reviews_weak_or_ambiguous_conflicts() -> None:
    assert (
        memory_conflict_route(
            [{"memory_id": "m1", "recency_score": 0.4, "source_trust": 0.4, "confirmations": 0}],
            min_score=0.5,
        )
        == "review"
    )
    assert (
        memory_conflict_route(
            [
                {"memory_id": "m1", "recency_score": 0.8, "source_trust": 0.8, "confirmations": 1},
                {"memory_id": "m2", "recency_score": 0.7, "source_trust": 0.9, "confirmations": 1},
            ],
            min_score=0.6,
            min_margin=0.05,
        )
        == "review"
    )


def test_memory_conflict_resolution_validation() -> None:
    with pytest.raises(ValueError):
        memory_evidence_score(1.1, 0.5, 1)
    with pytest.raises(ValueError):
        rank_conflicting_memories([])
    with pytest.raises(ValueError):
        memory_conflict_route([{"memory_id": "", "recency_score": 0.5, "source_trust": 0.5, "confirmations": 0}], min_score=0.5)
