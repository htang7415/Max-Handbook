from __future__ import annotations


def _normalize_candidate(candidate: str) -> str:
    return " ".join(candidate.lower().split())


def candidate_diversity(candidates: list[str]) -> float:
    if not candidates:
        return 0.0

    normalized = {_normalize_candidate(candidate) for candidate in candidates}
    return len(normalized) / len(candidates)
