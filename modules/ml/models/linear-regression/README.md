# Linear Regression

> Track: `ml` | Topic: `models`

## Concept

Linear regression models a target as an affine function of the input features.
Each feature contributes through a weight, and the bias shifts the prediction up
or down uniformly.

## Math
$$y = w^\top x + b$$

- $x$ -- input feature vector
- $w$ -- weight vector
- $b$ -- bias term
- $y$ -- predicted output

## Key Points

- The dot product combines features with learned coefficients.
- Positive weights increase the prediction when their feature grows; negative weights decrease it.
- Linear regression is often the first baseline for numerical prediction tasks.

## Function

```python
def predict(x: list[float], w: list[float], b: float) -> float:
```

## Run tests

```bash
pytest modules/ml/models/linear-regression/python -q
```
