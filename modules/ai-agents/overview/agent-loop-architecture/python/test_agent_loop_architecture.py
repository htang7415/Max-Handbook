from agent_loop_architecture import choose_next_action, trace_step, update_loop_state


def test_choose_next_action_routes_to_best_tool_when_value_is_clear():
    action = choose_next_action(
        goal="summarize failed deploys",
        confidence=0.72,
        risk_score=0.2,
        remaining_steps=3,
        tool_scores={"search_logs": 0.8, "send_email": -0.4},
    )

    assert action["route"] == "tool:search_logs"
    assert action["reason"] == "tool-has-positive-value"


def test_choose_next_action_reviews_risky_or_ambiguous_steps():
    risky = choose_next_action(
        goal="send customer email",
        confidence=0.9,
        risk_score=0.8,
        remaining_steps=2,
    )
    ambiguous = choose_next_action(
        goal="inspect deployment",
        confidence=0.9,
        risk_score=0.1,
        remaining_steps=2,
        tool_scores={"search_logs": 0.50, "query_metrics": 0.45},
        min_tool_margin=0.10,
    )

    assert risky["route"] == "review"
    assert risky["reason"] == "risk-over-threshold"
    assert ambiguous["route"] == "review"
    assert ambiguous["reason"] == "tool-choice-ambiguous"


def test_state_update_and_trace_capture_loop_shape():
    state = update_loop_state({}, "tool:search_logs", "found 2 failed deploys")
    span = trace_step("step-1", state["last_route"], latency_ms=120, success=True)

    assert state["step_count"] == 1
    assert state["history"][0]["observation"] == "found 2 failed deploys"
    assert span == {
        "step_id": "step-1",
        "route": "tool:search_logs",
        "latency_ms": 120,
        "success": True,
    }
