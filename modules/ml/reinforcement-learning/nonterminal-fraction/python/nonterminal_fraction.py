from __future__ import annotations


def nonterminal_fraction(done_flags: list[bool]) -> float:
    if not done_flags:
        return 0.0
    return sum(not done for done in done_flags) / len(done_flags)
