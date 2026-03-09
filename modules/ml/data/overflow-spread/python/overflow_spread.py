from __future__ import annotations

import math


def _quantile(values: list[int], quantile: float) -> float:
    if len(values) == 1:
        return float(values[0])

    position = (len(values) - 1) * quantile
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return float(values[lower_index])

    weight = position - lower_index
    return values[lower_index] * (1.0 - weight) + values[upper_index] * weight


def overflow_spread(
    lengths: list[int],
    max_length: int,
    low_quantile: float = 0.5,
    high_quantile: float = 0.95,
) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if not 0.0 <= low_quantile <= 1.0 or not 0.0 <= high_quantile <= 1.0:
        raise ValueError("quantiles must satisfy 0 <= q <= 1")
    if low_quantile > high_quantile:
        raise ValueError("low_quantile must be less than or equal to high_quantile")
    if not lengths:
        return 0.0
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    overflow = sorted(max(0, length - max_length) for length in lengths)
    return _quantile(overflow, high_quantile) - _quantile(overflow, low_quantile)
