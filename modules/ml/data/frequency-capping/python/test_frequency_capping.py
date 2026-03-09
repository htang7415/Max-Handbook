import pytest

from frequency_capping import cap_frequencies


def test_cap_frequencies_clips_large_counts() -> None:
    capped = cap_frequencies({"click": 2, "view": 9, "share": 14}, max_count=5)

    assert capped == {"click": 2, "view": 5, "share": 5}


def test_cap_frequencies_leaves_small_counts_unchanged() -> None:
    capped = cap_frequencies({"token_a": 1, "token_b": 3}, max_count=4)

    assert capped == {"token_a": 1, "token_b": 3}


def test_cap_frequencies_requires_non_negative_counts() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        cap_frequencies({"token": -1}, max_count=3)
