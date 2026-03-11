from __future__ import annotations


def runnable_branches(branch_states: dict[str, str]) -> list[str]:
    return [
        branch
        for branch, state in branch_states.items()
        if branch.strip() and state.strip().lower() == "ready"
    ]


def join_ready(branch_states: dict[str, str], required: int) -> bool:
    if required <= 0:
        raise ValueError("required must be positive")
    completed = sum(1 for state in branch_states.values() if state.strip().lower() == "done")
    return completed >= required


def join_state(branch_states: dict[str, str], required: int) -> str:
    if join_ready(branch_states, required):
        return "join-ready"
    if any(state.strip().lower() == "failed" for state in branch_states.values()):
        return "blocked"
    return "waiting"
