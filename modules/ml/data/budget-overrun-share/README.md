# Budget Overrun Share

> Track: `ml` | Topic: `data`

## Concept

Budget overrun share measures what fraction of total original length is lost beyond a hard length budget.

## Math

$$
\mathrm{OverrunShare} = \frac{\sum_{i=1}^{N} \max(0, l_i - L)}{\sum_{i=1}^{N} l_i}
$$

- $l_i$ -- original length for example $i$
- $L$ -- maximum allowed length

## Key Points

- This metric complements overflow count by normalizing lost budget.
- It is useful when comparing datasets with different absolute lengths.
- This module returns a value in $[0, 1]$ when total length is nonzero.

## Function

```python
def budget_overrun_share(lengths: list[int], max_length: int) -> float:
```

## Run tests

```bash
pytest modules/ml/data/budget-overrun-share/python -q
```
