from __future__ import annotations


def cap_frequencies(feature_counts: dict[str, int], max_count: int) -> dict[str, int]:
    if max_count <= 0:
        raise ValueError("max_count must be positive")

    capped: dict[str, int] = {}
    for feature, count in feature_counts.items():
        if count < 0:
            raise ValueError("feature counts must be non-negative")
        capped[feature] = min(count, max_count)
    return capped
