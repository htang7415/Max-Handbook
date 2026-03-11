from speculative_decoding import speculative_decode_step
import pytest


def test_speculative_decode_step_accepts_prefix_until_mismatch():
    assert speculative_decode_step([1, 2, 3], [1, 2, 4, 5]) == [1, 2, 4]


def test_speculative_decode_step_accepts_full_draft_and_next_target_token():
    assert speculative_decode_step([1, 2], [1, 2, 7]) == [1, 2, 7]


def test_speculative_decode_step_validates_target_and_token_ids():
    with pytest.raises(ValueError, match="non-empty"):
        speculative_decode_step([], [])
    with pytest.raises(ValueError, match="non-negative"):
        speculative_decode_step([1, -1], [1, 2])
