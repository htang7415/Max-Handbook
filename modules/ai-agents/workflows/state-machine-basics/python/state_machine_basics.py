from __future__ import annotations


EVENT_TO_STATE = {
    ("planned", "start"): "running",
    ("running", "complete"): "done",
    ("running", "block"): "blocked",
    ("blocked", "resume"): "running",
}


def valid_transition(
    current_state: str,
    next_state_name: str,
    transitions: dict[str, list[str]],
) -> bool:
    allowed = transitions.get(current_state.strip(), [])
    return next_state_name.strip() in allowed


def next_state(current_state: str, event: str) -> str:
    key = (current_state.strip(), event.strip())
    if key not in EVENT_TO_STATE:
        raise ValueError("invalid state transition")
    return EVENT_TO_STATE[key]


def transition_trace(states: list[str]) -> str:
    cleaned = [state.strip() for state in states if state.strip()]
    return " -> ".join(cleaned)
