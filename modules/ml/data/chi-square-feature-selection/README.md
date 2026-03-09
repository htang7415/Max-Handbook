# Chi-Square Feature Selection

> Track: `ml` | Topic: `data`

## Concept

Chi-square feature selection scores how strongly a categorical or count-like feature is associated with a class label.

## Math

$$
\chi^2 = \sum_{cells} \frac{(O - E)^2}{E}
$$

- $O$ -- observed count in a contingency-table cell
- $E$ -- expected count under independence

## Key Points

- Higher chi-square scores indicate stronger dependence between feature and label.
- This is common for sparse text features and one-hot encoded categories.
- The module scores one binary feature against one binary label.

## Function

```python
def chi_square_feature_score(
    present_positive: int,
    present_negative: int,
    absent_positive: int,
    absent_negative: int,
) -> float:
```

## Run tests

```bash
pytest modules/ml/data/chi-square-feature-selection/python -q
```
