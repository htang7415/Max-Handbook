from __future__ import annotations

import pytest

from cancellation_deadlines_and_timeouts import (
    can_start_step,
    execution_state,
    remaining_budget_ms,
)


def test_remaining_budget_and_start_checks_use_explicit_deadline_budget() -> None:
    assert remaining_budget_ms(total_deadline_ms=1200, elapsed_ms=300) == 900
    assert can_start_step(remaining_budget_ms=900, step_timeout_ms=400, cleanup_reserve_ms=100) is True
    assert can_start_step(remaining_budget_ms=900, step_timeout_ms=850, cleanup_reserve_ms=100) is False


def test_execution_state_distinguishes_running_cancelled_and_timed_out() -> None:
    assert execution_state(cancel_requested=False, remaining_budget_ms=900) == "running"
    assert execution_state(cancel_requested=True, remaining_budget_ms=900) == "cancelled"
    assert execution_state(cancel_requested=False, remaining_budget_ms=0) == "timed_out"


def test_time_values_must_be_non_negative() -> None:
    with pytest.raises(ValueError):
        remaining_budget_ms(total_deadline_ms=-1, elapsed_ms=0)
    with pytest.raises(ValueError):
        can_start_step(remaining_budget_ms=1, step_timeout_ms=-1)
