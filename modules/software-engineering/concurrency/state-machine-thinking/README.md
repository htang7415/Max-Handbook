# State-Machine Thinking

> Track: `software-engineering` | Topic: `concurrency`

## Concept

State-machine thinking turns workflow correctness into explicit states and allowed transitions instead of hidden condition chains.

## Key Points

- Long-running concurrent workflows are easier to reason about as states plus events.
- Invalid transitions should fail early.
- Terminal states should be explicit so retries and cleanup know when to stop.

## Minimal Code Mental Model

```python
allowed = valid_transition("pending", "start", transitions)
next_state = apply_transition("pending", "start", transitions)
terminal = is_terminal_state("completed", {"completed", "failed"})
```

## Function

```python
def valid_transition(
    current_state: str,
    event: str,
    transition_map: dict[tuple[str, str], str],
) -> bool:
def apply_transition(
    current_state: str,
    event: str,
    transition_map: dict[tuple[str, str], str],
) -> str:
def is_terminal_state(state: str, terminal_states: set[str]) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/concurrency/state-machine-thinking/python -q
```
