# Clustering Metrics

> Track: `ml` | Topic: `evaluation`

## Purpose

Use this module to compare the main unsupervised clustering summaries:
cohesion vs separation, cluster overlap, and variance-based separation.

## First Principles

- Clustering metrics evaluate structure without ground-truth class labels.
- Silhouette compares within-cluster tightness against nearest-cluster distance.
- Davies-Bouldin penalizes clusters that are wide and not well separated.
- Calinski-Harabasz rewards large between-cluster variance relative to within-cluster variance.

## Core Math

$$
\mathrm{Silhouette} = \frac{b - a}{\max(a, b)}
$$

$$
\mathrm{DB}_{ij} = \frac{s_i + s_j}{d_{ij}},
\quad
\mathrm{CH} = \frac{B/(k-1)}{W/(n-k)}
$$

## Minimal Code Mental Model

```python
sil = silhouette_score(a=0.2, b=0.6)
db = davies_bouldin_score(s_i=0.5, s_j=0.5, d_ij=2.0)
```

## Function

```python
def silhouette_score(a: float, b: float) -> float:
def davies_bouldin_score(s_i: float, s_j: float, d_ij: float) -> float:
def calinski_harabasz_score(between_dispersion: float, within_dispersion: float, clusters: int, samples: int) -> float:
```

## When To Use What

- Use silhouette when you want an intuitive cohesion-vs-separation score.
- Use Davies-Bouldin when you want a compactness-overlap penalty.
- Use Calinski-Harabasz when you want a variance-ratio style score over the full partition.

## Run tests

```bash
pytest modules/ml/evaluation/clustering-metrics/python -q
```
