# Latency Budgeting

> Track: `software-engineering` | Topic: `performance`

## Concept

A latency budget assigns a total response-time target and then forces each step in the request path to earn its share of that target.

## Use When

| Situation | Use this when | Avoid when |
| --- | --- | --- |
| Request path review | Several steps contribute to response time | There is no user-facing latency target |
| Bottleneck triage | You need to choose which step to investigate first | Measurements are not available |
| Regression gate | A change may consume too much headroom | Latency is irrelevant to the feature |

## First Principles

- Total latency is the sum of boundary costs, not just one slow line of code.
- Remaining budget helps decide which step can still fit inside the target.
- The largest contributor is usually the first thing to investigate.

## Workflow

1. Set a total latency budget in milliseconds.
2. Measure each observed step.
3. Compute remaining headroom.
4. Flag paths that exceed the total budget.
5. Investigate the largest contributor first.

## Minimal Code Mental Model

```python
remaining = remaining_latency_budget_ms(total_budget_ms=300, observed_steps_ms=[40, 80, 60])
exceeded = latency_budget_exceeded(total_budget_ms=300, observed_steps_ms=[40, 80, 60, 150])
bottleneck = largest_latency_contributor({"api": 40, "db": 120, "cache": 20})
```

## Failure Modes

| Failure | Symptom | Guard or test |
| --- | --- | --- |
| Negative latency input | Budget math becomes meaningless | Functions reject negative values |
| Empty contributor list | There is no bottleneck to rank | `largest_latency_contributor` rejects empty input |
| Optimizing the wrong step | Work does not improve user latency | Bottleneck helper picks the largest measured contributor |

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
