# Models and Classical ML

Classical ML is still the fastest path to good baselines, interpretable behavior, and small-data wins.

## Purpose

Use this page to choose the right model family before reaching for deeper systems:
- linear models
- tree and ensemble models
- nearest-neighbor and clustering models
- probabilistic models
- dimensionality reduction

## First Principles

- Linear models work well when the signal is mostly additive after good preprocessing.
- Tree models win when interactions and thresholds matter but data is still structured.
- Distance-based methods depend heavily on scaling and representation.
- Probabilistic models are useful when distributions or uncertainty assumptions matter.
- Dimensionality reduction helps when geometry matters more than raw feature count.

## Core Math

- Linear model:
  $$
  \hat{y} = w^\top x + b
  $$
- Logistic model:
  $$
  p(y=1 \mid x) = \sigma(w^\top x + b)
  $$
- Tree split objective is usually impurity or loss reduction.
- EM-style mixture models alternate between soft assignment and parameter re-estimation.

## Minimal Code Mental Model

```python
model.fit(x_train, y_train)
pred = model.predict(x_val)
score = evaluate(pred, y_val)
```

## Canonical Modules

- Linear models: `linear-models`
- Trees and ensembles: `decision-trees`, `random-forest`, `gradient-boosting`, `xgboost-objective`, `adaboost`
- Clustering and neighbors: `knn`, `k-means`, `dbscan`, `gaussian-mixture-model-em`
- Probabilistic baselines: `naive-bayes-models`, `gaussian-process-regression`
- Dimensionality reduction: `kernel-pca`, `lle`, `tsne-gradient`, `bic-aic`

## Supporting Guides

- Linear-model map (`docs/ml/models/linear`)
- Tree and ensemble map (`docs/ml/models/trees`)

## When To Use What

- Start with linear models when you want a strong, fast baseline.
- Use trees or boosting when nonlinear thresholds and feature interactions matter.
- Use clustering and neighbor methods when geometry is part of the task.
- Use probabilistic models when assumptions about distributions are actually helpful.
- Use dimensionality reduction when you need structure, visualization, or compressed features.
