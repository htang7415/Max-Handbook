import pytest

from canary_rollout import next_canary_share


def test_canary_rollout_advances_when_metric_is_healthy() -> None:
    share = next_canary_share(current_share=0.1, step=0.2, error_rate=0.01, threshold=0.02)

    assert share == pytest.approx(0.3)


def test_canary_rollout_rolls_back_when_metric_breaches_threshold() -> None:
    share = next_canary_share(current_share=0.4, step=0.1, error_rate=0.05, threshold=0.02)

    assert share == pytest.approx(0.3)


def test_canary_rollout_caps_at_full_rollout() -> None:
    share = next_canary_share(current_share=0.95, step=0.1, error_rate=0.0, threshold=0.02)

    assert share == pytest.approx(1.0)
