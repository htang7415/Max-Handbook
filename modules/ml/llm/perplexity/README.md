# Perplexity

> Track: `ml` | Topic: `llm`

## Purpose

Use this module to understand how language-model likelihood becomes a single
intrinsic evaluation number.

## First Principles

- Perplexity measures how surprised the model is by the true next tokens.
- Lower perplexity means the model assigned higher probability to the observed sequence.
- Perplexity is useful for language modeling comparisons, but it is not a full task metric.
- Tokenization and evaluation setup can change perplexity a lot.

## Core Math

Mean negative log-likelihood:

$$
\mathrm{NLL} = - \frac{1}{n} \sum_{i=1}^{n} \log p_i
$$

$$
\mathrm{PPL} = \exp(\mathrm{NLL})
$$

- $n$ -- number of tokens
- $p_i$ -- probability assigned to the correct token at position $i$

## From Math To Code

- Average the token-level negative log probabilities first.
- Exponentiate that average to get perplexity.

## Minimal Code Mental Model

```python
nll = mean_negative_log_likelihood(token_probs)
score = perplexity(token_probs)
```

## Function

```python
def mean_negative_log_likelihood(token_probs: list[float]) -> float:
def perplexity(token_probs: list[float]) -> float:
```

## When To Use What

- Use perplexity for pretraining-style language modeling comparisons.
- Do not use perplexity alone to judge downstream QA, reasoning, or product usefulness.
- Compare perplexity only when tokenization and evaluation setup are matched.

## Run tests

```bash
pytest modules/ml/llm/perplexity/python -q
```
