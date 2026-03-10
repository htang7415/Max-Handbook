# GPU Performance

GPU reasoning should connect model math to memory traffic and achievable throughput.

## Current Anchors

- Mixed precision training (`modules/ml/systems/mixed-precision`)
- Numeric formats and quantization (`modules/ml/llm/precision-and-quantization`)
- Roofline analysis (`modules/ml/systems/roofline-analysis`)

## Concepts to Cover Well

- Arithmetic intensity
- Compute-bound vs memory-bound kernels
- Quantization and memory savings
- Kernel fusion and bandwidth pressure
