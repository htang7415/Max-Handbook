# Deep Learning Training Techniques

Training techniques are the practical layer between a correct model and a stable training run.

## Purpose

Use this page to separate three different kinds of training tricks:
- regularization
- target shaping
- numerical stability

## First Principles

- Some techniques reduce overfitting by constraining the model or stopping earlier.
- Some techniques change the target signal so the model learns softer or more focused behavior.
- Some techniques keep optimization numerically stable at scale.
- These techniques are useful only after the base model and loss already make sense.

## Core Math

- Weight decay adds a penalty:
  $$
  L_{\text{total}} = L + \lambda \|w\|^2
  $$
- Label smoothing replaces a hard target with a softened distribution.
- Focal loss downweights easy examples and emphasizes hard ones.

## Minimal Code Mental Model

```python
loss = criterion(logits, targets)
loss = loss + weight_decay * l2_norm(model)
loss.backward()
clip_gradients(model)
optimizer.step()
```

## Canonical Modules

- Regularization: `dropout`, `early-stopping`, `weight-decay`
- Target shaping: `label-smoothing`, `knowledge-distillation-loss`, `focal-loss`
- Numerical stability: `gradient-clipping`, `loss-scaling`

## When To Use What

- Start with `weight-decay` and `early-stopping` before more specialized tricks.
- Use `label-smoothing` when overconfidence is the issue.
- Use `knowledge-distillation-loss` when the training signal should come from a stronger teacher.
- Use `focal-loss` when class imbalance or easy-example dominance is the real problem.
- Use `gradient-clipping` and `loss-scaling` when the failure is numerical, not conceptual.
