# Long Context and Caching

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand why long-context inference gets expensive and why
prompt or context caching matters in real systems.

## First Principles

- Long context increases what the model can condition on, but it also raises latency and memory cost.
- Prefill work is paid on prompt tokens before decoding starts.
- Repeated prompt prefixes are the best place to save work with caching.
- Long context and caching should be reasoned about together, not as separate serving topics.

## Core Math

Quadratic attention work:

$$
\mathrm{Pairs}(L) = L^2
$$

Effective prompt tokens after caching `C` of `T` prompt tokens:

$$
\mathrm{EffectivePrompt} = T - C
$$

Saved tokens across `r` repeated requests with shared cached prefix `C`:

$$
\mathrm{SavedTokens} = C(r - 1)
$$

Cache hit rate:

$$
\mathrm{HitRate} = \frac{C}{T}
$$

Context utilization:

$$
\mathrm{Utilization} = \frac{T}{W}
$$

- $L$ -- active sequence length
- $T$ -- total prompt tokens
- $C$ -- cached prefix tokens, with $0 \le C \le T$
- $r$ -- number of repeated requests sharing the same prefix
- $W$ -- context window

## From Math To Code

- Start by estimating how sequence length changes attention work.
- Measure how much of the prompt is reusable prefix.
- Subtract cached prefix tokens from total prompt tokens to estimate fresh prefill work.
- Convert that cached prefix fraction into a hit-rate style summary for monitoring.

## Minimal Code Mental Model

```python
pairs = quadratic_attention_pairs(sequence_length=128_000)
effective = effective_prefix_tokens(
    total_prompt_tokens=64_000,
    cached_prefix_tokens=48_000,
)
saved = prompt_cache_saved_tokens(shared_prefix_tokens=48_000, repeated_requests=10)
hit_rate = cache_hit_rate(cached_prefix_tokens=48_000, total_prompt_tokens=64_000)
```

## Functions

```python
def quadratic_attention_pairs(sequence_length: int) -> int:
def context_utilization(total_tokens: int, context_window: int) -> float:
def effective_prefix_tokens(total_prompt_tokens: int, cached_prefix_tokens: int) -> int:
def prompt_cache_saved_tokens(shared_prefix_tokens: int, repeated_requests: int) -> int:
def cache_hit_rate(cached_prefix_tokens: int, total_prompt_tokens: int) -> float:
```

## When To Use What

- Use `quadratic_attention_pairs` when sequence length is the main scaling issue.
- Use `context_utilization` when deciding whether a prompt fits comfortably inside the available window.
- Use `effective_prefix_tokens` and `prompt_cache_saved_tokens` when prompt caching is the main optimization.
- Use `cache_hit_rate` for a simple serving-side summary of reusable prefix coverage.

## Run tests

```bash
pytest modules/ml/llm/long-context-and-caching/python -q
```
