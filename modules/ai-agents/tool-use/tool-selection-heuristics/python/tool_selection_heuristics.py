from __future__ import annotations


def keyword_match_score(intent: str, keywords: list[str]) -> int:
    lowered = intent.strip().lower()
    if not lowered:
        return 0
    return sum(1 for keyword in keywords if keyword.strip().lower() in lowered)


def rank_tools(intent: str, tool_keywords: dict[str, list[str]]) -> list[tuple[str, int]]:
    scores = [
        (tool, keyword_match_score(intent, keywords))
        for tool, keywords in tool_keywords.items()
    ]
    ranked = sorted(scores, key=lambda item: (-item[1], item[0]))
    return [(tool, score) for tool, score in ranked if score > 0]


def pick_tool(intent: str, tool_keywords: dict[str, list[str]]) -> str | None:
    ranked = rank_tools(intent, tool_keywords)
    if not ranked:
        return None
    return ranked[0][0]
