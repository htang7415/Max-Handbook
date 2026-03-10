from __future__ import annotations

import math


def _validate_lengths(lengths: list[int], max_length: int) -> None:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")


def _overflow_amounts(lengths: list[int], max_length: int) -> list[int]:
    _validate_lengths(lengths, max_length)
    return [max(0, length - max_length) for length in lengths]


def truncation_rate(lengths: list[int], max_length: int) -> tuple[int, float]:
    overflow = _overflow_amounts(lengths, max_length)
    if not overflow:
        return 0, 0.0

    truncated = sum(value > 0 for value in overflow)
    return truncated, truncated / len(overflow)


def budget_overrun_share(lengths: list[int], max_length: int) -> float:
    overflow = _overflow_amounts(lengths, max_length)
    if not overflow:
        return 0.0

    total_length = sum(lengths)
    if total_length == 0:
        return 0.0
    return sum(overflow) / total_length


def overflow_quantile(lengths: list[int], max_length: int, quantile: float) -> float:
    if not 0.0 <= quantile <= 1.0:
        raise ValueError("quantile must satisfy 0 <= quantile <= 1")

    overflow = sorted(_overflow_amounts(lengths, max_length))
    if not overflow:
        return 0.0
    if len(overflow) == 1:
        return float(overflow[0])

    position = (len(overflow) - 1) * quantile
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return float(overflow[lower_index])

    weight = position - lower_index
    return overflow[lower_index] * (1.0 - weight) + overflow[upper_index] * weight


def overflow_cutoff_rate(lengths: list[int], max_length: int, cutoff: int) -> float:
    if cutoff < 0:
        raise ValueError("cutoff must be non-negative")

    overflow = _overflow_amounts(lengths, max_length)
    if not overflow:
        return 0.0
    return sum(value >= cutoff for value in overflow) / len(overflow)


def overflow_cutoff_tail_mass(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
    if cutoff < 0:
        raise ValueError("cutoff must be non-negative")
    if not 0.0 <= quantile <= 1.0:
        raise ValueError("quantile must satisfy 0 <= quantile <= 1")

    overflow = sorted(value for value in _overflow_amounts(lengths, max_length) if value >= cutoff)
    if not overflow:
        return 0.0
    if len(overflow) == 1:
        return 1.0

    threshold = overflow_quantile(
        [max_length + value for value in overflow],
        max_length=max_length,
        quantile=quantile,
    )
    total_mass = sum(overflow)
    tail_mass = sum(value for value in overflow if value >= threshold)
    return 0.0 if total_mass == 0 else tail_mass / total_mass
