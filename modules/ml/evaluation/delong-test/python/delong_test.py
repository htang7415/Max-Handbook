from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class DeLongResult:
    auc_a: float
    auc_b: float
    auc_difference: float
    z_score: float
    p_value: float


def _pair_score(positive_score: float, negative_score: float) -> float:
    if positive_score > negative_score:
        return 1.0
    if positive_score == negative_score:
        return 0.5
    return 0.0


def _sample_variance(values: list[float]) -> float:
    if len(values) <= 1:
        return 0.0
    mean = sum(values) / len(values)
    return sum((value - mean) ** 2 for value in values) / (len(values) - 1)


def _auc_components(positive_scores: list[float], negative_scores: list[float]) -> tuple[float, list[float], list[float]]:
    v10: list[float] = []
    for positive_score in positive_scores:
        v10.append(
            sum(_pair_score(positive_score, negative_score) for negative_score in negative_scores) / len(negative_scores)
        )

    v01: list[float] = []
    for negative_score in negative_scores:
        v01.append(
            sum(_pair_score(positive_score, negative_score) for positive_score in positive_scores) / len(positive_scores)
        )

    auc = sum(v10) / len(v10)
    return auc, v10, v01


def delong_auc_test(labels: list[int], scores_a: list[float], scores_b: list[float]) -> DeLongResult:
    if len(labels) != len(scores_a) or len(labels) != len(scores_b):
        raise ValueError("labels, scores_a, and scores_b must have the same length")
    if not labels:
        raise ValueError("labels must be non-empty")
    if any(label not in (0, 1) for label in labels):
        raise ValueError("labels must be binary")

    positive_indices = [index for index, label in enumerate(labels) if label == 1]
    negative_indices = [index for index, label in enumerate(labels) if label == 0]

    if not positive_indices or not negative_indices:
        raise ValueError("labels must contain both positive and negative examples")

    positive_scores_a = [scores_a[index] for index in positive_indices]
    negative_scores_a = [scores_a[index] for index in negative_indices]
    positive_scores_b = [scores_b[index] for index in positive_indices]
    negative_scores_b = [scores_b[index] for index in negative_indices]

    auc_a, v10_a, v01_a = _auc_components(positive_scores_a, negative_scores_a)
    auc_b, v10_b, v01_b = _auc_components(positive_scores_b, negative_scores_b)

    v10_diff = [component_a - component_b for component_a, component_b in zip(v10_a, v10_b)]
    v01_diff = [component_a - component_b for component_a, component_b in zip(v01_a, v01_b)]
    variance = _sample_variance(v10_diff) / len(v10_diff) + _sample_variance(v01_diff) / len(v01_diff)
    auc_difference = auc_a - auc_b

    if variance <= 0.0:
        z_score = 0.0
        p_value = 1.0
    else:
        z_score = auc_difference / math.sqrt(variance)
        p_value = math.erfc(abs(z_score) / math.sqrt(2.0))

    return DeLongResult(
        auc_a=auc_a,
        auc_b=auc_b,
        auc_difference=auc_difference,
        z_score=z_score,
        p_value=p_value,
    )
