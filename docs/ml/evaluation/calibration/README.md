# Calibration

Calibration asks whether model confidence matches empirical correctness.

## Current Anchors

- Expected calibration error (`modules/ml/evaluation/expected-calibration-error`)
- Isotonic calibration (`modules/ml/evaluation/isotonic-calibration`)
- Confusion matrix (`modules/ml/evaluation/confusion-matrix`)
- Precision / Recall (`modules/ml/evaluation/precision-recall`)
- ROC-AUC (`modules/ml/evaluation/roc-auc`)

## Concepts to Cover Well

- Confidence vs accuracy
- Thresholding vs ranking quality
- Reliability diagrams and expected calibration error
- Monotonic post-hoc calibration with isotonic regression
- Why a high-AUC model can still be badly calibrated
