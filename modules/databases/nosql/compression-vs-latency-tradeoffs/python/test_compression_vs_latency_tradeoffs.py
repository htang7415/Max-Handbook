import pytest

from compression_vs_latency_tradeoffs import tradeoff_summary


def test_compression_can_win_when_io_is_expensive_and_decode_is_cheap() -> None:
    assert tradeoff_summary(
        uncompressed_mb=100.0,
        compression_ratio=0.4,
        io_ms_per_mb=2.0,
        decode_ms_per_uncompressed_mb=0.2,
    ) == {
        "uncompressed_size_mb": 100.0,
        "compressed_size_mb": 40.0,
        "storage_saved_mb": 60.0,
        "uncompressed_latency_ms": 200.0,
        "compressed_latency_ms": 100.0,
        "compression_wins_latency": True,
    }


def test_compression_can_lose_when_io_is_cheap_but_decode_is_heavy() -> None:
    summary = tradeoff_summary(
        uncompressed_mb=100.0,
        compression_ratio=0.4,
        io_ms_per_mb=0.1,
        decode_ms_per_uncompressed_mb=0.5,
    )

    assert summary["uncompressed_latency_ms"] == 10.0
    assert summary["compressed_latency_ms"] == 54.0
    assert summary["compression_wins_latency"] is False


def test_invalid_compression_ratio_is_rejected() -> None:
    with pytest.raises(ValueError):
        tradeoff_summary(100.0, 0.0, 2.0, 0.1)
