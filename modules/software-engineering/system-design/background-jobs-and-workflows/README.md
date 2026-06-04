# Background Jobs And Workflows

> Track: `software-engineering` | Topic: `system-design`

## Concept

Work should leave the request path when it is slow, retry-prone, or composed of multiple durable steps.

## Use When

| Situation | Design Choice |
| --- | --- |
| Work is slow but not needed for the response | Background job |
| Work has retries, compensation, or multiple steps | Durable workflow |
| Work has a user-visible deadline | Queue priority and timeout policy |

## First Principles

- Background jobs reduce request latency by moving non-immediate work out of band.
- Multi-step business processes usually need workflow state, not just one queued function.
- User-visible deadlines still matter even when work is asynchronous.

## Workflow

1. Separate response-critical work from follow-up work.
2. Decide whether one task is enough or workflow state is needed.
3. Add retry, timeout, and idempotency rules.
4. Prioritize jobs by user impact and deadline.

## Minimal Code Mental Model

```python
background = should_background_job(user_waiting=True, duration_ms=1500, retries_expected=True)
kind = workflow_kind(needs_human_approval=False, has_multiple_steps=True)
priority = queue_priority(user_visible=True, deadline_ms=2000)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Queueing required response work | User sees missing or inconsistent state |
| No durable workflow state | Multi-step process loses progress |
| No priority policy | Urgent work waits behind bulk jobs |

## Function

```python
def should_background_job(user_waiting: bool, duration_ms: int, retries_expected: bool) -> bool:
def workflow_kind(needs_human_approval: bool, has_multiple_steps: bool) -> str:
def queue_priority(user_visible: bool, deadline_ms: int | None) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/background-jobs-and-workflows/python -q
```
