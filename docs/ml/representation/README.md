# Representation Learning

How models turn raw inputs into useful features.
A good representation organizes data geometry so that similarity, clustering,
and downstream tasks become simple.

## Concept

- A representation is a mapping from input $x$ to features $z = f(x)$.
- Useful representations compress nuisance variation and preserve task-relevant structure.
- The same representation can support multiple tasks via transfer learning.

## Purpose

Enable retrieval, clustering, and prediction by making “close” in feature space
match “similar” in meaning or behavior.

## Core Concepts

- Embeddings (dense vector features)
- Tokenization and vocabularies
- Feature engineering vs learned features
- Invariances and equivariances
- Bottlenecks and sparsity
- Contrastive pairs (positive / negative)
- Pairwise ranking losses for ordered preferences
- Probing and linear separability
- Transfer learning and freezing

## Math

- Dot product, cosine similarity, and normalization
- Distance metrics (Euclidean, Mahalanobis)
- PCA and SVD for linear subspaces
- Autoencoders as non-linear compression
- Contrastive objectives (InfoNCE-style)

## Key points

- Normalize embeddings when cosine similarity drives retrieval.
- Evaluate representations with downstream tasks, probing, or retrieval metrics.
- Representation quality is about geometry, not just reconstruction error.
- Watch for collapse, anisotropy, and shortcut features.

## Pitfalls

- Representation collapse (nearly constant vectors).
- Anisotropy (vectors cluster too tightly, hurting similarity search).
- Leakage or shortcuts that inflate evaluation results.
- Train / test shift that breaks learned features.

## Practice

- Compute cosine similarity across example embeddings and rank neighbors.
- Run PCA on hidden states and visualize the top components.
- Train a simple contrastive embedding and test retrieval accuracy.
- Compare pairwise-ranking loss values for preferred vs rejected scores.
