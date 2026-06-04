# Caching Basics

> Track: `software-engineering` | Topic: `performance`

## Concept

Caching is useful when repeated reads are common and the system can tolerate some freshness lag without violating correctness.

## Use When

| Signal | Cache Decision |
| --- | --- |
| Many repeated reads | Consider caching |
| Low mutation frequency | Cache is easier to keep fresh |
| Strict freshness required | Avoid or tightly invalidate |
| Low hit rate | Cache likely adds complexity without value |

## First Principles

- A cache is only as good as its invalidation and freshness rules.
- High mutation rates increase stale-data risk.
- Hit rate is the main signal for whether the cache is paying for itself.

## Workflow

1. Define the freshness tolerance.
2. Estimate read frequency, mutation frequency, and object size.
3. Add invalidation or TTL rules before adding the cache.
4. Measure hit rate and stale-read impact after rollout.

## Minimal Code Mental Model

```python
worth_it = should_cache(read_frequency=1000, mutation_frequency=5, freshness_tolerance_s=60)
hit_rate = cache_hit_rate(hits=900, lookups=1000)
risk = stale_risk(mutation_frequency=20, freshness_tolerance_s=5)
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| No invalidation rule | Stale data becomes a correctness bug |
| Caching low-read data | Extra latency and memory with little benefit |
| Ignoring mutation rate | Freshness assumptions break under writes |

## Function

```python
def should_cache(read_frequency: int, mutation_frequency: int, freshness_tolerance_s: int) -> bool:
def cache_hit_rate(hits: int, lookups: int) -> float:
def stale_risk(mutation_frequency: int, freshness_tolerance_s: int) -> str:
```

## Run tests

```bash
pytest modules/software-engineering/performance/caching-basics/python -q
```
