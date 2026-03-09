import pytest

from drift_detection import drift_detected, ks_drift_score


def test_ks_drift_score_is_zero_for_identical_samples() -> None:
    score = ks_drift_score(reference=[0.0, 1.0, 2.0], current=[0.0, 1.0, 2.0])

    assert score == pytest.approx(0.0)


def test_ks_drift_score_is_large_for_disjoint_samples() -> None:
    score = ks_drift_score(reference=[0.0, 1.0, 2.0], current=[10.0, 11.0, 12.0])

    assert score == pytest.approx(1.0)


def test_drift_detected_uses_threshold() -> None:
    assert drift_detected(reference=[0.0, 1.0, 2.0], current=[10.0, 11.0, 12.0], threshold=0.5)

