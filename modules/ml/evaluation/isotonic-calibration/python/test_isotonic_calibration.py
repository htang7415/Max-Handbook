import pytest

from isotonic_calibration import isotonic_calibration


def test_isotonic_calibration_pools_adjacent_violations() -> None:
    calibrated = isotonic_calibration([0.1, 0.4, 0.8], [1, 0, 1])

    assert calibrated == pytest.approx([0.5, 0.5, 1.0])


def test_isotonic_calibration_restores_original_order() -> None:
    calibrated = isotonic_calibration([0.8, 0.1, 0.4], [1, 1, 0])

    assert calibrated == pytest.approx([1.0, 0.5, 0.5])


def test_isotonic_calibration_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="binary"):
        isotonic_calibration([0.1], [2])
