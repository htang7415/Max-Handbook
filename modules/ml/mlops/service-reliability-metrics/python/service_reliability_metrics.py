from __future__ import annotations

import math


def sla_violations(latencies_ms: list[float], sla_ms: float) -> list[int]:
    if sla_ms <= 0.0:
        raise ValueError("sla_ms must be positive")
    if any(latency < 0.0 for latency in latencies_ms):
        raise ValueError("latencies_ms must be non-negative")
    return [int(latency > sla_ms) for latency in latencies_ms]


def request_sla_compliance(latencies_ms: list[float], sla_ms: float) -> tuple[int, float]:
    if sla_ms <= 0.0:
        raise ValueError("sla_ms must be positive")
    if not latencies_ms:
        return 0, 0.0
    if any(latency < 0.0 for latency in latencies_ms):
        raise ValueError("latencies_ms must be non-negative")

    compliant = len(latencies_ms) - sum(sla_violations(latencies_ms, sla_ms))
    return compliant, compliant / len(latencies_ms)


def violation_rate(violations: int, total: int) -> float:
    if violations < 0:
        raise ValueError("violations must be non-negative")
    if total < 0:
        raise ValueError("total must be non-negative")
    if violations > total:
        raise ValueError("violations must not exceed total")
    return violations / total if total > 0 else 0.0


def retry_rate(retry_counts: list[int]) -> tuple[int, float]:
    if not retry_counts:
        return 0, 0.0
    if any(count < 0 for count in retry_counts):
        raise ValueError("retry_counts must be non-negative")

    retried = sum(count > 0 for count in retry_counts)
    return retried, retried / len(retry_counts)


def queue_delay(enqueued_at: list[float], started_at: list[float]) -> tuple[list[float], float]:
    if len(enqueued_at) != len(started_at):
        raise ValueError("enqueued_at and started_at must have the same length")
    if not enqueued_at:
        return [], 0.0

    delays = queue_delay_values(enqueued_at, started_at)
    return delays, sum(delays) / len(delays)


def queue_delay_values(enqueued_at: list[float], started_at: list[float]) -> list[float]:
    if len(enqueued_at) != len(started_at):
        raise ValueError("enqueued_at and started_at must have the same length")
    delays: list[float] = []
    for arrival_time, service_time in zip(enqueued_at, started_at):
        if arrival_time < 0.0 or service_time < 0.0:
            raise ValueError("timestamps must be non-negative")
        if service_time < arrival_time:
            raise ValueError("started_at times must be at or after enqueued_at times")
        delays.append(service_time - arrival_time)
    return delays


def queue_utilization(queue_depth: int, queue_capacity: int) -> tuple[float, bool]:
    if queue_depth < 0:
        raise ValueError("queue_depth must be non-negative")
    if queue_capacity <= 0:
        raise ValueError("queue_capacity must be positive")

    utilization = queue_depth / queue_capacity
    return utilization, queue_depth >= queue_capacity


def _percentile(sorted_values: list[float], quantile: float) -> float:
    if len(sorted_values) == 1:
        return sorted_values[0]

    position = (len(sorted_values) - 1) * quantile
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        return sorted_values[lower_index]

    weight = position - lower_index
    return sorted_values[lower_index] * (1.0 - weight) + sorted_values[upper_index] * weight


def queue_age_percentiles(queue_ages: list[float]) -> tuple[float, float]:
    if not queue_ages:
        return 0.0, 0.0
    if any(age < 0.0 for age in queue_ages):
        raise ValueError("queue_ages must be non-negative")

    sorted_ages = sorted(queue_ages)
    return _percentile(sorted_ages, 0.5), _percentile(sorted_ages, 0.95)


def queue_backlog_ratio(queue_ages: list[float], target_age: float) -> tuple[list[float], float]:
    if target_age <= 0.0:
        raise ValueError("target_age must be positive")
    if not queue_ages:
        return [], 0.0
    if any(age < 0.0 for age in queue_ages):
        raise ValueError("queue_ages must be non-negative")

    ratios = [age / target_age for age in queue_ages]
    return ratios, sum(ratios) / len(ratios)


def saturation_rate(utilizations: list[float], threshold: float = 1.0) -> tuple[int, float]:
    if threshold < 0.0:
        raise ValueError("threshold must be non-negative")
    if not utilizations:
        return 0, 0.0
    if any(utilization < 0.0 for utilization in utilizations):
        raise ValueError("utilizations must be non-negative")

    saturated = sum(utilization >= threshold for utilization in utilizations)
    return saturated, saturated / len(utilizations)
