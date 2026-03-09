# Self-Attention

> Track: `ml` | Topic: `llm`

## Concept

Self-attention lets each token build a weighted combination of all token values.
Queries ask what a token is looking for, keys describe what each token offers,
and values carry the information that gets mixed together.

## Math

$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$$

- $d_k$ -- key dimension
- $Q$ -- query matrix
- $K$ -- key matrix
- $V$ -- value matrix
- $\mathrm{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)$ -- attention weights over tokens

## Key Points

- Dot products between queries and keys produce similarity scores.
- Softmax turns those scores into normalized weights.
- The output is a weighted sum of the value vectors.

## Function

```python
def self_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]]) -> list[list[float]]:
```

## Run tests

```bash
pytest modules/ml/llm/self-attention/python -q
```
