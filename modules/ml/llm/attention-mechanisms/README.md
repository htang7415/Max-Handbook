# Attention Mechanisms

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to learn the core attention variants together:
self-attention, multi-head attention, causal masking, and sparse local masking.

## First Principles

- Self-attention mixes token values using query-key similarity scores.
- Multi-head attention repeats that mixing in several learned subspaces.
- Causal masking blocks future tokens in autoregressive language modeling.
- Sparse attention reduces cost by only allowing selected token pairs to interact.

## Core Math

Scaled dot-product attention:

$$
\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

Multi-head attention:

$$
\mathrm{MHA}(Q,K,V) = \mathrm{Concat}(\mathrm{head}_1,\dots,\mathrm{head}_h)
$$

Causal masking sets future attention scores to $-\infty$ before softmax.

## Minimal Code Mental Model

```python
attn = self_attention(q, k, v)
mha = multi_head_attention(q, k, v, heads=8)
masked = causal_self_attention(Q, K, V)
mask = window_mask(seq_len=128, window=16)
```

## Function

```python
def self_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]]) -> list[list[float]]:
def multi_head_attention(q: list[list[float]], k: list[list[float]], v: list[list[float]], heads: int) -> list[list[float]]:
def causal_mask(seq_len: int) -> np.ndarray:
def causal_self_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray) -> np.ndarray:
def window_mask(seq_len: int, window: int) -> list[list[int]]:
```

## When To Use What

- Use self-attention first to understand the core weighted-mixing idea.
- Use multi-head attention to see how transformers scale attention capacity.
- Use causal masking for decoder-only LLMs.
- Use sparse local masking when full attention is too expensive.

## Run tests

```bash
pytest modules/ml/llm/attention-mechanisms/python -q
```
