import pytest

from rare_token_pruning import prune_rare_tokens


def test_prune_rare_tokens_replaces_infrequent_tokens() -> None:
    pruned = prune_rare_tokens(tokens=["a", "b", "a", "c"], min_count=2)

    assert pruned == ["a", "__UNK__", "a", "__UNK__"]


def test_prune_rare_tokens_keeps_frequent_tokens() -> None:
    pruned = prune_rare_tokens(tokens=["x", "x", "y", "y"], min_count=2)

    assert pruned == ["x", "x", "y", "y"]


def test_prune_rare_tokens_requires_positive_threshold() -> None:
    with pytest.raises(ValueError, match="positive"):
        prune_rare_tokens(tokens=["a"], min_count=0)
