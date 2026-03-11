from __future__ import annotations


def remaining_budget_ms(total_deadline_ms: int, elapsed_ms: int) -> int:
    if total_deadline_ms < 0 or elapsed_ms < 0:
        raise ValueError("time values must be non-negative")
    return max(0, total_deadline_ms - elapsed_ms)


def can_start_step(remaining_budget_ms: int, step_timeout_ms: int, cleanup_reserve_ms: int = 0) -> bool:
    if remaining_budget_ms < 0 or step_timeout_ms < 0 or cleanup_reserve_ms < 0:
        raise ValueError("time values must be non-negative")
    return remaining_budget_ms >= step_timeout_ms + cleanup_reserve_ms


def execution_state(cancel_requested: bool, remaining_budget_ms: int) -> str:
    if remaining_budget_ms < 0:
        raise ValueError("remaining_budget_ms must be non-negative")
    if cancel_requested:
        return "cancelled"
    if remaining_budget_ms == 0:
        return "timed_out"
    return "running"
