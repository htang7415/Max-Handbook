from __future__ import annotations


def all_steps_done(plan: list[dict[str, object]]) -> bool:
    if not plan:
        return False
    return all(bool(item.get("done", False)) for item in plan)


def stop_due_to_blockers(blockers: list[str]) -> bool:
    return any(blocker.strip() for blocker in blockers)


def stop_decision(plan: list[dict[str, object]], blockers: list[str], needs_review: bool) -> str:
    if all_steps_done(plan):
        return "done"
    if needs_review:
        return "review"
    if stop_due_to_blockers(blockers):
        return "blocked"
    return "continue"
