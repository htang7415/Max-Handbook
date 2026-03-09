# Why BatchNorm is Bad for Transformers

> Track: `ml` | Topic: `deep-learning`

## Concept

BatchNorm normalizes activations using statistics shared across the batch. In
transformers, this is usually a bad fit because sequence positions and
variable-length examples make those shared statistics unstable and order-dependent.

## Math

$$\mu_B = \frac{1}{BT}\sum_{b=1}^{B}\sum_{t=1}^{T} x_{b,t}$$

- $\mu_B$ -- batch mean used for normalization
- $x_{b,t}$ -- activation at batch element $b$ and timestep $t$
- $B$ -- batch size
- $T$ -- number of sequence positions
- $b$ -- batch index
- $t$ -- timestep index

## Key Points

- BatchNorm mixes information across examples, while transformers usually normalize within each token representation.
- Sequence length changes can change the normalization statistics.
- LayerNorm and RMSNorm are preferred because they avoid cross-example coupling.

## Function

```python
def batch_stats(matrix: list[list[float]]) -> tuple[float, float]:
```

## Run tests

```bash
pytest modules/ml/deep-learning/batchnorm-transformers/python -q
```
