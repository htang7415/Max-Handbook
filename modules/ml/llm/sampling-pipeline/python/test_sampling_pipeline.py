import pytest

from sampling_pipeline import sampling_pipeline_candidates


def test_sampling_pipeline_candidates_apply_temperature_then_top_k_then_top_p() -> None:
    kept = sampling_pipeline_candidates([2.0, 1.0, 0.0, -1.0], temperature=1.0, top_k=3, top_p=0.8)

    assert kept == [0, 1]


def test_sampling_pipeline_candidates_keep_top_k_when_top_p_is_one() -> None:
    kept = sampling_pipeline_candidates([2.0, 1.0, 0.0], temperature=1.0, top_k=2, top_p=1.0)

    assert kept == [0, 1]


def test_sampling_pipeline_candidates_require_positive_top_k() -> None:
    with pytest.raises(ValueError, match="top_k"):
        sampling_pipeline_candidates([1.0], temperature=1.0, top_k=0, top_p=1.0)
