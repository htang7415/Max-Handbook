"""cache_admission_policies - compare always-admit caching to simple frequency gates."""

from __future__ import annotations


def validate_min_hits(min_hits: int) -> None:
    if min_hits <= 0:
        raise ValueError("min_hits must be positive")


def request_counts(stream: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for key in stream:
        counts[key] = counts.get(key, 0) + 1
    return counts


def admit_always(key: str) -> bool:
    del key
    return True


def admit_on_frequency(key: str, counts: dict[str, int], min_hits: int) -> bool:
    validate_min_hits(min_hits)
    return counts.get(key, 0) >= min_hits


def admitted_keys(stream: list[str], min_hits: int) -> dict[str, list[str]]:
    validate_min_hits(min_hits)
    counts = request_counts(stream)
    ordered_unique: list[str] = []
    seen: set[str] = set()
    for key in stream:
        if key not in seen:
            ordered_unique.append(key)
            seen.add(key)

    frequency_admitted = [
        key
        for key in ordered_unique
        if admit_on_frequency(key, counts, min_hits)
    ]
    rejected = [
        key
        for key in ordered_unique
        if not admit_on_frequency(key, counts, min_hits)
    ]
    return {
        "always": [key for key in ordered_unique if admit_always(key)],
        "frequency_threshold": frequency_admitted,
        "rejected_by_frequency": rejected,
    }
