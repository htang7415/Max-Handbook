from __future__ import annotations


def end_of_episode_mask(done_flags: list[bool]) -> list[float]:
    return [1.0 if done else 0.0 for done in done_flags]
