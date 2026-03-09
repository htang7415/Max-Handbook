# Wilson Interval

> Track: `ml` | Topic: `evaluation`

## Concept

The Wilson interval gives a more stable confidence interval for a Bernoulli rate than the naive normal approximation, especially with small samples or extreme proportions.

## Math

$$
\hat{p}_W = \frac{\hat{p} + z^2/(2n)}{1 + z^2/n}
$$

$$
\mathrm{margin} = \frac{z}{1 + z^2/n} \sqrt{\frac{\hat{p}(1-\hat{p}) + z^2/(4n)}{n}}
$$

- $\hat{p}$ -- observed success rate
- $n$ -- number of trials
- $z$ -- normal critical value

## Key Points

- Wilson intervals stay better behaved when `n` is small.
- The interval remains within `[0, 1]`.
- This is a common default for binary-rate uncertainty.

## Function

```python
def wilson_interval(successes: int, trials: int, z: float = 1.96) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/evaluation/wilson-interval/python -q
```
