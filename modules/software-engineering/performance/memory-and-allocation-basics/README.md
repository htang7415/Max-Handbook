# Memory And Allocation Basics

> Track: `software-engineering` | Topic: `performance`

## Concept

Memory pressure comes from how many objects are created, how large they are, and how long they stay alive.

## Use When

| Signal | Look At |
| --- | --- |
| High GC or allocator time | Allocation rate |
| Memory close to limit | Peak live objects |
| Large per-request objects | Object size and retention |
| Repeated short-lived objects | Reuse or pooling only after measurement |

## First Principles

- Frequent allocations increase GC or allocator work.
- Peak memory depends on both object size and retention.
- Pooling or reuse is only worth it when allocation churn is materially high.

## Workflow

1. Measure allocation rate and heap size under representative load.
2. Separate short-lived churn from retained live data.
3. Remove unnecessary object creation before adding pools.
4. Re-check latency and memory after the change.

## Minimal Code Mental Model

```python
bytes_per_request = allocation_bytes(objects_per_request=500, bytes_per_object=256)
pressure = memory_pressure(heap_mb=900, limit_mb=1024)
reuse = reuse_worth_it(objects_per_request=5000, bytes_per_object=512)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Pooling without churn | More complexity with no measurable gain |
| Ignoring retention | Memory limit is still hit after allocation fixes |
| Optimizing tiny objects first | Effort misses the real pressure source |

## Function

```python
def allocation_bytes(objects_per_request: int, bytes_per_object: int) -> int:
def memory_pressure(heap_mb: int, limit_mb: int) -> str:
def reuse_worth_it(objects_per_request: int, bytes_per_object: int) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/performance/memory-and-allocation-basics/python -q
```
