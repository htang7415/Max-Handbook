# LLM Long Context

Long-context systems are about fitting more information into the prompt without making inference too slow or too expensive.

## Purpose

Use this page to understand:
- how long prompts change inference cost
- why context reuse matters
- when caching helps more than model changes

## First Principles

- Longer prompts increase prefill work before decoding starts.
- Attention cost grows quickly with sequence length.
- Shared prefixes are the easiest place to save work across requests.
- Long context is a systems topic as much as a model topic.

## Core Math

- Attention pair count:
  $$
  L^2
  $$
- Effective prompt after caching:
  $$
  T - C
  $$
  where `T` is total prompt tokens and `C` is cached prefix tokens.
- Cache hit rate:
  $$
  \frac{C}{T}
  $$

## Minimal Code Mental Model

```python
pairs = quadratic_attention_pairs(sequence_length=128_000)
effective = effective_prefix_tokens(total_prompt_tokens=64_000, cached_prefix_tokens=48_000)
hit_rate = cache_hit_rate(cached_prefix_tokens=48_000, total_prompt_tokens=64_000)
```

## Canonical Modules

- Main long-context mental model: `long-context-and-caching`
- KV memory growth: `kv-cache`
- Prefix reuse: `prefix-cache`, `prefix-cache-metrics`
- Serving support: `chunked-prefill`, `continuous-batching`

## When To Use What

- Start with `long-context-and-caching` when prompt length is the main constraint.
- Use `kv-cache` when memory, not prompt preprocessing, is the bottleneck.
- Use `prefix-cache` when requests share large repeated instructions or documents.
- Use `chunked-prefill` and `continuous-batching` when long prompts have to coexist with real serving throughput.
