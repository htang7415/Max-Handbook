from __future__ import annotations


def budget_token_segments(segment_lengths: list[int], max_tokens: int) -> tuple[list[int], int]:
    if max_tokens < 0:
        raise ValueError("max_tokens must be non-negative")
    if any(length < 0 for length in segment_lengths):
        raise ValueError("segment_lengths must be non-negative")

    remaining = max_tokens
    allocated: list[int] = []
    for length in segment_lengths:
        keep = min(length, remaining)
        allocated.append(keep)
        remaining -= keep

    dropped = sum(segment_lengths) - sum(allocated)
    return allocated, dropped
