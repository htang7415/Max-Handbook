import pytest

from feature_clipping import clip_features


def test_clip_features_caps_values_outside_bounds() -> None:
    clipped = clip_features([-10.0, -1.0, 2.0, 9.0], min_value=0.0, max_value=5.0)

    assert clipped == pytest.approx([0.0, 0.0, 2.0, 5.0])


def test_clip_features_leaves_interior_values_unchanged() -> None:
    clipped = clip_features([1.5, 2.5, 3.5], min_value=1.0, max_value=4.0)

    assert clipped == pytest.approx([1.5, 2.5, 3.5])


def test_clip_features_requires_ordered_bounds() -> None:
    with pytest.raises(ValueError, match="less than or equal"):
        clip_features([1.0], min_value=3.0, max_value=2.0)
