# Profiling Python

> Track: `software-engineering` | Topic: `python`

## Concept

Profiling Python usually means separating CPU-heavy work, object churn, and serialization cost before trying to optimize implementation details.

## Use When

| Symptom | First Check |
| --- | --- |
| High CPU | Function-level profile |
| High memory or GC pressure | Allocation and object churn |
| Slow API response | Serialization and dependency time |

## First Principles

- A Python profile is most useful when it identifies the dominant cost class first.
- Serialization and object churn are common hidden costs in Python services.
- The next step after profiling should match the bottleneck, not a generic optimization checklist.

## Workflow

1. Reproduce the slow path with representative input.
2. Separate CPU, allocation, and serialization cost.
3. Pick the hottest function or cost class.
4. Re-profile after one targeted change.

## Minimal Code Mental Model

```python
bottleneck = python_bottleneck(cpu_ms=80, alloc_mb=20, serialization_ms=10)
target = hotspot({"render": 12.0, "serialize": 45.0, "query_db": 20.0})
step = profiling_next_step(bottleneck)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Starting with micro-optimizations | The real bottleneck remains |
| Ignoring serialization | API cost is misclassified as business logic |
| Profiling unrealistic data | Fix does not move production latency |

## Function

```python
def python_bottleneck(cpu_ms: float, alloc_mb: float, serialization_ms: float) -> str:
def hotspot(costs: dict[str, float]) -> str:
def profiling_next_step(bottleneck: str) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/python/profiling-python/python -q
```
