# Orchestrator Workers

> Track: `ai-agents` | Topic: `multi-agent`

## Concept

Orchestrator-workers use one coordinator to own the global goal, assign bounded subtasks to workers, and merge structured worker reports back into one plan-level view.

## Key Points

- The orchestrator should keep the global state and give workers only narrow subtasks.
- Worker packets should cap scope so workers do not drift into doing the whole job.
- Worker reports should return status as well as result so the orchestrator can replan or escalate.

## Minimal Code Mental Model

```python
assignments = orchestrator_assignments(
    "audit repo and draft summary",
    {"researcher": "scan repo for risky files", "writer": "draft summary"},
)
packet = worker_task_packet("researcher", "scan repo for risky files", {"repo": "max-handbook"})
summary = orchestrator_summary([{"worker": "researcher", "status": "done", "result": "2 risky files"}])
```

## Function

```python
def orchestrator_assignments(goal: str, role_to_subtask: dict[str, str]) -> list[dict[str, str]]:
def worker_task_packet(
    worker: str,
    subtask: str,
    shared_context: dict[str, object],
    max_steps: int = 1,
) -> dict[str, object]:
def orchestrator_summary(worker_reports: list[dict[str, object]]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/multi-agent/orchestrator-workers/python -q
```
