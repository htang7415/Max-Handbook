# Optimizer Methods

> Track: `ml` | Topic: `optimization`

## Purpose

Use this module to compare the small set of optimizer update rules that matter most in practice:
plain SGD, momentum variants, and adaptive optimizers.

## First Principles

- Every optimizer starts from the same core update:
  $$
  w_{t+1} = w_t - \eta \cdot \text{update}_t
  $$
- SGD uses the raw gradient.
- Momentum methods smooth updates across steps.
- Adaptive methods rescale updates using gradient history.
- AdamW matters because decoupled weight decay changes training behavior in modern deep nets.
- The code here uses the minimal Adam/AdamW recurrences without bias correction so the state updates stay easy to inspect.

## Core Math

$$
\text{SGD: } w_{t+1} = w_t - \eta g_t
$$

$$
\text{Momentum: } v_t = \mu v_{t-1} + g_t,\quad w_{t+1} = w_t - \eta v_t
$$

$$
\text{Adaptive: } w_{t+1} = w_t - \eta \frac{m_t}{\sqrt{v_t} + \epsilon}
$$

- $\eta$ -- learning rate
- $g_t$ -- gradient at step $t$
- $v_t$ -- momentum or second-moment state, depending on the optimizer
- $\mu$ -- momentum coefficient
- $\epsilon$ -- numerical stabilizer

## From Math To Code

- Build the update in stages: gradient, momentum state, then parameter step.
- Reuse the same velocity equation across momentum and Nesterov so the code mirrors the math.
- Treat decoupled weight decay as a separate shrinkage term, not as part of the gradient itself.
- Read adaptive optimizers as moving-average estimators for first and second moments.

## Minimal Code Mental Model

```python
v = momentum_velocity(grad, v, mu)
w = sgd_step(w, grad, lr)
w, v = momentum_step(w, grad, v, lr, mu)
shrink = weight_decay_term(w, lr, wd)
w, m, v = adamw_step(w, grad, m, v, lr, wd, beta1, beta2, eps)
```

## Functions

```python
def momentum_velocity(grad: float, v: float, mu: float) -> float:
def sgd_step(w: float, grad: float, lr: float) -> float:
def momentum_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
def nesterov_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
def adagrad_step(w: float, grad: float, g2: float, lr: float, eps: float) -> tuple[float, float]:
def rmsprop_step(w: float, grad: float, v: float, lr: float, beta: float, eps: float) -> tuple[float, float]:
def adam_step(w: float, grad: float, m: float, v: float, lr: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
def adamw_step(w: float, grad: float, m: float, v: float, lr: float, wd: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
def weight_decay_term(w: float, lr: float, wd: float) -> float:
```

## When To Use What

- Use SGD when you want the cleanest baseline update.
- Use momentum or Nesterov when SGD oscillates and you want smoother progress.
- Use Adagrad or RMSProp when per-parameter scaling matters.
- Use Adam or AdamW as the modern default, with AdamW preferred when weight decay matters.

## Run tests

```bash
pytest modules/ml/optimization/optimizer-methods/python -q
```
