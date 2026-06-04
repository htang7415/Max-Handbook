# State Machine Basics

> Track: `software-engineering` | Topic: `design-patterns`

## Concept

Explicit state machines make workflow rules visible, so invalid transitions are rejected instead of being implied by scattered conditionals.

## Use When

| Situation | State Machine Value |
| --- | --- |
| Workflow has allowed and forbidden transitions | Centralize transition rules |
| Retries or rollbacks depend on current state | Make terminal states explicit |
| Conditionals are scattered across services | Move rules into one transition table |

## First Principles

- State is easiest to reason about when allowed transitions are declared in one place.
- Workflow correctness matters more than elegance for long-lived business processes.
- Terminal states should be explicit so retries and rollbacks behave predictably.

## Workflow

1. Name every state in the workflow.
2. List allowed transitions in one place.
3. Reject invalid transitions by default.
4. Mark terminal states so retry behavior is predictable.

## Minimal Code Mental Model

```python
assert can_transition("draft", "approved") is True
assert apply_transition("approved", "fulfilling") == "fulfilling"
assert terminal_state("shipped") is True
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Implicit transitions in conditionals | Invalid states slip through |
| Missing terminal states | Retries can reopen completed work |
| Transition rules split across files | Reviewers cannot see workflow correctness |

## Function

```python
def can_transition(current: str, nxt: str) -> bool:
def apply_transition(current: str, nxt: str) -> str:
def terminal_state(state: str) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/design-patterns/state-machine-basics/python -q
```
