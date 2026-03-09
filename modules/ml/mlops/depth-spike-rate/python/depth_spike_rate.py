from __future__ import annotations


def depth_spike_rate(depths: list[int], threshold: int) -> tuple[int, float]:
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    if not depths:
        return 0, 0.0
    if any(depth < 0 for depth in depths):
        raise ValueError("depths must be non-negative")

    spikes = sum(depth > threshold for depth in depths)
    return spikes, spikes / len(depths)
