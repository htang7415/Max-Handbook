# Admission Control

> Track: `ml` | Topic: `mlops`

## Concept

Admission control sheds load before queues grow without bound by admitting only the work that fits within a configured outstanding-request budget.

## Math

$$
\mathrm{available} = \max(0, M - O)
$$

$$
\mathrm{admitted} = \min(I, \mathrm{available}), \quad \mathrm{rejected} = I - \mathrm{admitted}
$$

- $M$ -- maximum allowed outstanding requests
- $O$ -- current outstanding requests
- $I$ -- newly arriving requests

## Key Points

- Admission control is an early load-shedding primitive.
- It is simpler than queue scheduling because it only decides accept vs reject.
- This module models request admission from a fixed outstanding-capacity budget.

## Function

```python
def admit_requests(
    current_outstanding: int,
    incoming_requests: int,
    max_outstanding: int,
) -> tuple[int, int]:
```

## Run tests

```bash
pytest modules/ml/mlops/admission-control/python -q
```
