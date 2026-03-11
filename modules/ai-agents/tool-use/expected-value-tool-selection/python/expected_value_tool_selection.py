from __future__ import annotations


def expected_tool_value(
    success_probability: float,
    success_value: float,
    tool_cost: float,
    failure_penalty: float = 0.0,
) -> float:
    if not 0.0 <= success_probability <= 1.0:
        raise ValueError("success_probability must satisfy 0 <= value <= 1")
    if success_value < 0.0:
        raise ValueError("success_value must be non-negative")
    if tool_cost < 0.0:
        raise ValueError("tool_cost must be non-negative")
    if failure_penalty < 0.0:
        raise ValueError("failure_penalty must be non-negative")
    return success_probability * success_value - tool_cost - (1.0 - success_probability) * failure_penalty


def rank_tools_by_expected_value(tool_to_profile: dict[str, dict[str, float]]) -> list[dict[str, object]]:
    if not tool_to_profile:
        raise ValueError("tool_to_profile must be non-empty")

    ranked: list[dict[str, object]] = []
    for tool_name, profile in tool_to_profile.items():
        cleaned_name = tool_name.strip()
        if not cleaned_name:
            raise ValueError("tool names must be non-empty")
        ranked.append(
            {
                "tool": cleaned_name,
                "expected_value": expected_tool_value(
                    success_probability=float(profile.get("success_probability", 0.0)),
                    success_value=float(profile.get("success_value", 0.0)),
                    tool_cost=float(profile.get("tool_cost", 0.0)),
                    failure_penalty=float(profile.get("failure_penalty", 0.0)),
                ),
            }
        )

    return sorted(
        ranked,
        key=lambda item: (-float(item["expected_value"]), str(item["tool"])),
    )


def tool_selection_route(
    tool_to_profile: dict[str, dict[str, float]],
    min_expected_value: float,
    min_margin: float = 0.0,
) -> str:
    if min_margin < 0.0:
        raise ValueError("min_margin must be non-negative")

    ranked = rank_tools_by_expected_value(tool_to_profile)
    top_value = float(ranked[0]["expected_value"])
    if top_value < min_expected_value:
        return "skip"

    second_value = float(ranked[1]["expected_value"]) if len(ranked) > 1 else float("-inf")
    if top_value - second_value < min_margin:
        return "review"
    return str(ranked[0]["tool"])
