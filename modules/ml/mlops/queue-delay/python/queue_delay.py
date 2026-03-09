from __future__ import annotations


def queue_delay(enqueued_at: list[float], started_at: list[float]) -> tuple[list[float], float]:
    if len(enqueued_at) != len(started_at):
        raise ValueError("enqueued_at and started_at must have the same length")
    if not enqueued_at:
        return [], 0.0

    delays: list[float] = []
    for arrival_time, service_time in zip(enqueued_at, started_at):
        if service_time < arrival_time:
            raise ValueError("started_at times must be at or after enqueued_at times")
        delays.append(service_time - arrival_time)
    return delays, sum(delays) / len(delays)
