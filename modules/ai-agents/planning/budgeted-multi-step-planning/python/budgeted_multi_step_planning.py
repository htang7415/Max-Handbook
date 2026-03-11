from __future__ import annotations


def per_step_budget(total_budget: float, step_count: int, reserve_budget: float = 0.0) -> float:
    if total_budget <= 0.0:
        raise ValueError("total_budget must be positive")
    if step_count <= 0:
        raise ValueError("step_count must be positive")
    if reserve_budget < 0.0:
        raise ValueError("reserve_budget must be non-negative")
    if reserve_budget >= total_budget:
        raise ValueError("reserve_budget must be smaller than total_budget")
    return (total_budget - reserve_budget) / step_count


def max_executable_steps(step_costs: list[float], total_budget: float, reserve_budget: float = 0.0) -> int:
    if not step_costs:
        raise ValueError("step_costs must be non-empty")
    remaining = total_budget - reserve_budget
    if total_budget <= 0.0:
        raise ValueError("total_budget must be positive")
    if reserve_budget < 0.0:
        raise ValueError("reserve_budget must be non-negative")
    if reserve_budget >= total_budget:
        raise ValueError("reserve_budget must be smaller than total_budget")

    count = 0
    for cost in step_costs:
        if cost < 0.0:
            raise ValueError("step_costs must be non-negative")
        if cost <= remaining:
            remaining -= cost
            count += 1
        else:
            break
    return count


def budgeted_plan_route(step_costs: list[float], total_budget: float, reserve_budget: float = 0.0) -> str:
    executable = max_executable_steps(step_costs, total_budget=total_budget, reserve_budget=reserve_budget)
    if executable == len(step_costs):
        return "execute-all"
    if executable == 0:
        return "review"
    return "trim-plan"
