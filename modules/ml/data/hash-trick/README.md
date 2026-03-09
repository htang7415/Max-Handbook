# Hash Trick

> Track: `ml` | Topic: `data`

## Concept

The hash trick maps tokens or categorical values into a fixed number of buckets without storing a vocabulary table.

## Math

$$
\mathrm{bucket}(x) = h(x) \bmod B
$$

- $h(x)$ -- hash of token or category $x$
- $B$ -- number of buckets

## Key Points

- The hash trick keeps feature dimension fixed even when vocabulary grows.
- Collisions are expected, so it trades memory for occasional ambiguity.
- This is useful for sparse text or very high-cardinality categorical features.

## Function

```python
def hashed_feature_counts(tokens: list[str], num_buckets: int) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/data/hash-trick/python -q
```
