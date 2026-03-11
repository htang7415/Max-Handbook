from __future__ import annotations

import pytest

from confidence_calibration import (
    calibration_gap,
    calibration_route,
    mean_confidence,
    observed_accuracy,
)


def test_confidence_calibration_measures_alignment_between_confidence_and_accuracy() -> None:
    confidence = mean_confidence([0.9, 0.8, 0.7])
    accuracy = observed_accuracy([True, True, False])

    assert confidence == pytest.approx(0.8)
    assert accuracy == pytest.approx(2 / 3)
    assert calibration_gap(confidence, accuracy) == pytest.approx(0.1333333333)
    assert calibration_route(confidence, accuracy, max_gap=0.15, min_accuracy=0.6) == "pass"


def test_confidence_calibration_reviews_low_accuracy_or_large_gap() -> None:
    assert calibration_route(0.9, 0.6, max_gap=0.1, min_accuracy=0.7) == "review"
    assert calibration_route(0.95, 0.75, max_gap=0.1, min_accuracy=0.7) == "review"


def test_confidence_calibration_validation() -> None:
    with pytest.raises(ValueError):
        mean_confidence([])
    with pytest.raises(ValueError):
        mean_confidence([1.1])
    with pytest.raises(ValueError):
        observed_accuracy([])
    with pytest.raises(ValueError):
        calibration_route(0.8, 0.7, max_gap=-0.1, min_accuracy=0.7)
