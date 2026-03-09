import pytest

from one_cycle_schedule import one_cycle_lr


def test_one_cycle_lr_starts_from_divided_learning_rate() -> None:
    lr = one_cycle_lr(max_lr=0.1, step=0, total_steps=10)

    assert lr == pytest.approx(0.004)


def test_one_cycle_lr_reaches_peak_at_end_of_up_phase() -> None:
    lr = one_cycle_lr(max_lr=0.1, step=2, total_steps=10)

    assert lr == pytest.approx(0.1)


def test_one_cycle_lr_anneals_to_tiny_final_value() -> None:
    lr = one_cycle_lr(max_lr=0.1, step=9, total_steps=10)

    assert lr == pytest.approx(4.0e-7)


def test_one_cycle_lr_requires_valid_pct_start() -> None:
    with pytest.raises(ValueError, match="pct_start"):
        one_cycle_lr(max_lr=0.1, step=0, total_steps=10, pct_start=1.0)
