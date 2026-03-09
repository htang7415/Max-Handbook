import pytest

from end_of_episode_mask import end_of_episode_mask


def test_end_of_episode_mask_maps_done_flags_to_terminal_mask() -> None:
    mask = end_of_episode_mask([False, True, False, True])

    assert mask == pytest.approx([0.0, 1.0, 0.0, 1.0])


def test_end_of_episode_mask_returns_empty_list_for_empty_input() -> None:
    assert end_of_episode_mask([]) == []


def test_end_of_episode_mask_allows_all_terminal_batch() -> None:
    assert end_of_episode_mask([True, True]) == pytest.approx([1.0, 1.0])
