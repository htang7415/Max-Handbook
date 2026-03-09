# Gradient Accumulation

> Track: `ml` | Topic: `systems`

## Concept

Gradient accumulation is a technique that simulates training with a large batch size by splitting it into several smaller micro-batches. Instead of updating parameters after every micro-batch, gradients are summed (or averaged) over $K$ micro-batches, and only then is the optimizer step performed. This produces mathematically equivalent updates to using a single large batch, while requiring only enough GPU memory to process one micro-batch at a time.

This technique is especially important when training large models where the desired batch size exceeds available GPU memory. It is also the foundation of distributed training strategies like data parallelism, where each device computes gradients on its own micro-batch and the results are aggregated before the optimizer step. The key implementation detail is to divide the accumulated gradient by the number of accumulation steps $K$ so the effective learning rate remains consistent.

## Math

Given $K$ micro-batches each of size $B_{\text{micro}}$, the effective gradient used for the parameter update is:

$$g_{\text{eff}} = \frac{1}{K} \sum_{k=1}^{K} g_k$$

The effective batch size is:

$$B_{\text{eff}} = K \cdot B_{\text{micro}}$$

- $g_k$ -- gradient computed on the $k$-th micro-batch
- $K$ -- number of accumulation steps
- $B_{\text{micro}}$ -- micro-batch size (samples per forward/backward pass)
- $B_{\text{eff}}$ -- effective batch size seen by the optimizer

## Key Points

- Gradient accumulation enables large effective batch sizes on hardware with limited memory by trading compute time for memory.
- Always divide the accumulated gradient by $K$ (or equivalently scale the loss by $\frac{1}{K}$) -- forgetting this changes the effective learning rate.
- Zero the gradients only after the optimizer step, not after each micro-batch, otherwise the accumulation is lost.
- Batch normalization statistics are computed per micro-batch, not per effective batch, which can slightly change training dynamics compared to true large-batch training.

## Function

```python
def accumulate(grads: list[list[float]]) -> list[float]:
```

- `grads` -- list of $K$ gradient vectors, one per micro-batch; each inner list has one entry per parameter

## Run tests

```bash
pytest modules/ml/systems/gradient-accumulation/python -q
```
