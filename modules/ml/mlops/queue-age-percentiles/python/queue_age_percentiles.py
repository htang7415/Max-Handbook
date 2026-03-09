from __future__ import annotations

import math


def _percentile(sorted_values: list[float], quantile: float) -> float:
    if len(sorted_values) == 1:
        return sorted_values[0]

    position = (len(sorted_values) - 1) * quantile
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return sorted_values[lower_index]

    weight = position - lower_index
    return (
        sorted_values[lower_index] * (1.0 - weight)
        + sorted_values[upper_index] * weight
    )


def queue_age_percentiles(queue_ages: list[float]) -> tuple[float, float]:
    if not queue_ages:
        return 0.0, 0.0
    if any(age < 0.0 for age in queue_ages):
        raise ValueError("queue_ages must be non-negative")

    sorted_ages = sorted(queue_ages)
    return _percentile(sorted_ages, 0.5), _percentile(sorted_ages, 0.95)
