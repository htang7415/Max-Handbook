"""memory_compaction_patterns - keep important memories raw and summarize the rest."""

from __future__ import annotations


def validate_importance(importance: float) -> None:
    if not 0.0 <= importance <= 1.0:
        raise ValueError("importance must be between 0 and 1")


def validate_recency_window(recency_window: int) -> None:
    if recency_window <= 0:
        raise ValueError("recency_window must be positive")


def validate_keep_raw(keep_raw: int) -> None:
    if keep_raw < 0:
        raise ValueError("keep_raw must be non-negative")


def memory_score(
    memory: dict[str, object],
    now: int,
    recency_window: int = 3600,
) -> float:
    validate_recency_window(recency_window)
    importance = float(memory.get("importance", 0.5))
    validate_importance(importance)
    if memory.get("pinned"):
        return 1000.0 + importance
    age = max(now - int(memory["created_at"]), 0)
    recency = max(0.0, 1.0 - (age / recency_window))
    return (0.7 * importance) + (0.3 * recency)


def raw_memory_ids(
    memories: list[dict[str, object]],
    now: int,
    keep_raw: int,
) -> list[str]:
    validate_keep_raw(keep_raw)
    ranked = sorted(
        memories,
        key=lambda memory: (
            -memory_score(memory, now),
            -int(memory["created_at"]),
            str(memory["id"]),
        ),
    )
    return [str(memory["id"]) for memory in ranked[:keep_raw]]


def summary_text(memories: list[dict[str, object]]) -> str:
    ordered = sorted(memories, key=lambda memory: (int(memory["created_at"]), str(memory["id"])))
    return " | ".join(str(memory["text"]) for memory in ordered)


def compact_memories(
    memories: list[dict[str, object]],
    now: int,
    keep_raw: int,
) -> list[dict[str, object]]:
    validate_keep_raw(keep_raw)
    kept_ids = set(raw_memory_ids(memories, now, keep_raw))
    kept_raw = [dict(memory) for memory in memories if str(memory["id"]) in kept_ids]

    grouped: dict[str, list[dict[str, object]]] = {}
    for memory in memories:
        if str(memory["id"]) in kept_ids:
            continue
        grouped.setdefault(str(memory.get("topic", "general")), []).append(memory)

    summaries: list[dict[str, object]] = []
    for topic, topic_memories in sorted(grouped.items()):
        summaries.append(
            {
                "id": f"summary:{topic}",
                "topic": topic,
                "text": f"Summary of {topic}: {summary_text(topic_memories)}",
                "created_at": max(int(memory["created_at"]) for memory in topic_memories),
                "importance": max(float(memory.get("importance", 0.5)) for memory in topic_memories),
                "kind": "summary",
            }
        )

    combined = kept_raw + summaries
    return sorted(combined, key=lambda memory: (int(memory["created_at"]), str(memory["id"])))
