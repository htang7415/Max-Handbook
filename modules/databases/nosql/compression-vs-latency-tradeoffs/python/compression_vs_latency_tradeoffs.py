"""compression_vs_latency_tradeoffs - smaller blocks reduce I/O but add decode work."""

from __future__ import annotations


def compressed_size_mb(uncompressed_mb: float, compression_ratio: float) -> float:
    if uncompressed_mb < 0:
        raise ValueError("uncompressed_mb must be non-negative")
    if not 0.0 < compression_ratio <= 1.0:
        raise ValueError("compression_ratio must be between 0 and 1")
    return uncompressed_mb * compression_ratio


def read_latency_ms(
    uncompressed_mb: float,
    compression_ratio: float,
    io_ms_per_mb: float,
    decode_ms_per_uncompressed_mb: float,
    compressed: bool,
) -> float:
    if compressed:
        io_cost = compressed_size_mb(uncompressed_mb, compression_ratio) * io_ms_per_mb
        decode_cost = uncompressed_mb * max(decode_ms_per_uncompressed_mb, 0.0)
        return io_cost + decode_cost
    return uncompressed_mb * io_ms_per_mb


def tradeoff_summary(
    uncompressed_mb: float,
    compression_ratio: float,
    io_ms_per_mb: float,
    decode_ms_per_uncompressed_mb: float,
) -> dict[str, float | bool]:
    compressed_mb = compressed_size_mb(uncompressed_mb, compression_ratio)
    uncompressed_latency = read_latency_ms(
        uncompressed_mb,
        compression_ratio,
        io_ms_per_mb,
        decode_ms_per_uncompressed_mb,
        compressed=False,
    )
    compressed_latency = read_latency_ms(
        uncompressed_mb,
        compression_ratio,
        io_ms_per_mb,
        decode_ms_per_uncompressed_mb,
        compressed=True,
    )
    return {
        "uncompressed_size_mb": uncompressed_mb,
        "compressed_size_mb": compressed_mb,
        "storage_saved_mb": uncompressed_mb - compressed_mb,
        "uncompressed_latency_ms": uncompressed_latency,
        "compressed_latency_ms": compressed_latency,
        "compression_wins_latency": compressed_latency <= uncompressed_latency,
    }
