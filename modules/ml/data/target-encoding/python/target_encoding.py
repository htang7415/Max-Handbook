from __future__ import annotations


def target_encoding_map(categories: list[str], targets: list[float]) -> dict[str, float]:
    if len(categories) != len(targets):
        raise ValueError("categories and targets must have the same length")
    if not categories:
        return {}

    sums: dict[str, float] = {}
    counts: dict[str, int] = {}

    for category, target in zip(categories, targets):
        sums[category] = sums.get(category, 0.0) + target
        counts[category] = counts.get(category, 0) + 1

    return {category: sums[category] / counts[category] for category in sums}
