# Distributed ML Systems

Distributed training and serving are mostly about communication patterns and where state lives.

## Purpose

Use this guide to route distributed-ML questions into the right communication pattern:
- tensor and context parallelism
- expert parallelism and routing
- synchronization cost
- state placement in training and serving

## First Principles

- Distributed ML is mostly about communication cost and where model state lives.
- Parallelism choices change both throughput and coordination overhead.
- Expert systems fail when routing balance is ignored.
- Training and serving workloads often need different parallelism choices.

## Core Math

- Throughput scales only if communication does not dominate compute.
- Synchronization cost grows with tensor size and collective frequency.
- Expert systems add a load-balancing objective on top of routing correctness.

## Minimal Code Mental Model

```python
local_grad = backward_step(batch_shard)
global_grad = all_reduce(local_grad)
tokens = dispatch_to_experts(hidden, routes)
```

## Canonical Modules

- Shared foundation: `training-loop-mechanics`
- Parallelism: `tensor-parallelism`, `context-parallelism`, `expert-parallelism`
- Balance and routing: `expert-load-balancing`, `moe-routing`

## When To Use What

- Start with `training-loop-mechanics` before any distributed variant.
- Use tensor parallelism when one layer no longer fits or runs efficiently on one device.
- Use context parallelism when sequence length is the main scaling bottleneck.
- Use expert parallelism when sparse MoE structure is the main scaling tool.
- Use expert load-balancing when routing works functionally but cluster efficiency is poor.
