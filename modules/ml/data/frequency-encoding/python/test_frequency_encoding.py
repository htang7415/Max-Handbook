import pytest

from frequency_encoding import frequency_encoding_map


def test_frequency_encoding_map_returns_relative_frequencies() -> None:
    encoding = frequency_encoding_map(["red", "blue", "red", "green"])

    assert encoding == pytest.approx({"red": 0.5, "blue": 0.25, "green": 0.25})


def test_frequency_encoding_map_returns_empty_mapping_for_no_data() -> None:
    assert frequency_encoding_map([]) == {}


def test_frequency_encoding_map_sums_to_one() -> None:
    encoding = frequency_encoding_map(["a", "a", "b"])

    assert sum(encoding.values()) == pytest.approx(1.0)
