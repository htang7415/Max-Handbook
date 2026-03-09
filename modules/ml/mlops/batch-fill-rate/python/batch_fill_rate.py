from __future__ import annotations


def batch_fill_rate(batch_sizes: list[int], max_batch_size: int) -> float:
    if max_batch_size <= 0:
        raise ValueError("max_batch_size must be positive")
    if any(batch_size < 0 for batch_size in batch_sizes):
        raise ValueError("batch_sizes must be non-negative")
    if any(batch_size > max_batch_size for batch_size in batch_sizes):
        raise ValueError("batch_sizes cannot exceed max_batch_size")
    if not batch_sizes:
        return 0.0

    average_batch_size = sum(batch_sizes) / len(batch_sizes)
    return average_batch_size / max_batch_size
