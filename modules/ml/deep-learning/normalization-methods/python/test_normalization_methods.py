import math

import pytest

from normalization_methods import (
    batch_stats,
    batchnorm,
    groupnorm,
    instancenorm,
    layernorm,
    mean_variance,
    normalize_with_stats,
    rmsnorm,
)


def test_centered_normalizers_produce_zero_mean_vectors() -> None:
    x = [1.0, 2.0, 3.0, 4.0]

    for out in (batchnorm(x), layernorm(x), instancenorm(x)):
        assert sum(out) == pytest.approx(0.0, abs=1e-6)


def test_rmsnorm_rescales_to_unit_rms() -> None:
    out = rmsnorm([1.0, -2.0, 3.0, -4.0])
    rms = math.sqrt(sum(value * value for value in out) / len(out))
    assert rms == pytest.approx(1.0, rel=1e-5)


def test_groupnorm_normalizes_each_group_independently() -> None:
    out = groupnorm([1.0, 3.0, 10.0, 14.0], groups=2)
    first_group = out[:2]
    second_group = out[2:]

    assert sum(first_group) == pytest.approx(0.0, abs=1e-6)
    assert sum(second_group) == pytest.approx(0.0, abs=1e-6)


def test_batch_stats_aggregates_rectangular_matrix() -> None:
    mean, variance = batch_stats([[1.0, 2.0], [3.0, 4.0]])

    assert mean == pytest.approx(2.5)
    assert variance == pytest.approx(1.25)


def test_mean_variance_and_normalize_with_stats_match_manual_values() -> None:
    mean, variance = mean_variance([1.0, 2.0, 3.0])
    assert mean == pytest.approx(2.0)
    assert variance == pytest.approx(2.0 / 3.0)
    out = normalize_with_stats([1.0, 2.0, 3.0], mean, variance)
    assert sum(out) == pytest.approx(0.0, abs=1e-6)


def test_invalid_groupnorm_and_batch_stats_inputs_raise() -> None:
    with pytest.raises(ValueError, match="divisible"):
        groupnorm([1.0, 2.0, 3.0], groups=2)

    with pytest.raises(ValueError, match="rectangular"):
        batch_stats([[1.0], [2.0, 3.0]])

    with pytest.raises(ValueError, match="positive"):
        normalize_with_stats([1.0, 2.0], mean=1.5, variance=0.25, eps=0.0)
