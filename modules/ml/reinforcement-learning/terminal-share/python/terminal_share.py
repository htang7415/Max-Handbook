from __future__ import annotations


def terminal_share(done_flags: list[bool]) -> float:
    if not done_flags:
        return 0.0
    return sum(done_flags) / len(done_flags)
