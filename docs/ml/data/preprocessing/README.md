# Data Preprocessing

Preprocessing decides whether downstream models learn signal or shortcuts.

## Current Anchors

- Data leakage (`modules/ml/data/data-leakage`)
- Feature scaling (`modules/ml/data/feature-scaling`)
- Robust scaling (`modules/ml/data/robust-scaling`)
- Polynomial features (`modules/ml/data/polynomial-features`)
- TF-IDF lexical features (`modules/ml/data/tf-idf`)
- Class imbalance (`modules/ml/data/class-imbalance`)
- Missing-data imputation (`modules/ml/data/imputation`)
- Missing-value indicators (`modules/ml/data/missing-indicator`)
- SMOTE-style synthetic oversampling (`modules/ml/data/smote`)
- Z-score outlier screening (`modules/ml/data/outlier-detection`)

## Concepts to Cover Well

- Scaling and normalization choices
- Robust alternatives when z-score scaling is too sensitive
- Label encoding and one-hot encoding
- Text feature extraction such as TF-IDF
- Missing-value handling and its failure modes
- Missingness indicators alongside imputation
- Outlier handling and when simple z-score rules fail
- Class imbalance remedies such as weighting, resampling, and SMOTE
