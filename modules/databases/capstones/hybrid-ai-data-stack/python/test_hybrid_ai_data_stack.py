from hybrid_ai_data_stack import route_data_request, release_gate, stack_readiness


def test_route_data_request_prioritizes_correctness_before_copies():
    assert route_data_request(
        needs_transaction=True,
        needs_similarity=True,
        needs_large_scan=True,
    ) == "source-of-truth"
    assert route_data_request(
        needs_transaction=False,
        needs_similarity=True,
        needs_large_scan=True,
    ) == "retrieval-layer"
    assert route_data_request(
        needs_transaction=False,
        needs_similarity=False,
        needs_large_scan=True,
    ) == "analytics-layer"


def test_stack_readiness_and_release_gate_ship_when_checks_pass():
    readiness = stack_readiness(
        {
            "source_constraints": True,
            "cdc_watermark_fresh": True,
            "analytics_backfill_ready": True,
            "retrieval_permissions_filtered": True,
            "retrieval_eval_passed": True,
        }
    )
    gate = release_gate(readiness, max_cdc_lag_seconds=120, observed_cdc_lag_seconds=45)

    assert readiness["ready"] is True
    assert gate["decision"] == "ship"
    assert gate["reasons"] == []


def test_release_gate_holds_for_retrieval_or_freshness_failures():
    readiness = stack_readiness(
        {
            "source_constraints": True,
            "cdc_watermark_fresh": True,
            "analytics_backfill_ready": True,
            "retrieval_permissions_filtered": False,
            "retrieval_eval_passed": True,
        }
    )
    gate = release_gate(readiness, max_cdc_lag_seconds=120, observed_cdc_lag_seconds=180)

    assert readiness["ready"] is False
    assert gate["decision"] == "hold"
    assert "retrieval_permissions_filtered" in gate["reasons"]
    assert "cdc-lag-over-budget" in gate["reasons"]
