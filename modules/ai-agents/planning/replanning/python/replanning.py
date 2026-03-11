from __future__ import annotations


def replan_needed(goal_changed: bool, blocked_step: bool, new_constraints: list[str]) -> bool:
    return goal_changed or blocked_step or any(item.strip() for item in new_constraints)


def remaining_steps(plan: list[dict[str, object]]) -> list[str]:
    steps: list[str] = []
    for item in plan:
        text = str(item.get("text", "")).strip()
        done = bool(item.get("done", False))
        if text and not done:
            steps.append(text)
    return steps


def replan_summary(steps: list[str], constraints: list[str]) -> str:
    cleaned_steps = [step.strip() for step in steps if step.strip()]
    cleaned_constraints = [constraint.strip() for constraint in constraints if constraint.strip()]
    step_part = "Remaining: " + ", ".join(cleaned_steps) if cleaned_steps else "Remaining: none"
    if not cleaned_constraints:
        return step_part
    return step_part + " | Constraints: " + ", ".join(cleaned_constraints)
