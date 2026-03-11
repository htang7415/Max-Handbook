import pytest

from kv_cache import kv_cache_bytes, kv_cache_gib


def test_kv_cache_bytes():
    assert kv_cache_bytes(
        num_layers=2,
        num_tokens=4,
        num_kv_heads=8,
        head_dim=16,
        bytes_per_element=2,
        batch_size=1,
    ) == 4096


def test_kv_cache_gib_is_consistent_with_bytes() -> None:
    bytes_used = kv_cache_bytes(2, 4, 8, 16, 2, batch_size=1)
    assert kv_cache_gib(2, 4, 8, 16, 2, batch_size=1) == pytest.approx(bytes_used / (1024**3))


def test_kv_cache_requires_positive_inputs() -> None:
    with pytest.raises(ValueError, match="positive"):
        kv_cache_bytes(0, 4, 8, 16, 2)
