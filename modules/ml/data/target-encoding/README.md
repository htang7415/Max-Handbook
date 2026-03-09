# Target Encoding

> Track: `ml` | Topic: `data`

## Concept

Target encoding replaces each category with the average target value observed for that category.

## Math

$$
\mathrm{enc}(c) = \frac{1}{N_c} \sum_{i: x_i = c} y_i
$$

- $c$ -- category
- $N_c$ -- number of training examples with category $c$
- $y_i$ -- target value for example $i$

## Key Points

- Target encoding is useful for high-cardinality categorical features.
- It can leak label information if computed outside the training fold.
- This module computes the simple per-category mean mapping.

## Function

```python
def target_encoding_map(categories: list[str], targets: list[float]) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/data/target-encoding/python -q
```
