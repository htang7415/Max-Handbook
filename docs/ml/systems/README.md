# Training Loop Mechanics

Training loop mechanics and debugging signals.
Each bullet maps to a module under `modules/ml/systems/`.

## Core Steps

- Zeroing gradients (`modules/ml/systems/zero-gradients`)
- Forward pass (`modules/ml/systems/forward-pass`)
- Backward pass (`modules/ml/systems/backward-pass`)
- Optimizer step (`modules/ml/systems/optimizer-step`)
- Gradient accumulation (`modules/ml/systems/gradient-accumulation`)
- Mixed precision training (`modules/ml/systems/mixed-precision`)
- Check gradients are flowing (`modules/ml/systems/check-gradients`)
- Debug overfitting vs underfitting (`modules/ml/systems/debug-overfit-underfit`)

## Performance Models

- Roofline analysis (`modules/ml/systems/roofline-analysis`)
- Tensor parallel linear communication (`modules/ml/systems/tensor-parallelism`)
- Context parallel attention bytes (`modules/ml/systems/context-parallelism`)
- Expert parallel dispatch (`modules/ml/systems/expert-parallelism`)
- Expert load-balancing loss (`modules/ml/systems/expert-load-balancing`)

## Serving Mechanics

- Continuous batching (`modules/ml/systems/continuous-batching`)
- Chunked prefill rounds (`modules/ml/systems/chunked-prefill`)
- Prefix cache savings metrics (`modules/ml/systems/prefix-cache-metrics`)

See also:

- GPU systems guide (`docs/ml/systems/gpu`)
- Distributed systems guide (`docs/ml/systems/distributed`)
