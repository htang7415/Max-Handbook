from __future__ import annotations


def valid_transition(
    current_state: str,
    event: str,
    transition_map: dict[tuple[str, str], str],
) -> bool:
    key = (current_state.strip(), event.strip())
    if not key[0] or not key[1]:
        raise ValueError("current_state and event must be non-empty")
    return key in transition_map


def apply_transition(
    current_state: str,
    event: str,
    transition_map: dict[tuple[str, str], str],
) -> str:
    if not valid_transition(current_state, event, transition_map):
        raise ValueError("invalid transition")
    return transition_map[(current_state.strip(), event.strip())]


def is_terminal_state(state: str, terminal_states: set[str]) -> bool:
    cleaned_state = state.strip()
    if not cleaned_state:
        raise ValueError("state must be non-empty")
    return cleaned_state in terminal_states
