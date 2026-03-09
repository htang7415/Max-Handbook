import pytest

from cosine_restarts import cosine_restart_lr


def test_cosine_restart_lr_starts_each_cycle_at_base_lr() -> None:
    assert cosine_restart_lr(base_lr=0.1, step=0, cycle_length=4) == pytest.approx(0.1)
    assert cosine_restart_lr(base_lr=0.1, step=4, cycle_length=4) == pytest.approx(0.1)


def test_cosine_restart_lr_decays_within_cycle() -> None:
    lr = cosine_restart_lr(base_lr=0.1, step=2, cycle_length=4)

    assert lr == pytest.approx(0.05)


def test_cosine_restart_lr_requires_positive_cycle_length() -> None:
    with pytest.raises(ValueError, match="positive"):
        cosine_restart_lr(base_lr=0.1, step=0, cycle_length=0)
