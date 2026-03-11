# Workflow Concurrency Basics

> Track: `ai-agents` | Topic: `workflows`

## Concept

Workflow concurrency basics model which steps can run in parallel and when their results should join back into one path.

## Key Points

- Concurrency only helps when branches are independent.
- Join points should make it explicit how many branches must finish.
- A simple ready / waiting check is enough for a first workflow.

## Minimal Code Mental Model

```python
ready = runnable_branches(branch_states)
joined = join_ready(branch_states, required=2)
state = join_state(branch_states, required=2)
```

## Function

```python
def runnable_branches(branch_states: dict[str, str]) -> list[str]:
def join_ready(branch_states: dict[str, str], required: int) -> bool:
def join_state(branch_states: dict[str, str], required: int) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/workflow-concurrency-basics/python -q
```
