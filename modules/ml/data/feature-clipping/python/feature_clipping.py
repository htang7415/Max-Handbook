from __future__ import annotations


def clip_features(values: list[float], min_value: float, max_value: float) -> list[float]:
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")

    return [min(max(value, min_value), max_value) for value in values]
