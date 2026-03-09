# Metrics and Evaluation

Metrics and evaluation patterns for common tasks.
Each bullet maps to a module under `modules/ml/evaluation/` unless noted.

## Classification

- Accuracy (when it fails) (`modules/ml/evaluation/accuracy`)
- Agreement rate (`modules/ml/evaluation/agreement-rate`)
- Positive rate (`modules/ml/evaluation/positive-rate`)
- Base-rate gap (`modules/ml/evaluation/base-rate-gap`)
- Prevalence ratio (`modules/ml/evaluation/prevalence-ratio`)
- Prevalence delta (`modules/ml/evaluation/prevalence-delta`)
- Risk ratio (`modules/ml/evaluation/risk-ratio`)
- Prevalence index (`modules/ml/evaluation/prevalence-index`)
- Base-rate ratio (`modules/ml/evaluation/base-rate-ratio`)
- Prevalence odds (`modules/ml/evaluation/prevalence-odds`)
- Cohen kappa (`modules/ml/evaluation/cohen-kappa`)
- Top-k accuracy (`modules/ml/evaluation/top-k-accuracy`)
- Hamming loss (`modules/ml/evaluation/hamming-loss`)
- Log loss (`modules/ml/evaluation/log-loss`)
- Macro F1 (`modules/ml/evaluation/macro-f1`)
- Balanced accuracy (`modules/ml/evaluation/balanced-accuracy`)
- Micro F1 (`modules/ml/evaluation/micro-f1`)
- Precision / Recall (`modules/ml/evaluation/precision-recall`)
- F1 (`modules/ml/evaluation/f1-score`)
- ROC-AUC (`modules/ml/evaluation/roc-auc`)
- PR-AUC (`modules/ml/evaluation/pr-auc`)
- Confusion matrix (`modules/ml/evaluation/confusion-matrix`)
- Matthews correlation coefficient (`modules/ml/evaluation/matthews-correlation`)
- Jaccard index (`modules/ml/evaluation/jaccard-index`)
- Dice score (`modules/ml/evaluation/dice-score`)
- Gini impurity (`modules/ml/evaluation/gini-impurity`)

## Clustering

- Silhouette score (`modules/ml/evaluation/silhouette-score`)
- Davies-Bouldin index (`modules/ml/evaluation/davies-bouldin`)
- Calinski-Harabasz index (`modules/ml/evaluation/calinski-harabasz`)

## Regression

- MAE vs MSE (`modules/ml/evaluation/mae-vs-mse`)
- RMSE (see `modules/ml/deep-learning/rmse-loss`)
- R2 (pitfalls) (`modules/ml/evaluation/r2-score`)

## Calibration

- Expected calibration error (`modules/ml/evaluation/expected-calibration-error`)
- Isotonic calibration (`modules/ml/evaluation/isotonic-calibration`)
- Brier score (`modules/ml/evaluation/brier-score`)

## Uncertainty

- Mean confidence intervals (`modules/ml/evaluation/confidence-intervals`)
- Bootstrap percentile intervals (`modules/ml/evaluation/bootstrap-intervals`)
- Wilson interval for binary rates (`modules/ml/evaluation/wilson-interval`)

## Statistical Testing

- Permutation test for mean difference (`modules/ml/evaluation/permutation-test`)
- Bradley-Terry pairwise probability (`modules/ml/evaluation/bradley-terry-ranking`)
- A/B test analysis for rate lift (`modules/ml/evaluation/ab-test-analysis`)
- DeLong test for paired ROC-AUC (`modules/ml/evaluation/delong-test`)

## Ranking and Retrieval

- Lift@k (`modules/ml/evaluation/lift-at-k`)
- Mean reciprocal rank (`modules/ml/evaluation/mean-reciprocal-rank`)
- NDCG (`modules/ml/evaluation/ndcg`)
- Coverage error (`modules/ml/evaluation/coverage-error`)
- Retrieval Precision@k (`modules/ml/llm/retrieval-precision-at-k`)
- Retrieval F1@k (`modules/ml/llm/retrieval-f1-at-k`)

See also:

- Calibration guide (`docs/ml/evaluation/calibration`)
