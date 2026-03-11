# LLM Inference Serving

Serving quality depends on latency, memory, batching, and hardware efficiency more than on model architecture alone.

## Purpose

Use this guide to organize LLM serving around the real bottlenecks:
- long-context cost
- cache reuse
- batching and scheduling
- memory format and hardware limits

## First Principles

- Serving quality is mostly a systems problem once the base model is fixed.
- TTFT, ITL, and tokens per second are shaped by scheduling and memory movement as much as by raw compute.
- Cache reuse matters only when prompts actually share structure.
- Long context is expensive because prefill cost and cache memory both grow quickly.

## Core Math

- KV cache memory grows with sequence length and layer width.
- Throughput is roughly:
  $$
  \frac{\text{tokens}}{\text{second}}
  $$
- Shared-prefix reuse changes effective prefill cost by avoiding repeated prompt work.

## Minimal Code Mental Model

```python
batch = continuous_batch(requests)
cached = prefix_cache_lookup(prompt_prefix)
decoded = speculative_decode(batch, draft_model, target_model)
```

## Canonical Modules

- Context and cache fundamentals: `long-context-and-caching`, `kv-cache`, `prefix-cache`
- Serving efficiency: `precision-and-quantization`, `speculative-decoding`
- Scheduling: `request-batching`, `continuous-batching`, `chunked-prefill`
- Performance modeling: `roofline-analysis`, `prefix-cache-metrics`

## When To Use What

- Start with `long-context-and-caching` when context length or memory is the first bottleneck.
- Use `kv-cache` and `prefix-cache` when reuse and memory budgets are the main issue.
- Use batching modules when latency and throughput trade-offs dominate.
- Use `precision-and-quantization` when model memory footprint blocks deployment targets.
- Use `speculative-decoding` only when verification overhead is smaller than the decode savings.
