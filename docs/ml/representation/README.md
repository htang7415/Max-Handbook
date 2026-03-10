# Representation Learning

Representation learning asks how to turn raw input into geometry that makes downstream tasks easier.

## Purpose

Use this page to organize representation learning into:
- embeddings and feature spaces
- similarity geometry
- contrastive and metric-learning objectives
- transfer and reuse

## First Principles

- A representation maps input $x$ to features $z = f(x)$.
- Good representations preserve task-relevant structure and suppress nuisance variation.
- Geometry matters because retrieval, clustering, and transfer all depend on which points become close.
- Modern representation learning is mostly about useful embedding spaces, not handcrafted features alone.

## Core Math

- Embedding map:
  $$
  z = f(x)
  $$
- Cosine similarity:
  $$
  \frac{z_1^\top z_2}{\|z_1\|\|z_2\|}
  $$
- Triplet margin shape:
  $$
  \max(0, d(a,p) - d(a,n) + m)
  $$

## Minimal Code Mental Model

```python
z_anchor = encoder(anchor)
z_positive = encoder(positive)
z_negative = encoder(negative)
loss = triplet_loss(z_anchor, z_positive, z_negative)
```

## Canonical Modules

- Embeddings and features: `embeddings`, `features`, `autoencoder`
- Similarity learning: `contrastive-loss`, `triplet-loss`, `pairwise-ranking-loss`
- Reuse and structure: embedding and metric-learning guides

## Supporting Guides

- Embeddings map (`docs/ml/representation/embeddings`)
- Metric learning map (`docs/ml/representation/metric-learning`)

## When To Use What

- Start with embeddings and cosine similarity before metric-learning losses.
- Use `contrastive-loss` when you have positive and negative pairs.
- Use `triplet-loss` when anchor-positive-negative structure is explicit.
- Use `pairwise-ranking-loss` when relative ordering matters more than absolute distance.
