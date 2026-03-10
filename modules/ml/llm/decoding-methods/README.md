# Decoding Methods

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand how next-token scores become an actual generated
sequence.

## First Principles

- Decoding is the policy applied at inference time, not part of the pretrained weights.
- Greedy and beam methods emphasize high-likelihood continuations.
- Temperature, top-k, and top-p reshape or filter the candidate distribution for sampling.
- Real generation usually applies temperature first and then a sampling filter.

## Core Math

- Greedy choice:
  $$
  \arg\max_i z_i
  $$
- Temperature-scaled probabilities:
  $$
  p_i=\frac{\exp(z_i/T)}{\sum_j \exp(z_j/T)}
  $$
- Beam score:
  $$
  s(y_{1:t})=s(y_{1:t-1})+\log p(y_t\mid y_{<t})
  $$

## From Math To Code

- Scale logits by temperature first.
- Turn scaled logits into probabilities.
- Filter candidates with top-k or top-p only after that probability step.
- Use beam search only when you want sequence-level score accumulation instead of sampling.

## Minimal Code Mental Model

```python
scaled = temperature_scaled_logits(logits, temperature=0.8)
probs = temperature_probabilities(logits, temperature=0.8)
candidates = top_p_filter(probs, p=0.9)
```

## Function

```python
def greedy_choice(scores: list[float]) -> int:
def temperature_scaled_logits(logits: list[float], temperature: float) -> list[float]:
def temperature_probabilities(logits: list[float], temperature: float) -> list[float]:
def top_k_filter(probabilities: list[float], k: int) -> list[int]:
def top_p_filter(probabilities: list[float], p: float) -> list[int]:
def sampling_pipeline_candidates(
    logits: list[float],
    temperature: float,
    top_k: int,
    top_p: float,
) -> list[int]:
def beam_search_step(
    beams: list[tuple[list[int], float]],
    next_token_log_probs: list[list[float]],
    beam_width: int,
) -> list[tuple[list[int], float]]:
```

## When To Use What

- Use greedy decoding as the simplest baseline.
- Use beam search when deterministic high-likelihood continuation matters more than diversity.
- Use temperature plus top-p or top-k when you need multiple diverse but plausible generations.
- Use top-p when you want candidate count to adapt to the probability shape instead of staying fixed.

## Run tests

```bash
pytest modules/ml/llm/decoding-methods/python -q
```
