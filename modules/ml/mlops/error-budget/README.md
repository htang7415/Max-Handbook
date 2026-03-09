# Error Budget

> Track: `ml` | Topic: `mlops`

## Concept

An error budget is the fraction of requests that may fail while still meeting an SLO target.

## Math

$$
\mathrm{allowed\_error\_rate} = 1 - \mathrm{SLO}
$$

$$
\mathrm{burn\_rate} = \frac{\mathrm{observed\_error\_rate}}{\mathrm{allowed\_error\_rate}}
$$

- $\mathrm{SLO}$ -- target success rate
- $\mathrm{observed\_error\_rate}$ -- failures divided by total requests
- $\mathrm{burn\_rate}$ -- how fast the service is consuming its budget

## Key Points

- Error budgets connect reliability targets to rollout decisions.
- A burn rate above `1.0` means the service is consuming budget too quickly.
- This module returns both remaining budget fraction and burn rate.

## Function

```python
def error_budget_status(total_requests: int, failed_requests: int, slo_target: float) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/mlops/error-budget/python -q
```
