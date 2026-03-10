from __future__ import annotations

import math
from collections.abc import Mapping


def log_rate(event_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if event_count < 0:
        raise ValueError("event_count must be non-negative")
    if event_count > total_count:
        raise ValueError("event_count cannot exceed total_count")
    if event_count == 0:
        return float("-inf")
    return math.log(event_count / total_count)


def log_rate_table(event_counts: Mapping[str, int], total_count: int) -> dict[str, float]:
    return {
        name: log_rate(count, total_count)
        for name, count in event_counts.items()
    }
