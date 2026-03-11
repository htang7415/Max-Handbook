# Handoffs and Routing

> Track: `ai-agents` | Topic: `workflows`

## Concept

Handoffs and routing decide which worker or step should handle a task, package the required state, and limit unnecessary retries.

## Key Points

- Routing should map task intent to a small number of known destinations.
- Handoffs should contain compact state that the next worker can actually use.
- Retries should be bounded so failed steps do not loop forever.

## Core Math

- Route score:
  $$
  \text{quality estimate} - \text{latency cost} - \text{tool cost}
  $$
- Retry budget:
  $$
  \text{attempt} \le \text{max attempts}
  $$

## Minimal Code Mental Model

```python
route = route_task("summarize docs and open a ticket", routes)
handoff = build_handoff("task_7", route, {"doc_id": "abc"})
retry = should_retry(attempt=1, max_attempts=3, retryable=True)
```

## Function

```python
def route_task(request: str, routes: dict[str, list[str]]) -> str | None:
def build_handoff(task_id: str, target: str, payload: dict[str, object]) -> dict[str, object]:
def should_retry(attempt: int, max_attempts: int, retryable: bool) -> bool:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/handoffs-and-routing/python -q
```
