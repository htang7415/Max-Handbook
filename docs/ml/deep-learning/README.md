# Deep Learning

Deep learning is about learning useful functions by composing linear maps,
nonlinearities, and gradient-based updates.

## Purpose

Use this page to keep deep learning in the right order:
- neuron and network basics
- gradients and backpropagation
- activation and normalization choices
- losses and regularization
- training stability for modern models

## First Principles

- A layer computes an affine map and then a nonlinearity.
- Backpropagation works because the chain rule propagates local gradients.
- Training quality depends on signal flow, not just model size.
- Activation, initialization, and normalization mostly exist to keep gradients usable.
- Regularization matters because a model that memorizes is not learning a reusable representation.

## Core Math

- Most deep-learning mechanics reduce to three shapes:
  $$
  y = \phi(Wx + b),
  \quad
  \text{chain rule},
  \quad
  \text{loss}
  $$
- The family modules below hold the actual comparison details.

## Minimal Code Mental Model

```python
hidden = activation(x @ w1 + b1)
logits = hidden @ w2 + b2
loss = criterion(logits, labels)
```

## Canonical Modules

- Network basics: `neuron-weights-bias-activation`, `feedforward-neural-network`
- Gradient mechanics: `backpropagation`, `automatic-differentiation`, `gradient-flow`
- Activations: `activation-functions`, `activation-failure-modes`
- Initialization and normalization: `xavier-initialization`, `he-initialization`, `normalization-methods`
- Losses and training signals: `cross-entropy`, `mse-loss`, `focal-loss`, `label-smoothing`, `knowledge-distillation-loss`
- Regularization: `dropout`, `weight-decay`, `early-stopping`

## Supporting Guides

- Training techniques (`docs/ml/deep-learning/training-techniques`)

## When To Use What

- Start with feedforward, activations, and backprop before optimization tricks.
- Use `activation-functions` and `normalization-methods` as the default entry points, not the old narrow variants.
- Use `cross-entropy` for most classification setups and `mse-loss` for basic regression.
- Use `label-smoothing` or `knowledge-distillation-loss` when the problem is modern training behavior, not basic function approximation.
- Use `qk-clip` from the LLM track only when attention-logit stability is the actual issue.
- Use this page as the map; use the canonical modules when you want the real formulas and code.
