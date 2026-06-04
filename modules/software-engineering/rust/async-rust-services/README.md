# Async Rust Services

> Track: `software-engineering` | Topic: `rust`

## Concept

Async Rust services are most useful for I/O-bound concurrency, but they still need explicit concurrency limits and backpressure.

## Use When

| Workload Signal | Async Fit |
| --- | --- |
| Many I/O waits | Strong fit |
| CPU-bound work dominates | Prefer CPU parallelism or optimization |
| In-flight requests can exceed capacity | Add explicit budget and backpressure |

## First Principles

- Async in Rust helps when work waits on external operations more than it burns CPU.
- Concurrency budgets should stay explicit.
- Backpressure is a first-class service behavior, not an afterthought.

## Workflow

1. Measure external wait time and local CPU time.
2. Set a concurrency budget per worker or service.
3. Apply backpressure before spawning more work.
4. Test the behavior at the budget boundary.

## Minimal Code Mental Model

```rust
let budget = block_on_ready(concurrency_budget(4, 25));
assert!(async_service_fit(120, 20));
assert!(backpressure_needed(120, budget));
```

## Failure Modes

| Mistake | Result |
| --- | --- |
| Async for CPU-bound paths | Runtime overhead without useful concurrency |
| Unbounded task spawning | Memory and latency grow under load |
| Backpressure hidden from callers | Overload behavior is unpredictable |

## Function

```rust
pub async fn concurrency_budget(worker_count: usize, per_worker_in_flight: usize) -> usize;
pub fn async_service_fit(network_wait_ms: u64, cpu_ms: u64) -> bool;
pub fn backpressure_needed(in_flight: usize, budget: usize) -> bool;
pub fn block_on_ready<F: Future>(future: F) -> F::Output;
```

## Run tests

```bash
cargo test --manifest-path modules/software-engineering/rust/async-rust-services/rust/Cargo.toml
```
