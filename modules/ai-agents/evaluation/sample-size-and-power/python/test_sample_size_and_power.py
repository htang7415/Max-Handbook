from __future__ import annotations

import pytest

from sample_size_and_power import (
    minimum_detectable_effect,
    required_sample_size,
    sample_size_route,
)


def test_sample_size_and_power_estimate_required_cases_and_mde() -> None:
    required = required_sample_size(baseline_success=0.7, effect_size=0.05)

    assert required == 1318
    assert minimum_detectable_effect(0.7, sample_size_per_variant=required) == pytest.approx(0.0499837, rel=1e-5)
    assert sample_size_route(current_samples_per_variant=900, required_samples_per_variant=required) == "collect-more"
    assert sample_size_route(current_samples_per_variant=1400, required_samples_per_variant=required) == "ready"


def test_sample_size_and_power_validation() -> None:
    with pytest.raises(ValueError):
        required_sample_size(baseline_success=1.0, effect_size=0.05)
    with pytest.raises(ValueError):
        required_sample_size(baseline_success=0.7, effect_size=0.0)
    with pytest.raises(ValueError):
        minimum_detectable_effect(0.7, sample_size_per_variant=0)
    with pytest.raises(ValueError):
        sample_size_route(current_samples_per_variant=-1, required_samples_per_variant=100)
