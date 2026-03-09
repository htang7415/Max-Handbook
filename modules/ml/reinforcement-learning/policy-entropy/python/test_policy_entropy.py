import math

import pytest

from policy_entropy import policy_entropy


def test_policy_entropy_is_zero_for_deterministic_policy() -> None:
    assert policy_entropy([1.0, 0.0, 0.0]) == pytest.approx(0.0)


def test_policy_entropy_matches_uniform_binary_policy() -> None:
    assert policy_entropy([0.5, 0.5]) == pytest.approx(math.log(2.0))


def test_policy_entropy_requires_probabilities_to_sum_to_one() -> None:
    with pytest.raises(ValueError, match="sum to 1"):
        policy_entropy([0.5, 0.4])
