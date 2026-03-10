# Data and Splitting

Data work is about preparing inputs so models learn stable signal instead of leakage, noise, or brittle shortcuts.

## Purpose

Use this page to organize the data side of ML into four parts:
- splits and leakage control
- preprocessing and feature construction
- missingness and imbalance handling
- hard-budget diagnostics such as token overflow

## First Principles

- A good split is part of the model, because it defines what “generalization” means.
- Preprocessing should be fit on training data and then reused, not relearned on every split.
- Feature construction should start simple and only become denser if the baseline misses real structure.
- Missingness, imbalance, and overflow are data problems first, not optimizer problems.

## Core Math

- Train/validation/test split:
  $$
  \mathcal{D} = \mathcal{D}_{train} \cup \mathcal{D}_{val} \cup \mathcal{D}_{test}
  $$
- Stratified sampling keeps class proportions approximately stable across splits.
- Overflow rate:
  $$
  \frac{\#\{\text{examples over budget}\}}{N}
  $$

## Minimal Code Mental Model

```python
train, val, test = stratified_split(dataset, labels)
preprocessor.fit(train)
x_train = preprocessor.transform(train)
x_val = preprocessor.transform(val)
```

## Canonical Modules

- Splits and leakage: `train-validation-test-split`, `stratified-split`, `data-leakage`
- Preprocessing: `docs/ml/data/preprocessing`
- Structured tabular features: `structured-feature-methods`
- Sparse text features: `sparse-text-feature-methods`
- Missingness and imbalance: `imputation`, `missing-indicator`, `class-imbalance`, `smote`
- Overflow and length budgets: `overflow-metrics` with the guide in `docs/ml/data/overflow-metrics`

## Supporting Modules

- Dataset vs batch vs epoch (`modules/ml/data/dataset-batch-epoch`)
- Batch iterator (`modules/ml/data/batch-iterator`)
- Polynomial feature expansion (`modules/ml/data/polynomial-features`)
- Outlier detection (`modules/ml/data/outlier-detection`)

## When To Use What

- Use stratified splits when label balance matters.
- Use the preprocessing guide before choosing specific encoders or feature transforms.
- Use sparse lexical features before heavier text pipelines when a simple baseline is enough.
- Use overflow metrics only when the system has a real token or length budget.
