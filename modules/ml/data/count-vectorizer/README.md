# Count Vectorizer

> Track: `ml` | Topic: `data`

## Concept

A count vectorizer converts tokens into a fixed vocabulary count vector.

## Math

$$
\mathbf{x}_j = \sum_{i=1}^{n} \mathbf{1}[t_i = v_j]
$$

- $t_i$ -- observed token
- $v_j$ -- vocabulary term at position $j$
- $\mathbf{x}_j$ -- count for vocabulary term $j$

## Key Points

- Count vectors are a simple lexical baseline before TF-IDF weighting.
- The feature dimension is fixed by the chosen vocabulary.
- Tokens outside the vocabulary are ignored in this minimal version.

## Function

```python
def count_vector(tokens: list[str], vocabulary: list[str]) -> list[int]:
```

## Run tests

```bash
pytest modules/ml/data/count-vectorizer/python -q
```
