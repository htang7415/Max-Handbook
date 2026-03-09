# Data Preprocessing

Preprocessing decides whether downstream models learn signal or shortcuts.

## Current Anchors

- Data leakage (`modules/ml/data/data-leakage`)
- Feature scaling (`modules/ml/data/feature-scaling`)
- Robust scaling (`modules/ml/data/robust-scaling`)
- Feature clipping for capped numeric ranges (`modules/ml/data/feature-clipping`)
- Polynomial features (`modules/ml/data/polynomial-features`)
- Count-vector lexical baseline (`modules/ml/data/count-vectorizer`)
- TF-IDF lexical features (`modules/ml/data/tf-idf`)
- Token budgeting under fixed prompt or feature limits (`modules/ml/data/token-budgeting`)
- Truncation rate under hard token limits (`modules/ml/data/truncation-rate`)
- Overflow count beyond hard token limits (`modules/ml/data/overflow-count`)
- Hash trick for fixed-width sparse features (`modules/ml/data/hash-trick`)
- Chi-square feature scoring for sparse features (`modules/ml/data/chi-square-feature-selection`)
- Frequency encoding for categorical counts (`modules/ml/data/frequency-encoding`)
- Frequency capping for repeated sparse events (`modules/ml/data/frequency-capping`)
- Target encoding for high-cardinality categories (`modules/ml/data/target-encoding`)
- Rare-category grouping for long-tail categoricals (`modules/ml/data/rare-category-grouping`)
- Weight-of-evidence encoding (`modules/ml/data/weight-of-evidence`)
- Smoothed mean encoding (`modules/ml/data/mean-encoding-smoothing`)
- Category cross features (`modules/ml/data/category-cross-features`)
- Entity embeddings for categorical IDs (`modules/ml/data/entity-embedding-intuition`)
- Rare-token pruning for sparse vocabularies (`modules/ml/data/rare-token-pruning`)
- Feature bucketing for numeric thresholds (`modules/ml/data/feature-bucketing`)
- Class imbalance (`modules/ml/data/class-imbalance`)
- Missing-data imputation (`modules/ml/data/imputation`)
- Missing-value indicators (`modules/ml/data/missing-indicator`)
- SMOTE-style synthetic oversampling (`modules/ml/data/smote`)
- Z-score outlier screening (`modules/ml/data/outlier-detection`)

## Concepts to Cover Well

- Scaling and normalization choices
- Robust alternatives when z-score scaling is too sensitive
- Feature clipping when only the most extreme numeric values should be capped
- Label encoding and one-hot encoding
- Count vectors as the simplest bag-of-words baseline
- Text feature extraction such as TF-IDF
- Token budgeting when prompts or sparse features have hard length limits
- Truncation rate as a diagnostic for whether a length cap is too aggressive
- Overflow count as a severity metric for how much content a hard cap removes
- Vocabulary-free hashing for large sparse feature spaces
- Chi-square filtering for sparse lexical or one-hot features
- Frequency encoding as a label-free categorical baseline
- Frequency capping to stop repeated sparse events from dominating linear weights
- Target encoding and the leakage risk around per-category means
- Rare-category grouping before downstream encodings
- Weight of evidence as a supervised categorical transformation
- Smoothing category means toward the global target average
- Category crosses for sparse interaction features
- Dense entity embeddings as a learned alternative to very wide one-hot features
- Rare-token pruning before sparse lexical featurization
- Bucketizing numeric features before simple models
- Missing-value handling and its failure modes
- Missingness indicators alongside imputation
- Outlier handling and when simple z-score rules fail
- Class imbalance remedies such as weighting, resampling, and SMOTE
