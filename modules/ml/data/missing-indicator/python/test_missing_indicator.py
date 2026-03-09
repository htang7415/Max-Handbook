import pytest

from missing_indicator import missing_indicators


def test_missing_indicators_mark_none_entries() -> None:
    indicators = missing_indicators([[1.0, None], [None, 2.0]])

    assert indicators == [[0, 1], [1, 0]]


def test_missing_indicators_return_empty_for_empty_table() -> None:
    assert missing_indicators([]) == []


def test_missing_indicators_require_rectangular_table() -> None:
    with pytest.raises(ValueError, match="same length"):
        missing_indicators([[1.0], [1.0, None]])
