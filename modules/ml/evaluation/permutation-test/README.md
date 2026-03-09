# Permutation Test for Mean Difference

> Track: `ml` | Topic: `evaluation`

## Concept

A permutation test checks whether an observed group difference could plausibly arise by random reassignment of labels under the null hypothesis.

## Math

$$p = \frac{1}{|\Pi|} \sum_{\pi \in \Pi} \mathbb{I}\!\left[|T(\pi)| \ge |T_{\mathrm{obs}}|\right]$$

- $\Pi$ -- set of all label permutations
- $T(\pi)$ -- test statistic under permutation $\pi$
- $T_{\mathrm{obs}}$ -- observed test statistic
- $p$ -- permutation-test p-value

## Key Points

- Permutation tests are non-parametric and make few distributional assumptions.
- The null hypothesis is exchangeability between groups.
- This module computes the exact two-sided p-value for small samples.

## Function

```python
def permutation_test_p_value(group_a: list[float], group_b: list[float]) -> float:
```

## Run tests

```bash
pytest modules/ml/evaluation/permutation-test/python -q
```
