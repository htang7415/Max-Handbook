# Dropout

> Track: `ml` | Topic: `deep-learning`

## Concept

Dropout randomly removes some activations during training so the network cannot
rely too heavily on any single pathway. This encourages more distributed and
robust internal representations.

## Math
$$x' = \frac{m \odot x}{1-p},\quad m \sim \mathrm{Bernoulli}(1-p)$$

- $x$ -- input activation vector
- $m$ -- binary dropout mask
- $p$ -- drop probability
- $x'$ -- scaled output after dropout

## Key Points

- Kept activations are scaled by $\frac{1}{1-p}$ so their expected magnitude stays similar.
- Dropout is used during training, not deterministic inference.
- Larger `p` means stronger regularization but also more information removal.

## Function

```python
def dropout(x: list[float], p: float, seed: int = 0) -> list[float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/dropout/python -q
```
