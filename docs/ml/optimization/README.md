# Optimization and Training Dynamics

How gradients become stable updates.
Each bullet maps to a module under `modules/ml/optimization/`.

## Optimizers

- SGD (`modules/ml/optimization/sgd`)
- SGD with Momentum (`modules/ml/optimization/sgd-momentum`)
- Nesterov Accelerated Gradient (`modules/ml/optimization/nesterov`)
- Adam (`modules/ml/optimization/adam`)
- AdamW (decoupled weight decay) (`modules/ml/optimization/adamw`)
- RMSProp (`modules/ml/optimization/rmsprop`)
- Adagrad (`modules/ml/optimization/adagrad`)
- Muon (high-level intuition) (`modules/ml/optimization/muon-optimizer`)

## Learning Rate Strategies

- Constant LR (`modules/ml/optimization/lr-constant`)
- Step decay (`modules/ml/optimization/lr-step-decay`)
- Exponential decay (`modules/ml/optimization/lr-exponential-decay`)
- Warmup (`modules/ml/optimization/lr-warmup`)
- Cosine decay (`modules/ml/optimization/lr-cosine-decay`)
- Warmup plus cosine decay (`modules/ml/optimization/warmup-cosine-decay`)
- One-cycle schedule (`modules/ml/optimization/one-cycle-schedule`)
- Cosine restarts (`modules/ml/optimization/cosine-restarts`)

## Training Stability

- Gradient clipping (global norm) (`modules/ml/optimization/gradient-clipping`)
- Loss scaling (mixed precision) (`modules/ml/optimization/loss-scaling`)
- Detecting NaNs / divergence (`modules/ml/optimization/detect-nans`)
