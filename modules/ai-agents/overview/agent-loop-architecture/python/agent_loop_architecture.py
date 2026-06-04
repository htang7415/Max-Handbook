from __future__ import annotations


def _require_unit_interval(name: str, value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must satisfy 0 <= value <= 1")
    return value


def choose_next_action(
    goal: str,
    confidence: float,
    risk_score: float,
    remaining_steps: int,
    tool_scores: dict[str, float] | None = None,
    blocked: bool = False,
    min_confidence: float = 0.7,
    max_risk: float = 0.6,
    min_tool_margin: float = 0.15,
) -> dict[str, object]:
    goal = goal.strip()
    if not goal:
        raise ValueError("goal must be non-empty")
    confidence = _require_unit_interval("confidence", confidence)
    risk_score = _require_unit_interval("risk_score", risk_score)
    min_confidence = _require_unit_interval("min_confidence", min_confidence)
    max_risk = _require_unit_interval("max_risk", max_risk)
    if remaining_steps < 0:
        raise ValueError("remaining_steps must be non-negative")
    if min_tool_margin < 0.0:
        raise ValueError("min_tool_margin must be non-negative")

    if blocked:
        return {"route": "block", "reason": "blocked", "goal": goal}
    if remaining_steps == 0:
        return {"route": "stop", "reason": "budget-exhausted", "goal": goal}
    if risk_score > max_risk:
        return {"route": "review", "reason": "risk-over-threshold", "goal": goal}

    ranked_tools = sorted(
        (tool_scores or {}).items(),
        key=lambda item: (-float(item[1]), item[0]),
    )
    if ranked_tools and ranked_tools[0][1] > 0.0:
        second_score = ranked_tools[1][1] if len(ranked_tools) > 1 else float("-inf")
        if second_score != float("-inf") and ranked_tools[0][1] - second_score < min_tool_margin:
            return {"route": "review", "reason": "tool-choice-ambiguous", "goal": goal}
        return {
            "route": f"tool:{ranked_tools[0][0]}",
            "reason": "tool-has-positive-value",
            "goal": goal,
        }

    if confidence < min_confidence:
        return {"route": "review", "reason": "low-confidence", "goal": goal}
    return {"route": "answer", "reason": "confidence-sufficient", "goal": goal}


def update_loop_state(state: dict[str, object], route: str, observation: str) -> dict[str, object]:
    route = route.strip()
    observation = observation.strip()
    if not route:
        raise ValueError("route must be non-empty")
    if not observation:
        raise ValueError("observation must be non-empty")

    history = list(state.get("history", []))
    history.append({"route": route, "observation": observation})
    return {
        **state,
        "last_route": route,
        "history": history,
        "step_count": len(history),
    }


def trace_step(step_id: str, route: str, latency_ms: int, success: bool) -> dict[str, object]:
    step_id = step_id.strip()
    route = route.strip()
    if not step_id:
        raise ValueError("step_id must be non-empty")
    if not route:
        raise ValueError("route must be non-empty")
    if latency_ms < 0:
        raise ValueError("latency_ms must be non-negative")
    return {
        "step_id": step_id,
        "route": route,
        "latency_ms": latency_ms,
        "success": bool(success),
    }
