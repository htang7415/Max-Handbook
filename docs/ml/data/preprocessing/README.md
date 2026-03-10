# Data Preprocessing

Preprocessing decides whether downstream models learn signal or shortcuts.

## Purpose

Use this page to choose the smallest useful preprocessing move:
- scale numeric features
- encode categorical features
- build sparse text features
- construct simple feature interactions
- handle missingness, imbalance, and hard length caps

## First Principles

- Scale features when the model is distance-based, gradient-based, or numerically unstable.
- Encode categories when IDs are informative but cannot be used as raw integers.
- Build sparse lexical features when a simple text baseline is enough.
- Add buckets or crosses when a simple model needs nonlinear thresholds or sparse interactions.
- Track missingness, imbalance, and overflow because preprocessing mistakes often dominate model quality.

## Core Math

- Standardization:
  $$
  z = \frac{x - \mu}{\sigma}
  $$
- TF-IDF:
  $$
  \mathrm{tfidf}(t, d) = \mathrm{tf}(t, d)\log\frac{N}{\mathrm{df}(t)}
  $$
- Smoothed target encoding:
  $$
  \hat{\mu}_c = \frac{\sum y_c + \alpha \mu}{n_c + \alpha}
  $$
- Truncation rate:
  $$
  \frac{\#\{\text{examples over budget}\}}{N}
  $$

## Minimal Code Mental Model

```python
preprocessor.fit(train_split)
x_train = preprocessor.transform(train_split)
x_val = preprocessor.transform(val_split)
overflow = truncation_rate(token_lengths, max_tokens=4096)
```

## Canonical Modules

- Numeric scaling: `scaling-methods`
- Categorical encoding: `categorical-encoding-methods`
- Sparse text features: `sparse-text-feature-methods`
- Structured tabular features: `structured-feature-methods`
- Missingness and repair: `imputation`, `missing-indicator`
- Imbalance and oversampling: `class-imbalance`, `smote`
- Overflow diagnostics: `token-budgeting`, `truncation-rate`, plus the overflow guide

## Supporting Guides

- Overflow metrics guide (`docs/ml/data/overflow-metrics`) with the canonical module `overflow-metrics`

## When To Use What

- Use standard or min-max scaling for linear models, distance models, and many neural inputs.
- Use robust scaling or clipping when outliers distort simple scaling.
- Use target, frequency, or WoE-style encodings for high-cardinality categories.
- Use TF-IDF, hashing, or chi-square filtering for quick lexical baselines.
- Use crosses, buckets, or entity embeddings when simple features miss interactions or category structure.
- Use missing indicators when the fact that a value is missing may itself carry signal.
- Use overflow diagnostics only when the system has a hard token or length cap.
