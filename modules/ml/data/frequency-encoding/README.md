# Frequency Encoding

> Track: `ml` | Topic: `data`

## Concept

Frequency encoding replaces each category with how often it appears in the training data.

## Math

$$
\mathrm{freq}(c) = \frac{N_c}{N}
$$

- $N_c$ -- count of category $c$
- $N$ -- total number of examples

## Key Points

- Frequency encoding is a cheap baseline for high-cardinality categorical features.
- It uses only the feature distribution, not the label.
- It is often safer than target encoding when leakage is a concern.

## Function

```python
def frequency_encoding_map(categories: list[str]) -> dict[str, float]:
```

## Run tests

```bash
pytest modules/ml/data/frequency-encoding/python -q
```
