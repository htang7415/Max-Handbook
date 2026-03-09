import pytest

from target_encoding import target_encoding_map


def test_target_encoding_map_averages_targets_per_category() -> None:
    encoding = target_encoding_map(
        categories=["red", "blue", "red", "green"],
        targets=[1.0, 0.0, 0.0, 1.0],
    )

    assert encoding == pytest.approx({"red": 0.5, "blue": 0.0, "green": 1.0})


def test_target_encoding_map_returns_empty_mapping_for_no_data() -> None:
    assert target_encoding_map(categories=[], targets=[]) == {}


def test_target_encoding_map_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        target_encoding_map(categories=["red"], targets=[1.0, 0.0])
