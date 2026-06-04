# Consistency Tradeoffs

> Track: `software-engineering` | Topic: `system-design`

## Concept

Consistency choices decide whether a system optimizes for immediate correctness across replicas and components or accepts temporary divergence for availability and latency.

## Use When

| Requirement | Consistency Bias |
| --- | --- |
| Cross-entity invariant must always hold | Strong consistency |
| Stale reads are acceptable | Eventual consistency |
| Many concurrent writers | Stronger conflict control |
| Low-latency global reads | Eventual or cached reads |

## First Principles

- Strong consistency is most valuable when cross-entity invariants matter.
- Eventual consistency is easier to scale when stale reads are acceptable.
- Write conflicts and stale-read tolerance are the main design signals.

## Workflow

1. Name the invariant that must or may temporarily break.
2. Decide who can read stale data and for how long.
3. Estimate concurrent writers and conflict cost.
4. Pick the weakest consistency model that preserves correctness.

## Minimal Code Mental Model

```python
mode = consistency_mode(cross_entity_invariant=True, stale_reads_tolerable=False)
risk = read_write_conflict_risk(concurrent_writers=4, stale_reads_tolerable=False)
decision = consistency_decision(cross_entity_invariant=False, stale_reads_tolerable=True, concurrent_writers=1)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Treating all data as equally strict | System becomes slower or harder to scale than needed |
| Ignoring conflicts | Last-write-wins can corrupt user intent |
| Hiding stale reads | Users see confusing or unsafe state |

## Function

```python
def consistency_mode(cross_entity_invariant: bool, stale_reads_tolerable: bool) -> str:
def read_write_conflict_risk(concurrent_writers: int, stale_reads_tolerable: bool) -> str:
def consistency_decision(
    cross_entity_invariant: bool,
    stale_reads_tolerable: bool,
    concurrent_writers: int,
) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/system-design/consistency-tradeoffs/python -q
```
