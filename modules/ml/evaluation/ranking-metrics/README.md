# Ranking Metrics

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module to compare ranking metrics by the question they answer:
- first-hit quality
- graded top-of-list quality
- full-label coverage
- top-prefix enrichment

## First Principles

- Ranking metrics care about order, not just whether a label appears somewhere.
- MRR focuses on the first useful hit.
- NDCG rewards good ranking near the top and supports graded relevance.
- Coverage error matters when all relevant labels eventually need to appear.
- Lift@k asks whether the top prefix is enriched compared with the base rate.

## Core Math

- MRR:
  $$
  \mathrm{MRR} = \frac{1}{Q}\sum_{q=1}^{Q}\frac{1}{\mathrm{rank}_q}
  $$
- NDCG@k:
  $$
  \mathrm{NDCG@}k = \frac{\mathrm{DCG@}k}{\mathrm{IDCG@}k}
  $$
- Lift@k:
  $$
  \mathrm{Lift@}k = \frac{\mathrm{Precision@}k}{\mathrm{BaseRate}}
  $$

## From Math To Code

- Compute discounted gain first.
- Normalize by the ideal ranking only if you want NDCG.
- Use MRR or Lift when the business question is narrower than full graded ranking quality.

## Minimal Code Mental Model

```python
dcg = dcg_at_k(relevance, k=10)
mrr = mean_reciprocal_rank(relevance_lists)
score = ndcg_at_k(relevance, k=10)
lift = lift_at_k(labels, k=100)
```

## Function

```python
def dcg_at_k(relevance: list[float], k: int) -> float:
def mean_reciprocal_rank(relevance_lists: list[list[int]]) -> float:
def ndcg_at_k(relevance: list[float], k: int) -> float:
def coverage_error(relevance_rankings: list[list[int]]) -> float:
def lift_at_k(labels: list[int], k: int) -> float:
```

## When To Use What

- Use MRR when the first correct result dominates the user experience.
- Use NDCG when relevance is graded or when early ranking quality matters most.
- Use coverage error when all relevant labels should appear eventually.
- Use Lift@k when enrichment of the top slice matters more than full recall.

## Run tests

```bash
pytest modules/ml/evaluation/ranking-metrics/python -q
```
