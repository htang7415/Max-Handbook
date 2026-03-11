from __future__ import annotations


def remaining_latency_budget_ms(total_budget_ms: int, observed_steps_ms: list[int]) -> int:
    if total_budget_ms < 0 or any(step < 0 for step in observed_steps_ms):
        raise ValueError("latencies must be non-negative")
    return max(0, total_budget_ms - sum(observed_steps_ms))


def latency_budget_exceeded(total_budget_ms: int, observed_steps_ms: list[int]) -> bool:
    return remaining_latency_budget_ms(total_budget_ms, observed_steps_ms) == 0 and sum(
        observed_steps_ms
    ) > total_budget_ms


def largest_latency_contributor(step_latencies_ms: dict[str, int]) -> str:
    if not step_latencies_ms:
        raise ValueError("step_latencies_ms must be non-empty")
    if any(latency < 0 for latency in step_latencies_ms.values()):
        raise ValueError("latencies must be non-negative")
    return max(step_latencies_ms, key=step_latencies_ms.get)
