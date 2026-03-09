from __future__ import annotations


def request_sla_compliance(
    latencies_ms: list[float],
    sla_ms: float,
) -> tuple[int, float]:
    if sla_ms <= 0.0:
        raise ValueError("sla_ms must be positive")
    if not latencies_ms:
        return 0, 0.0
    if any(latency < 0.0 for latency in latencies_ms):
        raise ValueError("latencies_ms must be non-negative")

    compliant = sum(latency <= sla_ms for latency in latencies_ms)
    return compliant, compliant / len(latencies_ms)
