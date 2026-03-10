from __future__ import annotations

import math

import pytest

from initialization_methods import he_normal, he_std, xavier_limit, xavier_uniform


def test_xavier_uniform_returns_expected_number_of_weights() -> None:
    assert len(xavier_uniform(2, 3, seed=1)) == 6
    assert xavier_limit(2, 3) == pytest.approx(math.sqrt(6 / 5))


def test_he_normal_returns_expected_number_of_weights() -> None:
    assert len(he_normal(2, 3, seed=1)) == 6
    assert he_std(2) == pytest.approx(1.0)


def test_initialization_helpers_validate_positive_fans() -> None:
    with pytest.raises(ValueError, match="positive"):
        xavier_limit(0, 3)
    with pytest.raises(ValueError, match="positive"):
        he_std(0)
