# Data and Splitting

Reliable data setup, preprocessing, and evaluation splits.
Each bullet maps to a module under `modules/ml/data/`.

## Concepts

- Dataset vs batch vs epoch (`modules/ml/data/dataset-batch-epoch`)
- Batch iterator (`modules/ml/data/batch-iterator`)
- Train / validation / test split (`modules/ml/data/train-validation-test-split`)
- Stratified split (`modules/ml/data/stratified-split`)
- Data leakage (common failure modes) (`modules/ml/data/data-leakage`)
- Feature scaling (`modules/ml/data/feature-scaling`)
- Robust scaling (`modules/ml/data/robust-scaling`)
- Feature clipping (`modules/ml/data/feature-clipping`)
- Polynomial feature expansion (`modules/ml/data/polynomial-features`)
- Count vectorizer (`modules/ml/data/count-vectorizer`)
- TF-IDF lexical features (`modules/ml/data/tf-idf`)
- Token budgeting under fixed length limits (`modules/ml/data/token-budgeting`)
- Truncation rate under hard length caps (`modules/ml/data/truncation-rate`)
- Overflow count beyond hard length caps (`modules/ml/data/overflow-count`)
- Hash trick for sparse features (`modules/ml/data/hash-trick`)
- Chi-square feature scoring (`modules/ml/data/chi-square-feature-selection`)
- Frequency encoding for categorical features (`modules/ml/data/frequency-encoding`)
- Frequency capping for sparse counts (`modules/ml/data/frequency-capping`)
- Target encoding for categorical features (`modules/ml/data/target-encoding`)
- Rare-category grouping (`modules/ml/data/rare-category-grouping`)
- Weight of evidence (`modules/ml/data/weight-of-evidence`)
- Mean encoding smoothing (`modules/ml/data/mean-encoding-smoothing`)
- Category cross features (`modules/ml/data/category-cross-features`)
- Entity embedding intuition (`modules/ml/data/entity-embedding-intuition`)
- Rare-token pruning (`modules/ml/data/rare-token-pruning`)
- Feature bucketing (`modules/ml/data/feature-bucketing`)
- Handling class imbalance (`modules/ml/data/class-imbalance`)
- Missing-data imputation (`modules/ml/data/imputation`)
- Missing-value indicators (`modules/ml/data/missing-indicator`)
- SMOTE-style synthetic oversampling (`modules/ml/data/smote`)
- Z-score outlier screening (`modules/ml/data/outlier-detection`)

See also:

- Preprocessing map (`docs/ml/data/preprocessing`)
