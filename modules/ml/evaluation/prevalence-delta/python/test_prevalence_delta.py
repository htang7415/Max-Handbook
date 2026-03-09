import pytest

from prevalence_delta import prevalence_delta


def test_prevalence_delta_returns_signed_change_from_baseline_to_comparison() -> None:
    delta = prevalence_delta([1, 0, 0, 1], [1, 1, 1, 0])

    assert delta == pytest.approx(0.25)


def test_prevalence_delta_handles_empty_groups_as_zero_rate() -> None:
    assert prevalence_delta([], [1, 0]) == pytest.approx(0.5)


def test_prevalence_delta_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        prevalence_delta([1, 2], [0, 1])
