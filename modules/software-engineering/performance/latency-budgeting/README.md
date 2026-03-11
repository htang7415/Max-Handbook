# Latency Budgeting

> Track: `software-engineering` | Topic: `performance`

## Concept

A latency budget assigns a total response-time target and then forces each step in the request path to earn its share of that target.

## Key Points

- Total latency is the sum of boundary costs, not just one slow line of code.
- Remaining budget helps decide which step can still fit inside the target.
- The largest contributor is usually the first thing to investigate.

## Minimal Code Mental Model

```python
remaining = remaining_latency_budget_ms(total_budget_ms=300, observed_steps_ms=[40, 80, 60])
exceeded = latency_budget_exceeded(total_budget_ms=300, observed_steps_ms=[40, 80, 60, 150])
bottleneck = largest_latency_contributor({"api": 40, "db": 120, "cache": 20})
```

## Function

```python
def remaining_latency_budget_ms(total_budget_ms: int, observed_steps_ms: list[int]) -> int:
def latency_budget_exceeded(total_budget_ms: int, observed_steps_ms: list[int]) -> bool:
def largest_latency_contributor(step_latencies_ms: dict[str, int]) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/performance/latency-budgeting/python -q
```
