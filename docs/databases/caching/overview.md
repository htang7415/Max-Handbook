# Caching And Semantic Caching

Caches reduce latency and cost by serving reused data from a faster copy.

## Purpose

Use this topic to learn classic cache patterns, invalidation trade-offs, and where AI-era semantic caching fits.

## First Principles

- A cache is a copy. The core problem is deciding when that copy is valid enough to trust.
- Read-mostly workloads benefit from cache-aside patterns. Write-heavy workloads often fail when caching is added naively.
- TTL is a freshness policy, not a correctness guarantee.
- Semantic caching helps with repeated LLM requests, but it does not replace authorization checks, grounding checks, or product-specific invalidation.

## Minimal Query Mental Model

```python
value = cache.get(key)
if value is None:
    value = load_from_database(key)
    cache.set(key, value, ttl=300)
return value
```

## Canonical Modules

- `cache-aside`
- `ttl-and-invalidation`
- `write-through-vs-write-behind`
- `client-side-caching`
- `cache-consistency-patterns`
- `hot-key-and-rate-limit-protection`
- `semantic-caching-basics`

## Supporting Modules

- `semantic-cache-invalidation`
- `semantic-cache-hit-rate-analysis`
- `cache-stampede-mitigation`
- `cache-admission-policies`
- `negative-caching-patterns`

## Boundary Notes

- `semantic-caching-basics` teaches when a request can reuse a previous answer.
- `semantic-cache-invalidation` teaches when a previous answer must be removed or ignored because policy, source data, or tenant scope changed.
- `ttl-and-invalidation` is the general cache freshness module; semantic invalidation is the AI-answer-specific version with policy and corpus versions.

## When To Use What

- Start with `cache-aside`, then learn TTL and invalidation before any more advanced cache policy.
- Add write-through, write-behind, and client-side caching only when the ownership and freshness rules are already clear.
- Use consistency, stampede, and hot-key modules when the cache is already on a real product path.
- Use semantic caching only for repeated retrieval or model-answer patterns with stable permissions and bounded freshness needs.
