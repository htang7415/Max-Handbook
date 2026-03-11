# Step-Level Evaluation

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Step-level evaluation measures whether the individual steps inside a run completed, stalled, or failed, instead of only scoring the final outcome.

## Key Points

- Whole-run success can hide where the breakdown actually happened.
- Step completion is useful for planning-heavy agents.
- Blocked or failed steps should be counted separately from completed ones.

## Minimal Code Mental Model

```python
rates = step_completion_rate(["done", "done", "blocked"])
blocked = blocked_step_rate(["done", "done", "blocked"])
counts = step_status_counts(["done", "failed", "blocked", "done"])
```

## Function

```python
def step_completion_rate(statuses: list[str]) -> float:
def blocked_step_rate(statuses: list[str]) -> float:
def step_status_counts(statuses: list[str]) -> dict[str, int]:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/step-level-evaluation/python -q
```
