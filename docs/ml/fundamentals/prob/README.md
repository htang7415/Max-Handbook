# Probability for ML

Probability gives models a language for uncertainty, sampling, and latent variables.

## Purpose

Use this guide to learn the probability ideas that show up repeatedly in ML:
- uncertainty and sampling
- likelihood and posterior reasoning
- divergence between distributions
- state transitions and latent uncertainty

## First Principles

- Probability is the language of uncertainty, not a list of formulas to memorize in isolation.
- Likelihood links parameters to observed data.
- Posterior reasoning updates beliefs when evidence arrives.
- Divergence measures matter because modern ML constantly compares distributions, policies, and representations.

## Core Math

- Conditional probability:
  $$
  P(A \mid B) = \frac{P(A, B)}{P(B)}
  $$
- Bayes rule:
  $$
  p(\theta \mid x) \propto p(x \mid \theta) p(\theta)
  $$
- KL divergence:
  $$
  D_{KL}(P \| Q) = \sum_x P(x)\log\frac{P(x)}{Q(x)}
  $$

## Minimal Code Mental Model

```python
posterior = normalize(likelihood * prior)
mean = expectation(values, probs)
gap = kl_divergence(p, q)
```

## Canonical Modules

- Basic distributions and sampling: `distributions`, `empirical-pmf`, `expectation`
- State and sequence uncertainty: `markov-chains`
- Distribution comparison: `kl-divergence`, `jensen-shannon-divergence`, `mutual-information`
- Bayesian updating: `beta-binomial`

## When To Use What

- Start with `distributions`, `expectation`, and `kl-divergence`.
- Use `beta-binomial` when you want the smallest concrete Bayesian update story.
- Use `markov-chains` when uncertainty evolves through state transitions.
- Use divergence modules when comparing model outputs, latent spaces, or objectives.
