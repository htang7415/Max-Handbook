from __future__ import annotations

import pytest

from budgeted_multi_step_planning import (
    budgeted_plan_route,
    max_executable_steps,
    per_step_budget,
)


def test_budgeted_multi_step_planning_splits_budget_and_executes_full_plan() -> None:
    assert per_step_budget(total_budget=4.0, step_count=3, reserve_budget=0.5) == pytest.approx(1.1666666667)
    assert max_executable_steps([1.0, 1.5, 1.0], total_budget=4.0, reserve_budget=0.5) == 3
    assert budgeted_plan_route([1.0, 1.5, 1.0], total_budget=4.0, reserve_budget=0.5) == "execute-all"


def test_budgeted_multi_step_planning_distinguishes_trim_and_review() -> None:
    assert budgeted_plan_route([2.0, 2.0, 2.0], total_budget=3.0, reserve_budget=0.5) == "trim-plan"
    assert budgeted_plan_route([2.0, 2.0], total_budget=1.5, reserve_budget=0.5) == "review"


def test_budgeted_multi_step_planning_validation() -> None:
    with pytest.raises(ValueError):
        per_step_budget(total_budget=1.0, step_count=0)
    with pytest.raises(ValueError):
        max_executable_steps([], total_budget=1.0)
    with pytest.raises(ValueError):
        max_executable_steps([1.0], total_budget=1.0, reserve_budget=1.0)
    with pytest.raises(ValueError):
        max_executable_steps([1.0, -1.0], total_budget=2.0)
