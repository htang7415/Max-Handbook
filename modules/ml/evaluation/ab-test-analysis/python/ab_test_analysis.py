from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class ABTestResult:
    control_rate: float
    treatment_rate: float
    relative_lift: float
    z_score: float
    p_value: float


def ab_test_analysis(
    control_conversions: int,
    control_trials: int,
    treatment_conversions: int,
    treatment_trials: int,
) -> ABTestResult:
    if control_trials <= 0 or treatment_trials <= 0:
        raise ValueError("trial counts must be positive")
    if not 0 <= control_conversions <= control_trials:
        raise ValueError("control_conversions must satisfy 0 <= conversions <= trials")
    if not 0 <= treatment_conversions <= treatment_trials:
        raise ValueError("treatment_conversions must satisfy 0 <= conversions <= trials")

    control_rate = control_conversions / control_trials
    treatment_rate = treatment_conversions / treatment_trials
    pooled_rate = (control_conversions + treatment_conversions) / (control_trials + treatment_trials)
    standard_error = math.sqrt(
        pooled_rate * (1.0 - pooled_rate) * (1.0 / control_trials + 1.0 / treatment_trials)
    )

    if standard_error == 0.0:
        z_score = 0.0
        p_value = 1.0
    else:
        z_score = (treatment_rate - control_rate) / standard_error
        p_value = math.erfc(abs(z_score) / math.sqrt(2.0))

    if control_rate == 0.0:
        relative_lift = 0.0 if treatment_rate == 0.0 else math.inf
    else:
        relative_lift = (treatment_rate - control_rate) / control_rate

    return ABTestResult(
        control_rate=control_rate,
        treatment_rate=treatment_rate,
        relative_lift=relative_lift,
        z_score=z_score,
        p_value=p_value,
    )
