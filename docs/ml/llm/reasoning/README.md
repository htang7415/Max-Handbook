# LLM Reasoning

Reasoning models spend more inference compute to improve performance on harder tasks.

## Purpose

Use this page to understand:
- what changes when a model is allowed to think longer
- when extra sampling or voting helps
- why reasoning gains cost latency and tokens

## First Principles

- Reasoning is usually an inference-time choice, not a different optimization rule at training time.
- More test-time compute can mean longer chains, more samples, or stronger aggregation.
- Extra compute only helps when the base model already has useful signal.
- Reasoning should be evaluated with task success, not just token likelihood.

## Core Math

- Total sampled token cost:
  $$
  n(P + R + A)
  $$
  where `P` is prompt tokens, `R` is reasoning tokens, `A` is answer tokens, and `n` is the number of traces.
- Best-of-`n` success:
  $$
  1 - (1 - q)^n
  $$
- Majority-vote success grows with repeated independent correct traces.

## Minimal Code Mental Model

```python
cost = total_inference_tokens(prompt_tokens, reasoning_tokens, answer_tokens, samples=4)
quality = best_of_n_success_probability(single_try_success=0.35, n=4)
vote = majority_vote_success_probability(single_try_success=0.7, n=5)
```

## Canonical Modules

- Core reasoning trade-off: `reasoning-and-test-time-compute`
- Multi-sample agreement: `vote-metrics`
- Task-level reasoning evaluation: `pass-at-k`, `answer-verification`, `answer-stability`

## When To Use What

- Start with `reasoning-and-test-time-compute` when the main question is quality versus latency or token cost.
- Use `vote-metrics` when you are sampling multiple traces and need consensus summaries.
- Use `pass-at-k` when retries matter more than one-shot exactness.
- Use `answer-verification` when the task has a strong objective checker.
