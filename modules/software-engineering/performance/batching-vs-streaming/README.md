# Batching Vs Streaming

> Track: `software-engineering` | Topic: `performance`

## Concept

Batching amortizes overhead across many items, while streaming delivers early partial results at the cost of more per-item overhead.

## Use When

| Goal | Prefer |
| --- | --- |
| Maximize throughput | Batching |
| Show partial output quickly | Streaming |
| Reduce per-item overhead | Larger batches |
| Reduce perceived wait | Earlier streamed chunks |

## First Principles

- Batching is useful when throughput matters more than time to first result.
- Streaming is useful when users benefit from partial output quickly.
- The right choice depends on whether amortization or responsiveness is the bottleneck.

## Workflow

1. Measure time to first result and full completion time.
2. Identify fixed overhead per request or item.
3. Choose batching when amortized cost dominates.
4. Choose streaming when early feedback changes user experience.

## Minimal Code Mental Model

```python
mode = preferred_delivery_mode(needs_early_results=True, amortization_priority=False)
cost = batch_cost_per_item(total_batch_ms=120, batch_size=6)
worth_it = streaming_worth_it(time_to_first_result_ms=100, full_completion_ms=900)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Batch size too large | Slow first response and higher memory pressure |
| Streaming tiny chunks | Excess overhead and noisy clients |
| Optimizing throughput only | Interactive workflows feel slow |

## Function

```python
def preferred_delivery_mode(needs_early_results: bool, amortization_priority: bool) -> str:
def batch_cost_per_item(total_batch_ms: int, batch_size: int) -> float:
def streaming_worth_it(time_to_first_result_ms: int, full_completion_ms: int) -> bool:
```

## Run tests

```bash
pytest modules/software-engineering/performance/batching-vs-streaming/python -q
```
