# Queues Vs Locks

> Track: `software-engineering` | Topic: `concurrency`

## Concept

Locks coordinate immediate access to shared state, while queues turn contested work into ordered units that can be processed later.

## Key Points

- Locks are useful when the caller must finish the critical section now.
- Queues are useful when work can be delayed and serialized.
- High contention and long critical sections make lock-based designs more fragile.

## Minimal Code Mental Model

```python
pattern = coordination_pattern(shared_resource=True, can_delay_work=True, needs_single_owner=False)
risk = lock_contention_risk(concurrent_workers=6, critical_section_ms=80)
warning = queue_backlog_warning(queue_depth=200, workers=10)
```

## Function

```python
def coordination_pattern(shared_resource: bool, can_delay_work: bool, needs_single_owner: bool) -> str:
def lock_contention_risk(concurrent_workers: int, critical_section_ms: int) -> str:
def queue_backlog_warning(queue_depth: int, workers: int) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/concurrency/queues-vs-locks/python -q
```
