from __future__ import annotations


def least_privilege_scopes(
    requested_tools: list[str],
    tool_scopes: dict[str, list[str]],
) -> list[str]:
    if not requested_tools:
        raise ValueError("requested_tools must be non-empty")

    scopes: set[str] = set()
    for tool_name in requested_tools:
        cleaned_tool = tool_name.strip()
        if not cleaned_tool:
            raise ValueError("requested tool names must be non-empty")
        if cleaned_tool not in tool_scopes:
            raise ValueError(f"unknown tool: {cleaned_tool}")
        for scope in tool_scopes[cleaned_tool]:
            cleaned_scope = scope.strip()
            if cleaned_scope:
                scopes.add(cleaned_scope)
    return sorted(scopes)


def sandbox_profile(needs_write: bool, needs_network: bool, handles_secrets: bool) -> str:
    if handles_secrets and (needs_write or needs_network):
        return "isolated-review"
    if needs_write and needs_network:
        return "workspace-write-network"
    if needs_write:
        return "workspace-write"
    if needs_network:
        return "read-only-network"
    return "read-only"


def scope_escalation_required(current_scopes: list[str], requested_scopes: list[str]) -> bool:
    current = {scope.strip() for scope in current_scopes if scope.strip()}
    requested = {scope.strip() for scope in requested_scopes if scope.strip()}
    if not requested:
        raise ValueError("requested_scopes must be non-empty")
    return not requested.issubset(current)
