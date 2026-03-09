import pytest

from continuation_mask import continuation_mask


def test_continuation_mask_maps_done_flags_to_continuation_mask() -> None:
    mask = continuation_mask([False, True, False, True])

    assert mask == pytest.approx([1.0, 0.0, 1.0, 0.0])


def test_continuation_mask_returns_empty_list_for_empty_input() -> None:
    assert continuation_mask([]) == []


def test_continuation_mask_allows_all_continuing_batch() -> None:
    assert continuation_mask([False, False]) == pytest.approx([1.0, 1.0])
