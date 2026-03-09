from __future__ import annotations

from collections import Counter


def count_vector(tokens: list[str], vocabulary: list[str]) -> list[int]:
    if len(set(vocabulary)) != len(vocabulary):
        raise ValueError("vocabulary must contain unique terms")

    counts = Counter(tokens)
    return [counts.get(term, 0) for term in vocabulary]
