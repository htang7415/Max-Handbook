from __future__ import annotations

from initialization_methods import he_normal, xavier_uniform


def test_xavier_uniform_returns_expected_number_of_weights() -> None:
    assert len(xavier_uniform(2, 3, seed=1)) == 6


def test_he_normal_returns_expected_number_of_weights() -> None:
    assert len(he_normal(2, 3, seed=1)) == 6
