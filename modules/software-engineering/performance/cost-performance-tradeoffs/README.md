# Cost-Performance Tradeoffs

> Track: `software-engineering` | Topic: `performance`

## Concept

Performance changes should be judged against their cost, because lower latency is only one part of the engineering decision.

## Use When

| Decision | Compare |
| --- | --- |
| Faster instance type | Latency gained vs cost per 1k requests |
| More replicas | Tail latency reduction vs steady spend |
| Optimization project | User value vs engineering time |

## First Principles

- Faster is not automatically better if the cost increase is too large.
- Compare improvements in units the team can reason about, like milliseconds saved and cost per 1k requests.
- Small latency wins on low-value paths often do not justify large infrastructure spend.

## Workflow

1. Measure baseline latency and baseline cost.
2. Estimate the candidate latency and extra cost.
3. Normalize cost to a request or customer unit.
4. Approve the trade-off only when the gain matters for the product path.

## Minimal Code Mental Model

```python
cost = cost_per_1k_requests(hourly_cost=12.0, requests_per_hour=60000)
gain = latency_improvement_ms(baseline_ms=300, candidate_ms=220)
worth_it = worthwhile_tradeoff(gain, extra_cost_per_1k=0.02, max_extra_cost_per_1k=0.03)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Optimizing average latency only | Expensive change may not improve user pain |
| No cost unit | Teams cannot compare alternatives |
| Improving low-value paths first | Spend rises without meaningful product impact |

## Function

```python
def cost_per_1k_requests(hourly_cost: float, requests_per_hour: int) -> float:
def latency_improvement_ms(baseline_ms: int, candidate_ms: int) -> int:
def worthwhile_tradeoff(
    latency_gain_ms: int,
    extra_cost_per_1k: float,
    max_extra_cost_per_1k: float,
) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/performance/cost-performance-tradeoffs/python -q
```
