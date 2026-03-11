from __future__ import annotations

from span_taxonomy import label_spans, span_kind, span_kind_counts


def test_span_taxonomy_labels_common_span_types() -> None:
    assert span_kind("tool_call") == "tool"
    assert span_kind("guardrail_check") == "guardrail"
    assert span_kind("plan") == "workflow"
    assert span_kind("model_generate") == "model"
    assert label_spans(["plan", "tool_call", "guardrail_check"]) == {
        "plan": "workflow",
        "tool_call": "tool",
        "guardrail_check": "guardrail",
    }
    assert span_kind_counts(["plan", "tool_call", "tool_result"]) == {
        "workflow": 1,
        "tool": 2,
    }


def test_span_taxonomy_handles_unknown_and_empty_names() -> None:
    assert span_kind("") == "unknown"
    assert label_spans(["", "custom_step"]) == {"custom_step": "unknown"}
