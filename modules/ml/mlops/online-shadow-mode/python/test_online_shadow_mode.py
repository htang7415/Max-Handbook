import pytest

from online_shadow_mode import shadow_disagreement_rate


def test_shadow_disagreement_rate_counts_mismatches() -> None:
    count, rate = shadow_disagreement_rate(
        live_predictions=["cat", "dog", "dog", "bird"],
        shadow_predictions=["cat", "cat", "dog", "bird"],
    )

    assert count == 1
    assert rate == pytest.approx(0.25)


def test_shadow_disagreement_rate_is_zero_for_identical_outputs() -> None:
    count, rate = shadow_disagreement_rate(live_predictions=[1, 0], shadow_predictions=[1, 0])

    assert count == 0
    assert rate == pytest.approx(0.0)


def test_shadow_disagreement_rate_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        shadow_disagreement_rate(live_predictions=[1], shadow_predictions=[1, 0])
