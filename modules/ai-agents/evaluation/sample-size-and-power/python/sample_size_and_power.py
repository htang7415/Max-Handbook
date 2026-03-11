from __future__ import annotations

import math


def _validate_baseline_success(baseline_success: float) -> None:
    if not 0.0 < baseline_success < 1.0:
        raise ValueError("baseline_success must satisfy 0 < value < 1")


def _validate_z_value(value: float, name: str) -> None:
    if value <= 0.0:
        raise ValueError(f"{name} must be positive")


def required_sample_size(
    baseline_success: float,
    effect_size: float,
    z_alpha: float = 1.96,
    z_beta: float = 0.84,
) -> int:
    _validate_baseline_success(baseline_success)
    if effect_size <= 0.0:
        raise ValueError("effect_size must be positive")
    _validate_z_value(z_alpha, "z_alpha")
    _validate_z_value(z_beta, "z_beta")

    variance = 2.0 * baseline_success * (1.0 - baseline_success)
    z_total = z_alpha + z_beta
    return math.ceil(variance * (z_total / effect_size) ** 2)


def minimum_detectable_effect(
    baseline_success: float,
    sample_size_per_variant: int,
    z_alpha: float = 1.96,
    z_beta: float = 0.84,
) -> float:
    _validate_baseline_success(baseline_success)
    if sample_size_per_variant <= 0:
        raise ValueError("sample_size_per_variant must be positive")
    _validate_z_value(z_alpha, "z_alpha")
    _validate_z_value(z_beta, "z_beta")

    variance = 2.0 * baseline_success * (1.0 - baseline_success)
    z_total = z_alpha + z_beta
    return z_total * math.sqrt(variance / sample_size_per_variant)


def sample_size_route(current_samples_per_variant: int, required_samples_per_variant: int) -> str:
    if current_samples_per_variant < 0:
        raise ValueError("current_samples_per_variant must be non-negative")
    if required_samples_per_variant <= 0:
        raise ValueError("required_samples_per_variant must be positive")
    if current_samples_per_variant >= required_samples_per_variant:
        return "ready"
    return "collect-more"
