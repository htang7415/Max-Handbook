from __future__ import annotations


def agreement_rate(outcomes: list[str | int]) -> float:
    if not outcomes:
        return 0.0

    counts: dict[str | int, int] = {}
    for outcome in outcomes:
        counts[outcome] = counts.get(outcome, 0) + 1
    return max(counts.values()) / len(outcomes)
