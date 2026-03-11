# Planning Stop Conditions

> Track: `ai-agents` | Topic: `planning`

## Concept

Planning stop conditions define when a workflow should finish, pause, or escalate instead of continuing to generate more steps.

## Key Points

- A plan should stop when the goal is satisfied or the remaining work is blocked.
- Explicit stop rules reduce wasted looping.
- Stop conditions are often simpler than the planning logic itself.

## Minimal Code Mental Model

```python
done = all_steps_done(plan)
blocked = stop_due_to_blockers(blockers)
decision = stop_decision(plan, blockers, needs_review=False)
```

## Function

```python
def all_steps_done(plan: list[dict[str, object]]) -> bool:
def stop_due_to_blockers(blockers: list[str]) -> bool:
def stop_decision(plan: list[dict[str, object]], blockers: list[str], needs_review: bool) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/planning/planning-stop-conditions/python -q
```
