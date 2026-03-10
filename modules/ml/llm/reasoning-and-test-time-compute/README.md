# Reasoning and Test-Time Compute

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand why modern reasoning models often improve when you
spend more compute at inference time.

## First Principles

- Test-time compute changes how much work you do per request, not the model weights.
- More compute can come from longer reasoning traces, multiple samples, or vote aggregation.
- Better answers are not free: more reasoning usually costs more latency and tokens.
- Extra compute only helps when the base model already has useful signal to amplify.

## Core Math

If one request uses `P` prompt tokens, `R` reasoning tokens, and `A` answer
tokens, then `n` sampled traces cost:

$$
\mathrm{Tokens}(n) = n(P + R + A)
$$

Relative compute multiplier versus one direct answer:

$$
\mathrm{Multiplier} = \frac{n(P + R + A)}{P + A}
$$

If one sampled trace succeeds with probability `q`, then best-of-`n` success is:

$$
\mathrm{BestOfN}(q, n) = 1 - (1 - q)^n
$$

Majority-vote success for odd `n`:

$$
\sum_{k=\lfloor n/2 \rfloor + 1}^{n} \binom{n}{k} q^k (1-q)^{n-k}
$$

## From Math To Code

- Count prompt, reasoning, and answer tokens for one trace first.
- Multiply by the number of traces to see the real test-time cost.
- Treat best-of-`n` and majority vote as wrappers around single-trace quality.
- Use these formulas to reason about the latency/quality tradeoff before deployment.

## Minimal Code Mental Model

```python
tokens = total_inference_tokens(
    prompt_tokens=1200,
    reasoning_tokens=1800,
    answer_tokens=200,
    samples=4,
)
multiplier = test_time_compute_multiplier(
    prompt_tokens=1200,
    reasoning_tokens=1800,
    answer_tokens=200,
    samples=4,
)
best = best_of_n_success_probability(single_try_success=0.35, n=4)
vote = majority_vote_success_probability(single_try_success=0.7, n=5)
```

## Functions

```python
def total_inference_tokens(
    prompt_tokens: int,
    reasoning_tokens: int,
    answer_tokens: int,
    samples: int = 1,
) -> int:
def test_time_compute_multiplier(
    prompt_tokens: int,
    reasoning_tokens: int,
    answer_tokens: int,
    samples: int = 1,
) -> float:
def best_of_n_success_probability(single_try_success: float, n: int) -> float:
def majority_vote_success_probability(single_try_success: float, n: int) -> float:
```

## When To Use What

- Use `total_inference_tokens` when comparing reasoning presets or sampling plans.
- Use `test_time_compute_multiplier` when you want one number for the extra inference cost.
- Use `best_of_n_success_probability` for retry or best-of-`n` intuition.
- Use `majority_vote_success_probability` when you want to reason about self-consistency-style gains.

## Run tests

```bash
pytest modules/ml/llm/reasoning-and-test-time-compute/python -q
```
