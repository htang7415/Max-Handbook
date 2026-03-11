# Regression Checks

> Track: `ai-agents` | Topic: `evaluation`

## Concept

Regression checks compare a new variant against a baseline and flag when a key metric drops below an allowed threshold.

## Key Points

- Regression checks protect against silent quality drops.
- The threshold should be explicit and small enough to audit.
- A few key metrics are better than a large unstable checklist.

## Minimal Code Mental Model

```python
drop = metric_drop(0.84, 0.79)
failed = regression_failed(0.84, 0.79, max_drop=0.03)
report = regression_report("success", 0.84, 0.79, max_drop=0.03)
```

## Function

```python
def metric_drop(baseline: float, candidate: float) -> float:
def regression_failed(baseline: float, candidate: float, max_drop: float) -> bool:
def regression_report(metric_name: str, baseline: float, candidate: float, max_drop: float) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ai-agents/evaluation/regression-checks/python -q
```
