# Worker Coordination

> Track: `ai-agents` | Topic: `multi-agent`

## Concept

Worker coordination routes a task to the right specialist, packages a small handoff, and merges worker outputs into one coordinator-facing result.

## Key Points

- Workers should have distinct roles.
- Handoffs should carry only the context the worker needs.
- Merge logic should stay simple enough to inspect.

## Minimal Code Mental Model

```python
worker = select_worker("investigate billing issue", worker_keywords)
handoff = worker_handoff(worker, "investigate invoice mismatch", {"invoice_id": "inv_7"})
merged = merge_worker_outputs(outputs)
```

## Function

```python
def select_worker(task: str, worker_keywords: dict[str, list[str]]) -> str | None:
def worker_handoff(worker: str, task: str, context: dict[str, object]) -> dict[str, object]:
def merge_worker_outputs(outputs: list[dict[str, object]]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/multi-agent/worker-coordination/python -q
```
