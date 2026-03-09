from __future__ import annotations


def budget_overrun_share(lengths: list[int], max_length: int) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")
    if not lengths:
        return 0.0

    total_length = sum(lengths)
    if total_length == 0:
        return 0.0

    overflow = sum(max(0, length - max_length) for length in lengths)
    return overflow / total_length
