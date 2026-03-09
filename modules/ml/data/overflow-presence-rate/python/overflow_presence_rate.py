from __future__ import annotations


def overflow_presence_rate(lengths: list[int], max_length: int) -> tuple[int, float]:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if not lengths:
        return 0, 0.0
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    overflowing = sum(length > max_length for length in lengths)
    return overflowing, overflowing / len(lengths)
