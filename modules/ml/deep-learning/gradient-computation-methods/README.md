# Gradient Computation Methods

> Track: `ml` | Topic: `deep-learning`

## Purpose

Use this module to learn how deep-learning systems actually obtain gradients:
manual backpropagation, automatic differentiation, and finite-difference checks.

## First Principles

- Backpropagation applies the chain rule layer by layer.
- Automatic differentiation builds the same chain rule into a computation graph.
- Gradient checking does not train the model; it verifies that the analytic gradient is plausible.

## Core Math

Local backpropagation rule:

$$
\frac{\partial L}{\partial w} = \frac{\partial L}{\partial z}\cdot x
$$

Autodiff path view:

$$
\frac{\partial L}{\partial x}=\sum_{\text{paths }x\rightarrow L}\prod \text{local derivatives}
$$

Finite difference:

$$
\frac{df}{dx} \approx \frac{f(x+\epsilon) - f(x-\epsilon)}{2\epsilon}
$$

## From Math To Code

- Compute the forward scalar first.
- Define a small scalar loss from that forward value.
- Differentiate it either analytically, through autodiff, or with finite differences.

## Minimal Code Mental Model

```python
pred = linear_forward(x=3.0, w=2.0, b=1.0)
loss = squared_error(prediction=pred, target=5.0)
grad_w = linear_backprop(x=3.0, w=2.0, grad_out=0.5)
approx = grad_check(lambda v: v * v, x=3.0)
value = Value(2.0) * Value(-3.0)
```

## Functions

```python
def linear_forward(x: float, w: float, b: float = 0.0) -> float:
def squared_error(prediction: float, target: float) -> float:
def linear_backprop(x: float, w: float, grad_out: float) -> float:
class Value:
def grad_check(f, x: float, eps: float = 1e-5) -> float:
```

## When To Use What

- Use `linear_backprop` to understand the local mechanics of the chain rule.
- Use `Value` when you want the computation-graph view of automatic differentiation.
- Use `grad_check` only for debugging custom gradients or verifying a small implementation.

## Run tests

```bash
pytest modules/ml/deep-learning/gradient-computation-methods/python -q
```
