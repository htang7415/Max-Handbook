# Pareto-Front Benchmark Comparisons

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Pareto-front benchmark comparisons keep all non-dominated variants instead of forcing one winner when success, cost, latency, or safety trade off against each other.

## Key Points

- A variant is Pareto-optimal when no other variant is at least as good on every metric and strictly better on one.
- Multi-metric evaluation should not collapse tradeoffs too early.
- The frontier is a compact shortlist for the next round of review or deployment decisions.

## Minimal Code Mental Model

```python
frontier = pareto_front(variants, maximize=["success"], minimize=["cost", "latency"])
route = pareto_route("candidate-b", variants, maximize=["success"], minimize=["cost", "latency"])
```

## Function

```python
def dominates(
    left_metrics: dict[str, float],
    right_metrics: dict[str, float],
    maximize_metrics: list[str],
    minimize_metrics: list[str],
) -> bool:
def pareto_front(
    variants: dict[str, dict[str, float]],
    maximize_metrics: list[str],
    minimize_metrics: list[str],
) -> list[str]:
def pareto_route(
    candidate_name: str,
    variants: dict[str, dict[str, float]],
    maximize_metrics: list[str],
    minimize_metrics: list[str],
) -> str:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/pareto-front-benchmark-comparisons/python -q
```
