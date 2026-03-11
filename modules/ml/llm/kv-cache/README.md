# KV Cache Size

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to estimate how cached attention keys and values consume memory
during autoregressive decoding.

## First Principles

- During decoding, transformers reuse old key and value tensors instead of recomputing the full prefix every step.
- This speeds up inference, but cache memory grows linearly with context length.
- KV cache size often becomes the real serving bottleneck before compute does.
- Multi-query and grouped-query attention reduce cache size by shrinking the number of KV heads.

## Core Math

$$
\mathrm{bytes} = B \cdot L \cdot T \cdot H_{kv} \cdot D \cdot 2 \cdot s
$$

$$
\mathrm{GiB} = \frac{\mathrm{bytes}}{1024^3}
$$

- $B$ -- batch size
- $L$ -- number of layers
- $T$ -- cached tokens
- $H_{kv}$ -- number of key-value heads
- $D$ -- head dimension
- $2$ -- one tensor for keys and one for values
- $s$ -- bytes per stored element
- $\mathrm{GiB}$ -- binary gibibytes, not decimal gigabytes

## From Math To Code

- Multiply the per-token cache size by tokens, layers, and batch size.
- Convert bytes to GiB when you need a deployment estimate instead of a raw count.

## Minimal Code Mental Model

```python
cache_bytes = kv_cache_bytes(
    num_layers,
    num_tokens,
    num_kv_heads,
    head_dim,
    bytes_per_element,
)
cache_gib = kv_cache_gib(
    num_layers,
    num_tokens,
    num_kv_heads,
    head_dim,
    bytes_per_element,
)
```

## Function

```python
def kv_cache_bytes(
    num_layers: int,
    num_tokens: int,
    num_kv_heads: int,
    head_dim: int,
    bytes_per_element: int,
    batch_size: int = 1,
) -> int:
def kv_cache_gib(
    num_layers: int,
    num_tokens: int,
    num_kv_heads: int,
    head_dim: int,
    bytes_per_element: int,
    batch_size: int = 1,
) -> float:
```

## When To Use What

- Use this estimate when context length, batch size, or head layout changes.
- Use it before deployment to check whether a serving plan fits GPU memory.
- Pair it with batching and prefix-cache topics when inference throughput is the real concern.

## Run tests

```bash
pytest modules/ml/llm/kv-cache/python -q
```
