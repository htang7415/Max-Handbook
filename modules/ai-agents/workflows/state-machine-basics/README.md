# State Machine Basics

> Track: `ai-agents` | Topic: `workflows`

## Concept

State machine basics model a workflow as a small set of states and explicit transitions between them.

## Key Points

- State machines are useful when the workflow has a few stable stages.
- Explicit transitions make debugging easier than hidden status flags.
- Invalid transitions should fail early.

## Minimal Code Mental Model

```python
state = next_state("planned", "start")
allowed = valid_transition("running", "complete", transitions)
trace = transition_trace(["planned", "running", "done"])
```

## Function

```python
def valid_transition(current_state: str, next_state_name: str, transitions: dict[str, list[str]]) -> bool:
def next_state(current_state: str, event: str) -> str:
def transition_trace(states: list[str]) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/workflows/state-machine-basics/python -q
```
