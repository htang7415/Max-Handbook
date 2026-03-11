from __future__ import annotations


def _rate(outcomes: list[bool]) -> float:
    if not outcomes:
        raise ValueError("outcomes must be non-empty")
    return sum(1 for outcome in outcomes if outcome) / len(outcomes)


def task_success_rate(outcomes: list[bool]) -> float:
    return _rate(outcomes)


def tool_call_success_rate(outcomes: list[bool]) -> float:
    return _rate(outcomes)


def mean_latency_ms(latencies_ms: list[float]) -> float:
    if not latencies_ms:
        raise ValueError("latencies_ms must be non-empty")
    if any(latency < 0 for latency in latencies_ms):
        raise ValueError("latencies_ms must be non-negative")
    return sum(latencies_ms) / len(latencies_ms)


def failure_breakdown(labels: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for label in labels:
        cleaned = label.strip()
        if not cleaned:
            continue
        counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts
