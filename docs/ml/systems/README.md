# ML Systems

ML systems are about how training and inference actually run on hardware.

## Purpose

Use this page to organize systems thinking into four parts:
- training loop mechanics
- profiling and bottlenecks
- inference scheduling
- distributed execution

## First Principles

- The training loop is a sequence of state updates, not a black box.
- Memory movement is often the real bottleneck, not raw FLOPs.
- Serving quality depends on batching, caching, and scheduling, not just model quality.
- Parallelism changes communication cost as much as it changes throughput.

## Core Math

- Arithmetic intensity:
  $$
  \frac{\mathrm{FLOPs}}{\mathrm{bytes\ moved}}
  $$
- Batch throughput:
  $$
  \frac{\mathrm{tokens\ or\ examples}}{\mathrm{second}}
  $$
- Communication grows with tensor size and synchronization frequency.

## Minimal Code Mental Model

```python
optimizer.zero_grad()
loss = model(batch).loss
loss.backward()
optimizer.step()
```

## Canonical Modules

- Training loop: `zero-gradients`, `forward-pass`, `backward-pass`, `optimizer-step`, `gradient-accumulation`, `mixed-precision`
- Profiling and debugging: `check-gradients`, `debug-overfit-underfit`, `roofline-analysis`
- Inference scheduling: `continuous-batching`, `chunked-prefill`, `prefix-cache-metrics`
- Distributed execution: `tensor-parallelism`, `context-parallelism`, `expert-parallelism`, `expert-load-balancing`

## Supporting Guides

- GPU systems guide (`docs/ml/systems/gpu`)
- Distributed systems guide (`docs/ml/systems/distributed`)

## When To Use What

- Start with the training loop modules before distributed systems.
- Use `roofline-analysis` when you need a first-principles performance model.
- Use batching and cache modules when latency and throughput are the main problem.
- Use tensor, context, or expert parallelism only when one-device execution is no longer enough.
