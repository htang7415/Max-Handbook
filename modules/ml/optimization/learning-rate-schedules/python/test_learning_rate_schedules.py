from __future__ import annotations

import pytest

from learning_rate_schedules import (
    constant_lr,
    cosine_decay,
    cosine_decay_factor,
    cosine_restart_lr,
    exp_decay,
    one_cycle_lr,
    step_decay,
    warmup_factor,
    warmup_cosine_lr,
    warmup_lr,
)


def test_constant_step_and_exponential_decay_cover_basic_schedule_shapes() -> None:
    assert constant_lr(0.1) == pytest.approx(0.1)
    assert step_decay(0.1, 10, 0.5, 10) == pytest.approx(0.05)
    assert exp_decay(0.1, 0.0, 10) == pytest.approx(0.1)


def test_cosine_family_schedules_decay_smoothly() -> None:
    assert cosine_decay_factor(0, 10) == pytest.approx(1.0)
    assert cosine_decay(1.0, 10, 10) == pytest.approx(0.0)
    assert cosine_restart_lr(0.1, 0, 4) == pytest.approx(0.1)
    assert warmup_cosine_lr(1.0, 2, 4, 10) == pytest.approx(0.5)


def test_warmup_and_one_cycle_capture_common_modern_patterns() -> None:
    assert warmup_factor(5, 10) == pytest.approx(0.5)
    assert warmup_lr(1.0, 5, 10) == pytest.approx(0.5)
    assert one_cycle_lr(0.1, 0, 10) == pytest.approx(0.004)


def test_schedule_validation_rejects_invalid_shapes() -> None:
    with pytest.raises(ValueError):
        cosine_restart_lr(0.1, 0, 0)
    with pytest.raises(ValueError):
        one_cycle_lr(0.1, 0, 10, pct_start=1.0)
