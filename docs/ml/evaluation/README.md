# Metrics and Evaluation

Metrics and evaluation patterns for common tasks.
Each bullet maps to a module under `modules/ml/evaluation/` unless noted.

## Classification

- Accuracy (when it fails) (`modules/ml/evaluation/accuracy`)
- Precision / Recall (`modules/ml/evaluation/precision-recall`)
- F1 (`modules/ml/evaluation/f1-score`)
- ROC-AUC (`modules/ml/evaluation/roc-auc`)
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

## Uncertainty

- Mean confidence intervals (`modules/ml/evaluation/confidence-intervals`)
- Bootstrap percentile intervals (`modules/ml/evaluation/bootstrap-intervals`)

## Statistical Testing

- Permutation test for mean difference (`modules/ml/evaluation/permutation-test`)
- Bradley-Terry pairwise probability (`modules/ml/evaluation/bradley-terry-ranking`)

See also:

- Calibration guide (`docs/ml/evaluation/calibration`)
