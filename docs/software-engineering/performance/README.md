# Performance

This section is about response time, throughput, resource cost, and where the real bottlenecks come from.

## Purpose

Use this page to organize performance into:
- latency budgets
- throughput constraints
- caching and batching
- profiling and cost tradeoffs

## First Principles

- Performance work starts with measurement, not with optimization folklore.
- Latency is often dominated by a few slow boundaries, not by every line of code equally.
- Throughput, memory, and cost trade off against each other.
- The right optimization depends on the bottleneck shape: CPU, I/O, memory, network, or contention.

## Canonical Modules

- `latency-budgeting`
- `caching-basics`
- `batching-vs-streaming`
- `profiling-workflow`
- `memory-and-allocation-basics`
- `cost-performance-tradeoffs`

## Math And Code

- Math matters here through latency decomposition, throughput, allocation counts, cache hit rates, and cost curves.
- Code should stay measurement-first: small profiles, budget calculations, batching choices, and correctness-preserving optimizations.

## When To Use What

- Start with latency budgets and profiling before trying micro-optimizations.
- Use caching only when invalidation and freshness rules are explicit enough to keep it correct.
- Use batching when amortization matters more than tail latency.
- Use streaming when early partial results matter more than total completion time.
