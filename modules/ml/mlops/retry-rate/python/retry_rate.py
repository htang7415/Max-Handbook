from __future__ import annotations


def retry_rate(retry_counts: list[int]) -> tuple[int, float]:
    if not retry_counts:
        return 0, 0.0
    if any(count < 0 for count in retry_counts):
        raise ValueError("retry_counts must be non-negative")

    retried = sum(count > 0 for count in retry_counts)
    return retried, retried / len(retry_counts)
