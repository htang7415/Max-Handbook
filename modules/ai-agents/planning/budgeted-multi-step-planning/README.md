# Budgeted Multi-Step Planning

> Track: `ai-agents` | Topic: `planning`

## Concept

Budgeted multi-step planning decides how much budget each step can use, how many steps fit under the remaining budget, and whether the plan should execute fully, trim itself, or review.

## Key Points

- Multi-step plans should consume an explicit budget, not an implicit hope.
- Reserve budget before dividing the remainder across steps.
- If only part of the plan fits, trimming is safer than silently overspending.

## Minimal Code Mental Model

```python
step_budget = per_step_budget(total_budget=4.0, step_count=3, reserve_budget=0.5)
count = max_executable_steps([1.0, 1.5, 1.0], total_budget=4.0, reserve_budget=0.5)
route = budgeted_plan_route([1.0, 1.5, 1.0], total_budget=4.0, reserve_budget=0.5)
```

## Function

```python
def per_step_budget(total_budget: float, step_count: int, reserve_budget: float = 0.0) -> float:
def max_executable_steps(step_costs: list[float], total_budget: float, reserve_budget: float = 0.0) -> int:
def budgeted_plan_route(step_costs: list[float], total_budget: float, reserve_budget: float = 0.0) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/planning/budgeted-multi-step-planning/python -q
```
