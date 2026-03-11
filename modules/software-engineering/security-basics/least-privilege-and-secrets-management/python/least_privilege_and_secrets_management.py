from __future__ import annotations


def least_privilege_scopes(
    requested_capabilities: list[str],
    capability_scopes: dict[str, list[str]],
) -> list[str]:
    if not requested_capabilities:
        raise ValueError("requested_capabilities must be non-empty")

    scopes: set[str] = set()
    for capability in requested_capabilities:
        cleaned_capability = capability.strip()
        if not cleaned_capability:
            raise ValueError("requested capabilities must be non-empty")
        if cleaned_capability not in capability_scopes:
            raise ValueError(f"unknown capability: {cleaned_capability}")
        scopes.update(scope.strip() for scope in capability_scopes[cleaned_capability] if scope.strip())
    return sorted(scopes)


def secret_handling_action(secret_name: str, destination: str) -> str:
    if not secret_name.strip():
        raise ValueError("secret_name must be non-empty")

    normalized_destination = destination.strip().lower()
    if normalized_destination in {"log", "ticket", "source-control"}:
        return "deny"
    if normalized_destination in {"config-file", "terminal-output"}:
        return "redact"
    if normalized_destination == "process-env":
        return "inject-ephemeral"
    if normalized_destination == "secret-manager":
        return "store-managed"
    raise ValueError("unknown destination")


def privilege_escalation_required(
    current_scopes: list[str],
    requested_scopes: list[str],
    secret_access: bool = False,
) -> bool:
    current = {scope.strip() for scope in current_scopes if scope.strip()}
    requested = {scope.strip() for scope in requested_scopes if scope.strip()}
    if not requested:
        raise ValueError("requested_scopes must be non-empty")
    return secret_access or not requested.issubset(current)
