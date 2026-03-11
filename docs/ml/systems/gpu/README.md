# GPU Performance

GPU reasoning should connect model math to memory traffic and achievable throughput.

## Purpose

Use this guide to connect model code to hardware behavior:
- arithmetic intensity
- compute-bound versus memory-bound kernels
- numeric formats
- throughput limits

## First Principles

- GPU performance is often limited by memory movement rather than raw FLOPs.
- Arithmetic intensity is the first quick check for whether a kernel is compute-bound or bandwidth-bound.
- Numeric formats change memory footprint, bandwidth pressure, and sometimes the feasible batch size.
- Throughput gains that ignore memory traffic usually do not hold up in real workloads.

## Core Math

- Arithmetic intensity:
  $$
  \frac{\mathrm{FLOPs}}{\mathrm{bytes\ moved}}
  $$
- Throughput:
  $$
  \frac{\text{tokens or examples}}{\text{second}}
  $$

## Minimal Code Mental Model

```python
intensity = flops / bytes_moved
loss = model(batch).loss
loss.backward()
optimizer.step()
```

## Canonical Modules

- Execution baseline: `training-loop-mechanics`
- Performance model: `roofline-analysis`
- Memory-format leverage: `precision-and-quantization`

## When To Use What

- Start with `training-loop-mechanics` before hardware-level tuning.
- Use `roofline-analysis` when you need a first-principles performance model.
- Use `precision-and-quantization` when memory footprint and bandwidth pressure dominate.
- Revisit batching and serving modules when the bottleneck is request scheduling rather than kernel behavior.
