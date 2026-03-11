# Replanning

> Track: `ai-agents` | Topic: `planning`

## Concept

Replanning updates the remaining work after a goal changes, a step gets blocked, or new constraints arrive.

## Key Points

- A plan should change when the task state changes.
- Replanning should preserve what is already done and only update what remains.
- New constraints should be attached explicitly so the revised plan is easy to inspect.

## Minimal Code Mental Model

```python
need = replan_needed(goal_changed=False, blocked_step=True, new_constraints=["Need manager approval"])
remaining = remaining_steps(plan)
updated = replan_summary(remaining, ["Need manager approval"])
```

## Function

```python
def replan_needed(goal_changed: bool, blocked_step: bool, new_constraints: list[str]) -> bool:
def remaining_steps(plan: list[dict[str, object]]) -> list[str]:
def replan_summary(steps: list[str], constraints: list[str]) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/planning/replanning/python -q
```
