from __future__ import annotations

import math


def _validate_observations(observations: list[float], capacity: float) -> None:
    if capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")


def _bucket_counts(observations: list[float], capacity: float, cutoffs: list[float]) -> tuple[list[int], int]:
    _validate_observations(observations, capacity)
    if any(cutoff < 0.0 for cutoff in cutoffs):
        raise ValueError("cutoffs must be non-negative")
    if any(left > right for left, right in zip(cutoffs, cutoffs[1:])):
        raise ValueError("cutoffs must be sorted")

    counts = [0] * (len(cutoffs) + 1)
    breached_count = 0
    for observation in observations:
        if observation <= capacity:
            continue

        breached_count += 1
        excess_ratio = (observation - capacity) / capacity
        bucket_index = len(cutoffs)
        for index, cutoff in enumerate(cutoffs):
            if excess_ratio <= cutoff:
                bucket_index = index
                break
        counts[bucket_index] += 1

    return counts, breached_count


def capacity_breach_rate(observations: list[float], capacity: float) -> tuple[int, float]:
    _validate_observations(observations, capacity)
    if not observations:
        return 0, 0.0

    breaches = sum(observation > capacity for observation in observations)
    return breaches, breaches / len(observations)


def headroom_gap(observations: list[float], ceiling: float) -> tuple[list[float], float]:
    if ceiling < 0.0:
        raise ValueError("ceiling must be non-negative")
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")
    if not observations:
        return [], 0.0

    gaps = [ceiling - observation for observation in observations]
    return gaps, sum(gaps) / len(gaps)


def overload_margin(observations: list[float], capacity: float) -> float:
    _validate_observations(observations, capacity)
    if not observations:
        return 0.0
    return sum(max(0.0, observation - capacity) for observation in observations) / len(observations)


def pressure_score(observations: list[float], capacity: float) -> float:
    _validate_observations(observations, capacity)
    if not observations:
        return 0.0

    total = 0.0
    for observation in observations:
        if observation > capacity:
            total += 1.0 + (observation - capacity) / capacity
    return total / len(observations)


def surge_pressure(observations: list[float], capacity: float) -> float:
    _validate_observations(observations, capacity)
    if not observations:
        return 0.0

    total = 0.0
    for observation in observations:
        if observation > capacity:
            excess_ratio = (observation - capacity) / capacity
            total += excess_ratio * excess_ratio
    return total / len(observations)


def breach_bucket_share(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
    counts, breached_count = _bucket_counts(observations, capacity, cutoffs)
    if breached_count == 0:
        return [0.0] * len(counts)
    return [count / breached_count for count in counts]


def breach_bucket_entropy(observations: list[float], capacity: float, cutoffs: list[float]) -> float:
    counts, breached_count = _bucket_counts(observations, capacity, cutoffs)
    if breached_count == 0:
        return 0.0
    return -sum(
        (count / breached_count) * math.log(count / breached_count)
        for count in counts
        if count > 0
    )


def breach_bucket_slope(observations: list[float], capacity: float, cutoffs: list[float]) -> float:
    counts, breached_count = _bucket_counts(observations, capacity, cutoffs)
    if breached_count == 0 or len(counts) < 2:
        return 0.0

    shares = [count / breached_count for count in counts]
    return max(abs(right - left) for left, right in zip(shares, shares[1:]))


def breach_bucket_tail(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
    tail_buckets: int = 1,
) -> float:
    if tail_buckets <= 0:
        raise ValueError("tail_buckets must be positive")

    counts, breached_count = _bucket_counts(observations, capacity, cutoffs)
    if breached_count == 0:
        return 0.0

    tail_bucket_count = min(tail_buckets, len(counts))
    return sum(counts[-tail_bucket_count:]) / breached_count
