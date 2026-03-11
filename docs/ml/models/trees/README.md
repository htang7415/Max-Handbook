# Trees and Ensembles

Tree-based models dominate many tabular problems because they capture nonlinear structure with limited preprocessing.

## Purpose

Use this guide to route the main tree ideas:
- split quality
- bagging and variance reduction
- boosting and residual fitting
- anomaly detection with tree structure

## First Principles

- Trees win when threshold effects and feature interactions matter.
- Bagging reduces variance by averaging many unstable learners.
- Boosting improves fit by correcting current errors stage by stage.
- Tabular problems often reward tree structure before deep models.

## Core Math

- Split quality uses impurity or loss reduction.
- Bagging averages many fitted trees.
- Boosting adds a stage update:
  $$
  \hat{y}' = \hat{y} + \eta h
  $$

## Minimal Code Mental Model

```python
impurity = gini_impurity(labels)
bagged = bootstrap_indices(n=100, seed=0)
updated, residuals = gradient_boosting_step(y, pred, weak_output, learning_rate=0.1)
```

## Canonical Modules

- Family module: `tree-ensemble-methods`
- Supporting module: `isolation-forest`

## When To Use What

- Start with `tree-ensemble-methods` for impurity, bagging, boosting, and XGBoost-style gain.
- Use `isolation-forest` when anomaly detection is the real problem.
- Prefer tree ensembles over linear models when threshold effects and feature interactions dominate.
- Move back to the data section if feature leakage or preprocessing is the real issue.
