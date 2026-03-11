from __future__ import annotations

from tool_selection_heuristics import keyword_match_score, pick_tool, rank_tools


def test_tool_selection_heuristics_scores_and_picks_best_tool() -> None:
    tool_keywords = {
        "weather": ["weather", "temperature"],
        "calendar": ["schedule", "meeting"],
        "search": ["search", "look up"],
    }
    assert keyword_match_score("check the weather in Madison", ["weather", "temperature"]) == 1
    assert rank_tools("check the weather in Madison", tool_keywords) == [("weather", 1)]
    assert pick_tool("check the weather in Madison", tool_keywords) == "weather"


def test_tool_selection_heuristics_handles_no_match() -> None:
    tool_keywords = {"calendar": ["meeting"]}
    assert rank_tools("tell me a joke", tool_keywords) == []
    assert pick_tool("tell me a joke", tool_keywords) is None
