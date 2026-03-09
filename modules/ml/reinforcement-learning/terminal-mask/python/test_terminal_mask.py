import pytest

from terminal_mask import terminal_mask


def test_terminal_mask_maps_done_flags_to_nonterminal_mask() -> None:
    mask = terminal_mask([False, True, False, True])

    assert mask == pytest.approx([1.0, 0.0, 1.0, 0.0])


def test_terminal_mask_returns_empty_list_for_empty_input() -> None:
    assert terminal_mask([]) == []


def test_terminal_mask_allows_all_nonterminal_batch() -> None:
    assert terminal_mask([False, False]) == pytest.approx([1.0, 1.0])
