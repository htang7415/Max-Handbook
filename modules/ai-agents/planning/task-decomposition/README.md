# Task Decomposition

> Track: `ai-agents` | Topic: `planning`

## Concept

Task decomposition turns one broad goal into smaller checkpoints that are easier to inspect and execute.

## Key Points

- Decomposition is useful when a goal is too vague to execute directly.
- Good checkpoints are concrete and ordered.
- A short list of checkpoints is better than a long speculative plan.

## Minimal Code Mental Model

```python
parts = decompose_goal("Prepare launch report", ["collect", "write", "send"])
checkpoints = numbered_checkpoints(parts)
ready = decomposition_is_actionable(checkpoints, min_count=2)
```

## Function

```python
def decompose_goal(goal: str, verbs: list[str]) -> list[str]:
def numbered_checkpoints(items: list[str]) -> list[dict[str, object]]:
def decomposition_is_actionable(items: list[dict[str, object]], min_count: int) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/planning/task-decomposition/python -q
```
