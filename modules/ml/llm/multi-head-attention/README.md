# Multi-Head Attention (Minimal)

> Track: `ml` | Topic: `llm`

## Concept

Multi-head attention splits the model dimension into smaller subspaces, runs
attention independently in each head, and concatenates the head outputs. This
lets the model attend to different patterns in parallel.

## Math
$$\mathrm{head}_i = \mathrm{Attention}(Q_i, K_i, V_i),\quad \mathrm{MHA}(Q,K,V) = \mathrm{Concat}(\mathrm{head}_1, \dots, \mathrm{head}_h)$$

- $h$ -- number of heads
- $Q_i$ -- i-th query matrix
- $K_i$ -- i-th key matrix
- $V_i$ -- i-th value matrix
- $i$ -- index
- $Q$ -- query matrix
- $K$ -- key matrix
- $V$ -- value matrix

## Key Points

- Each head sees only a slice of the model dimension.
- Concatenation merges those per-head outputs back into one representation.
- This minimal lab omits learned Q/K/V and output projection matrices to stay small.

## Function

```python
def multi_head_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]], heads: int) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/multi-head-attention/python -q
```
