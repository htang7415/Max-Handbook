from __future__ import annotations

import math


def _quantile(sorted_values: list[float], q: float) -> float:
    position = q * (len(sorted_values) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1.0 - weight) + sorted_values[upper] * weight


def robust_scale(values: list[float]) -> list[float]:
    if not values:
        return []

    sorted_values = sorted(values)
    median = _quantile(sorted_values, 0.5)
    q1 = _quantile(sorted_values, 0.25)
    q3 = _quantile(sorted_values, 0.75)
    iqr = q3 - q1
    if iqr == 0.0:
        return [0.0 for _ in values]
    return [(value - median) / iqr for value in values]
