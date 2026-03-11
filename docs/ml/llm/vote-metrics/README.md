# Vote and Minority-Cluster Metrics

Vote metrics summarize how multiple sampled answers agree, disagree, or fragment into alternatives.

## Purpose

Use this guide when repeated generations produce multiple answers and you need the right summary:
- agreement and consistency
- diversity and exploration
- concentration and decisiveness
- structured disagreement in minority clusters

## First Principles

- Multiple sampled answers are useful only if you can summarize whether disagreement is noise or signal.
- Agreement metrics answer consistency questions.
- Diversity metrics answer exploration questions.
- Minority-cluster metrics answer whether alternatives form meaningful competing groups rather than random leftovers.

## Core Math

- Top-vote share:
  $$
  \max_a \frac{n_a}{N}
  $$
- Vote entropy:
  $$
  -\sum_a p_a \log p_a
  $$
- Majority-vote margin compares the top answer share against the runner-up share.

## Minimal Code Mental Model

```python
votes = tally_answers(samples)
entropy = vote_entropy(votes)
margin = majority_vote_margin(votes)
diversity = answer_uniqueness_rate(samples)
```

## Canonical Modules

- Family module: `vote-metrics`

## Supporting Modules

- `answer-stability`
- `candidate-diversity`
- `consensus-disagreement-rate`
- `majority-vote-margin`

## When To Use What

- Start with `vote-metrics` for the main agreement-versus-diversity picture.
- Use answer stability and majority-vote margin for quick self-consistency checks.
- Use uniqueness and candidate diversity when you care about exploration.
- Use minority-cluster metrics when disagreement structure matters more than just the winning answer.
- Use vote entropy when you need one compact concentration summary.

## Good Defaults

- Start with the canonical module `vote-metrics`
- Use `answer_stability` for repeated-run consistency
- Use `majority_vote_margin` plus `vote_entropy` for confidence-style summaries
- Use `answer_uniqueness_rate` for diversity
- Use `minority_cluster_entropy` when disagreement structure matters
