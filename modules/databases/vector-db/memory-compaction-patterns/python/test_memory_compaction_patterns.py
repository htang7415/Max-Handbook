from memory_compaction_patterns import compact_memories, memory_score, raw_memory_ids, summary_text
import pytest


def test_raw_memory_selection_keeps_pinned_and_recent_high_value_items():
    memories = [
        {"id": "m1", "topic": "retrieval", "text": "Old note", "created_at": 10, "importance": 0.4},
        {"id": "m2", "topic": "retrieval", "text": "Switch to hybrid search", "created_at": 20, "importance": 0.6},
        {"id": "m3", "topic": "ops", "text": "Page on-call", "created_at": 190, "importance": 0.9, "pinned": True},
        {"id": "m4", "topic": "retrieval", "text": "Reranker fixed support docs", "created_at": 195, "importance": 0.8},
    ]

    assert raw_memory_ids(memories, now=200, keep_raw=2) == ["m3", "m4"]


def test_compaction_summarizes_older_memories_by_topic():
    memories = [
        {"id": "m1", "topic": "retrieval", "text": "Old note", "created_at": 10, "importance": 0.4},
        {"id": "m2", "topic": "retrieval", "text": "Switch to hybrid search", "created_at": 20, "importance": 0.6},
        {"id": "m3", "topic": "ops", "text": "Page on-call", "created_at": 190, "importance": 0.9, "pinned": True},
        {"id": "m4", "topic": "retrieval", "text": "Reranker fixed support docs", "created_at": 195, "importance": 0.8},
    ]

    compacted = compact_memories(memories, now=200, keep_raw=2)

    assert [memory["id"] for memory in compacted] == ["summary:retrieval", "m3", "m4"]
    assert compacted[0]["kind"] == "summary"
    assert compacted[0]["text"] == "Summary of retrieval: Old note | Switch to hybrid search"
    assert summary_text(memories[:2]) == "Old note | Switch to hybrid search"


def test_invalid_memory_ranges_are_rejected():
    with pytest.raises(ValueError, match="keep_raw"):
        raw_memory_ids([], now=200, keep_raw=-1)

    with pytest.raises(ValueError, match="importance"):
        memory_score({"id": "m1", "text": "bad", "created_at": 100, "importance": 2.0}, now=200)
