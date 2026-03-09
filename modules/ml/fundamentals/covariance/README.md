# Covariance

> Track: `ml` | Topic: `fundamentals`

## Concept

Covariance measures whether two variables move together. If large values of one
variable tend to occur with large values of the other, covariance is positive;
if one tends to be large when the other is small, covariance is negative.

## Math

$$\mathrm{cov}(X,Y)=\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]$$

- $\mathbb{E}$ -- expectation
- $X, Y$ -- random variables
- $\mu_X$ -- mean of $X$
- $\mu_Y$ -- mean of $Y$
- \mathrm{cov}(X,Y) -- covariance between the variables

## Key Points

- Covariance captures direction of co-movement, not normalized strength.
- Its magnitude depends on scale, which is why correlation is often easier to compare.
- Zero covariance means no linear relationship, not necessarily independence.

## Function

```python
def covariance(x: list[float], y: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/fundamentals/covariance/python -q
```
