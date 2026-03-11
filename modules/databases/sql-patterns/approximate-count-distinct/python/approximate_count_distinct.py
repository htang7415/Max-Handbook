"""approximate_count_distinct - simple linear-counting style cardinality estimate."""

from __future__ import annotations

import math


def stable_bucket(value: str, bucket_count: int) -> int:
    if bucket_count <= 1:
        raise ValueError("bucket_count must be greater than 1")
    stable_hash = sum((index + 1) * ord(char) for index, char in enumerate(value))
    return stable_hash % bucket_count


def exact_count_distinct(values: list[str]) -> int:
    return len(set(values))


def approximate_count_distinct(values: list[str], bucket_count: int) -> int:
    occupied = {stable_bucket(value, bucket_count) for value in set(values)}
    filled = len(occupied)
    if filled >= bucket_count:
        return bucket_count
    estimate = -bucket_count * math.log(1 - (filled / bucket_count))
    return max(int(round(estimate)), filled)


def count_distinct_summary(values: list[str], bucket_count: int) -> dict[str, int]:
    exact = exact_count_distinct(values)
    approximate = approximate_count_distinct(values, bucket_count)
    return {
        "exact": exact,
        "approximate": approximate,
        "absolute_error": abs(approximate - exact),
    }
