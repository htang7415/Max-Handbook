from __future__ import annotations


def memory_evidence_score(recency_score: float, source_trust: float, confirmations: int) -> float:
    if not 0.0 <= recency_score <= 1.0:
        raise ValueError("recency_score must satisfy 0 <= value <= 1")
    if not 0.0 <= source_trust <= 1.0:
        raise ValueError("source_trust must satisfy 0 <= value <= 1")
    if confirmations < 0:
        raise ValueError("confirmations must be non-negative")

    confirmation_score = min(confirmations, 3) / 3
    return 0.4 * recency_score + 0.4 * source_trust + 0.2 * confirmation_score


def rank_conflicting_memories(memories: list[dict[str, object]]) -> list[dict[str, object]]:
    if not memories:
        raise ValueError("memories must be non-empty")

    ranked: list[dict[str, object]] = []
    for memory in memories:
        memory_id = str(memory.get("memory_id", "")).strip()
        if not memory_id:
            raise ValueError("memory_id must be non-empty")
        score = memory_evidence_score(
            recency_score=float(memory.get("recency_score", 0.0)),
            source_trust=float(memory.get("source_trust", 0.0)),
            confirmations=int(memory.get("confirmations", 0)),
        )
        ranked.append({"memory_id": memory_id, "score": score})

    return sorted(ranked, key=lambda item: (-float(item["score"]), str(item["memory_id"])))


def memory_conflict_route(memories: list[dict[str, object]], min_score: float, min_margin: float = 0.0) -> str:
    if not 0.0 <= min_score <= 1.0:
        raise ValueError("min_score must satisfy 0 <= value <= 1")
    if min_margin < 0.0:
        raise ValueError("min_margin must be non-negative")

    ranked = rank_conflicting_memories(memories)
    top_score = float(ranked[0]["score"])
    if top_score < min_score:
        return "review"
    second_score = float(ranked[1]["score"]) if len(ranked) > 1 else 0.0
    if top_score - second_score < min_margin:
        return "review"
    return str(ranked[0]["memory_id"])
