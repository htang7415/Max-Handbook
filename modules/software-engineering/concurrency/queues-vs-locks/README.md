# Queues Vs Locks

> Track: `software-engineering` | Topic: `concurrency`

## Concept

Locks coordinate immediate access to shared state, while queues turn contested work into ordered units that can be processed later.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Lock | Work must finish now inside one critical section | Work can be delayed and serialized |
| Queue | Work can be processed later by workers | The caller needs immediate state mutation |
| Single-owner worker | A resource needs serialized ownership | Multiple workers can safely coordinate with locks |

## First Principles

- Locks are useful when the caller must finish the critical section now.
- Queues are useful when work can be delayed and serialized.
- High contention and long critical sections make lock-based designs more fragile.

## Workflow

1. Decide whether the work touches shared state.
2. Decide whether the caller can wait for delayed processing.
3. Choose a queue when delayed serialization is acceptable.
4. Choose a lock when immediate critical-section completion is required.
5. Watch contention and backlog as separate risk signals.

## Minimal Code Mental Model

```python
pattern = coordination_pattern(shared_resource=True, can_delay_work=True, needs_single_owner=False)
risk = lock_contention_risk(concurrent_workers=6, critical_section_ms=80)
warning = queue_backlog_warning(queue_depth=200, workers=10)
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Lock under high contention | Workers wait and tail latency rises | `lock_contention_risk` flags worker and critical-section pressure |
| Queue without enough workers | Backlog grows faster than processing | `queue_backlog_warning` compares depth to worker count |
| Wrong coordination primitive | Design adds latency or race risk | `coordination_pattern` chooses from shared state and delay tolerance |

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
