# LLM Eval Serving Gate

> Track: `ml` | Topic: `capstones`

## Concept

An LLM release gate combines quality, calibration, latency, cost, and regression checks before a variant is allowed to ship.

## Key Points

- A higher judge score is not enough if calibration, latency, or cost violates the product budget.
- Release gates should return explicit reasons so failures can be debugged.
- Regression risk should block rollout even when aggregate quality improves.
- This capstone connects LLM evaluation with serving and MLOps release discipline.

## Core Math

- Composite quality:
  $$
  0.5 \cdot \text{task success} + 0.3 \cdot \text{judge win rate} + 0.2 \cdot (1 - \text{calibration error}) - 0.4 \cdot \text{regression rate}
  $$
- Serving fit:
  $$
  \min\left(\frac{\text{latency budget}}{\text{p95 latency}}, \frac{\text{cost budget}}{\text{cost}}\right)
  $$

## Minimal Code Mental Model

```python
quality = composite_quality_score(0.86, 0.62, calibration_error=0.08)
fit = serving_fit(850, 0.42, latency_budget_ms=1000, cost_budget_per_1k=0.50)
decision = release_gate(
    metrics={
        "task_success": 0.86,
        "judge_win_rate": 0.62,
        "calibration_error": 0.08,
        "regression_rate": 0.01,
        "p95_latency_ms": 850,
        "cost_per_1k": 0.42,
    },
    budgets={"min_quality": 0.78, "max_latency_ms": 1000, "max_cost_per_1k": 0.50},
)
```

## Function

```python
def composite_quality_score(
    task_success: float,
    judge_win_rate: float,
    calibration_error: float,
    regression_rate: float = 0.0,
) -> float:
def serving_fit(
    p95_latency_ms: float,
    cost_per_1k: float,
    latency_budget_ms: float,
    cost_budget_per_1k: float,
) -> float:
def release_gate(metrics: dict[str, float], budgets: dict[str, float]) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/ml/capstones/llm-eval-serving-gate/python -q
```
