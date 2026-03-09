from __future__ import annotations


def frequency_encoding_map(categories: list[str]) -> dict[str, float]:
    if not categories:
        return {}

    counts: dict[str, int] = {}
    for category in categories:
        counts[category] = counts.get(category, 0) + 1

    total = len(categories)
    return {category: count / total for category, count in counts.items()}
