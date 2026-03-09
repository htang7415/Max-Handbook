# Distributed ML Systems

Distributed training and serving are mostly about communication patterns and where state lives.

## Current Anchors

- Gradient accumulation (`modules/ml/systems/gradient-accumulation`)
- Tensor parallel linear communication (`modules/ml/systems/tensor-parallelism`)
- Context parallel attention bytes (`modules/ml/systems/context-parallelism`)
- Expert parallel dispatch (`modules/ml/systems/expert-parallelism`)
- Expert load-balancing loss (`modules/ml/systems/expert-load-balancing`)
- Sparse MoE routing (`modules/ml/llm/moe-routing`)

## Concepts to Cover Well

- Data, tensor, expert, and context parallelism
- All-reduce cost and synchronization bottlenecks
- Load balancing across experts, not just routing correctness
- Prefill vs decode workload separation
- When communication dominates compute
