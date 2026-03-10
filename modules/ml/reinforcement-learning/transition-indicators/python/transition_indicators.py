from __future__ import annotations


def terminal_mask(done_flags: list[bool]) -> list[float]:
    return [0.0 if done else 1.0 for done in done_flags]


def continuation_mask(done_flags: list[bool]) -> list[float]:
    return terminal_mask(done_flags)


def end_of_episode_mask(done_flags: list[bool]) -> list[float]:
    return [1.0 if done else 0.0 for done in done_flags]


def done_fraction(done_flags: list[bool]) -> float:
    if not done_flags:
        return 0.0
    return sum(done_flags) / len(done_flags)


def episode_end_rate(done_flags: list[bool]) -> float:
    return done_fraction(done_flags)


def terminal_indicator(done: bool) -> float:
    return 1.0 if done else 0.0


def nonterminal_indicator(done: bool) -> float:
    return 0.0 if done else 1.0


def continuing_transition_batch(done_flags: list[bool]) -> list[float]:
    return continuation_mask(done_flags)


def persistent_transition_batch(done_flags: list[bool]) -> list[float]:
    return continuation_mask(done_flags)


def resilient_transition_batch(done_flags: list[bool]) -> list[float]:
    return continuation_mask(done_flags)
