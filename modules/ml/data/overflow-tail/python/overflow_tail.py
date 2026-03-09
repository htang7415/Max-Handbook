from __future__ import annotations

import math


def overflow_tail(lengths: list[int], max_length: int, quantile: float = 0.95) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if not 0.0 <= quantile <= 1.0:
        raise ValueError("quantile must satisfy 0 <= quantile <= 1")
    if not lengths:
        return 0.0
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    overflow = sorted(max(0, length - max_length) for length in lengths)
    if len(overflow) == 1:
        return float(overflow[0])

    position = (len(overflow) - 1) * quantile
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return float(overflow[lower_index])

    weight = position - lower_index
    return overflow[lower_index] * (1.0 - weight) + overflow[upper_index] * weight
