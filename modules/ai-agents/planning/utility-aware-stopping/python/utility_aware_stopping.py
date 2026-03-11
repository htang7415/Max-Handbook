from __future__ import annotations


def expected_step_utility(
    success_probability: float,
    success_value: float,
    step_cost: float,
    risk_penalty: float = 0.0,
) -> float:
    if not 0.0 <= success_probability <= 1.0:
        raise ValueError("success_probability must satisfy 0 <= value <= 1")
    if success_value < 0.0:
        raise ValueError("success_value must be non-negative")
    if step_cost < 0.0:
        raise ValueError("step_cost must be non-negative")
    if risk_penalty < 0.0:
        raise ValueError("risk_penalty must be non-negative")
    return success_probability * success_value - step_cost - risk_penalty


def plan_utility(step_utilities: list[float]) -> float:
    if not step_utilities:
        raise ValueError("step_utilities must be non-empty")
    return sum(step_utilities)


def utility_stop_route(
    expected_utility: float,
    min_continue_utility: float,
    max_stop_loss: float = 0.0,
) -> str:
    if min_continue_utility < max_stop_loss:
        raise ValueError("min_continue_utility must be greater than or equal to max_stop_loss")
    if expected_utility >= min_continue_utility:
        return "continue"
    if expected_utility <= max_stop_loss:
        return "stop"
    return "review"
