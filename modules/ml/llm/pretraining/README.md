# Pretraining (Next-Token Loss)

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to connect language-model pretraining to the actual token-level
cross-entropy being minimized.

## First Principles

- Pretraining for causal LMs is repeated next-token classification.
- Each position contributes one negative log-likelihood term.
- The training loss is the average of those token losses.
- Perplexity is just the exponential of that mean negative log-likelihood.

## Core Math

Per-token negative log-likelihood:

$$
\ell_t = -\log p_\theta(x_t \mid x_{<t})
$$

Mean next-token loss:

$$
L = \frac{1}{T}\sum_{t=1}^{T}\ell_t
$$

With logits:

$$
\ell_t = -\log\left(\mathrm{softmax}(\text{logits}_t)_{\text{target}_t}\right)
$$

## From Math To Code

- Convert each logit row into a probability distribution.
- Pick the probability assigned to the correct next token.
- Take the negative log.
- Average across positions.

## Minimal Code Mental Model

```python
losses = token_nlls(logits, targets)
loss = next_token_loss(logits, targets)
```

## Function

```python
def token_nlls(logits: list[list[float]], targets: list[int]) -> list[float]:
def next_token_loss(logits: list[list[float]], targets: list[int]) -> float:
```

## When To Use What

- Use `token_nlls` when you want to inspect which positions are easy or hard.
- Use `next_token_loss` when you want the mean pretraining objective for a batch.
- Pair this module with `perplexity` when you want the same signal in exponentiated form.

## Run tests

```bash
pytest modules/ml/llm/pretraining/python -q
```
