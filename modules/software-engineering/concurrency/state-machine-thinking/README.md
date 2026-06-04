# State-Machine Thinking

> Track: `software-engineering` | Topic: `concurrency`

## Concept

State-machine thinking turns workflow correctness into explicit states and allowed transitions instead of hidden condition chains.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Long-running workflow | Work can be pending, running, completed, failed, or cancelled | The operation is one immediate pure function |
| Retry or cleanup logic | Some states should stop future work | There are no terminal states |
| Concurrent event handling | Events can arrive out of order | State transitions do not matter |

## First Principles

- Long-running concurrent workflows are easier to reason about as states plus events.
- Invalid transitions should fail early.
- Terminal states should be explicit so retries and cleanup know when to stop.

## Workflow

1. List valid states and terminal states.
2. Define allowed `(state, event) -> next_state` transitions.
3. Check transitions before applying them.
4. Reject invalid events early.
5. Stop retries and cleanup once the workflow reaches a terminal state.

## Minimal Code Mental Model

```python
allowed = valid_transition("pending", "start", transitions)
next_state = apply_transition("pending", "start", transitions)
terminal = is_terminal_state("completed", {"completed", "failed"})
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Hidden transition | Workflow reaches impossible state | `valid_transition` checks the transition map |
| Invalid event accepted | Retry or cleanup runs from the wrong state | `apply_transition` rejects invalid transitions |
| Terminal state not explicit | Completed work keeps retrying | `is_terminal_state` makes stop states inspectable |

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
