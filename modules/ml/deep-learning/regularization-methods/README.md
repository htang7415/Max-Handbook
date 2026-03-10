# Regularization Methods

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to compare the main regularization tools that matter in practice:
weight penalties, dropout, and early stopping.

## First Principles

- Regularization reduces overfitting by discouraging overly specific solutions.
- L1 favors sparsity.
- L2 and weight decay shrink weights smoothly.
- Dropout injects noise into hidden activations during training.
- Early stopping regularizes through training duration instead of an explicit penalty term.

## Core Math

$$
L = L_0 + \lambda \sum_i |w_i|,
\quad
L = L_0 + \lambda \sum_i w_i^2
$$

$$
x' = \frac{m \odot x}{1-p},
\quad
w \leftarrow w - \eta (g + \lambda w)
$$

## Minimal Code Mental Model

```python
penalty = l2_penalty(weights, lam=1e-4)
masked = dropout(activations, p=0.1, seed=1)
stop = should_stop(val_losses, patience=3)
```

## Function

```python
def l1_penalty(weights: list[float], lam: float) -> float:
def l2_penalty(weights: list[float], lam: float) -> float:
def weight_decay_step(w: float, grad: float, lr: float, lam: float) -> float:
def dropout(x: list[float], p: float, seed: int = 0) -> list[float]:
def should_stop(losses: list[float], patience: int) -> bool:
```

## When To Use What

- Use L1 when sparsity is part of the goal.
- Use L2 or weight decay as the standard smooth parameter shrinkage baseline.
- Use dropout when model co-adaptation is the problem.
- Use early stopping when validation performance starts degrading before the optimizer has fully converged.

## Run tests

```bash
pytest modules/ml/deep-learning/regularization-methods/python -q
```
