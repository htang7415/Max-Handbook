from __future__ import annotations


def throughput_per_dollar(requests_per_second: float, dollars_per_hour: float) -> float:
    if requests_per_second < 0.0:
        raise ValueError("requests_per_second must be non-negative")
    if dollars_per_hour <= 0.0:
        raise ValueError("dollars_per_hour must be positive")

    return requests_per_second * 3600.0 / dollars_per_hour
