import math

import pytest

from entropy_bonus import entropy_bonus


def test_entropy_bonus_scales_policy_entropy_by_coefficient() -> None:
    bonus = entropy_bonus([0.5, 0.5], coefficient=0.1)

    assert bonus == pytest.approx(0.1 * math.log(2.0))


def test_entropy_bonus_is_zero_for_deterministic_policy() -> None:
    assert entropy_bonus([1.0, 0.0], coefficient=0.3) == pytest.approx(0.0)


def test_entropy_bonus_requires_non_negative_coefficient() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        entropy_bonus([0.5, 0.5], coefficient=-0.1)
