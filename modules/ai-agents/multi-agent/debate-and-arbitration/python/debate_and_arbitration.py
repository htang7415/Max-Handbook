from __future__ import annotations


def normalize_candidate(text: str) -> str:
    return " ".join(text.strip().lower().split())


def vote_counts(candidates: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for candidate in candidates:
        normalized = normalize_candidate(candidate)
        if not normalized:
            continue
        counts[normalized] = counts.get(normalized, 0) + 1
    return counts


def agreement_rate(candidates: list[str]) -> float:
    counts = vote_counts(candidates)
    total = sum(counts.values())
    if total == 0:
        raise ValueError("candidates must contain at least one non-empty answer")
    return max(counts.values()) / total


def arbitrate_majority(candidates: list[str]) -> str | None:
    counts = vote_counts(candidates)
    if not counts:
        return None
    winner = max(counts.items(), key=lambda item: (item[1], item[0]))
    return winner[0]
