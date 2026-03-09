import pytest

from permutation_test import permutation_test_p_value


def test_permutation_test_p_value_matches_exact_enumeration() -> None:
    p_value = permutation_test_p_value([1.0, 2.0], [4.0, 5.0])

    assert p_value == pytest.approx(1.0 / 3.0)


def test_permutation_test_p_value_is_one_for_identical_groups() -> None:
    p_value = permutation_test_p_value([1.0, 2.0], [1.0, 2.0])

    assert p_value == 1.0


def test_permutation_test_p_value_requires_non_empty_groups() -> None:
    with pytest.raises(ValueError, match="non-empty"):
        permutation_test_p_value([], [1.0])
