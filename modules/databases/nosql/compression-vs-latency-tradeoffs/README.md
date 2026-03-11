# Compression Vs Latency Tradeoffs

> Track: `databases` | Topic: `nosql`

## Concept

Compression reduces bytes on disk and over the network, but it adds CPU work to decode data during reads. Whether it helps latency depends on whether the workload is more I/O-bound or CPU-bound.

## Key Points

- Better compression saves storage and often improves cache density.
- Smaller reads help most when I/O is the bottleneck.
- Heavy decode work can cancel out those gains for hot low-latency paths.
- This tradeoff matters in column stores, log-structured engines, and time-series systems.

## Minimal Code Mental Model

```python
summary = tradeoff_summary(
    uncompressed_mb=100.0,
    compression_ratio=0.4,
    io_ms_per_mb=2.0,
    decode_ms_per_uncompressed_mb=0.2,
)
```

## Function

```python
def compressed_size_mb(uncompressed_mb: float, compression_ratio: float) -> float:
def read_latency_ms(
    uncompressed_mb: float,
    compression_ratio: float,
    io_ms_per_mb: float,
    decode_ms_per_uncompressed_mb: float,
    compressed: bool,
) -> float:
def tradeoff_summary(
    uncompressed_mb: float,
    compression_ratio: float,
    io_ms_per_mb: float,
    decode_ms_per_uncompressed_mb: float,
) -> dict[str, float | bool]:
```

## Run tests

```bash
pytest modules/databases/nosql/compression-vs-latency-tradeoffs/python -q
```
