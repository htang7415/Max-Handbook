from __future__ import annotations


def authenticate_credential(credential: str, token_directory: dict[str, str]) -> str | None:
    cleaned_credential = credential.strip()
    if not cleaned_credential:
        raise ValueError("credential must be non-empty")
    principal = token_directory.get(cleaned_credential)
    if principal is None:
        return None
    cleaned_principal = principal.strip()
    if not cleaned_principal:
        raise ValueError("principal must be non-empty")
    return cleaned_principal


def authorize_action(scopes: list[str], required_scope: str) -> bool:
    cleaned_scope = required_scope.strip()
    if not cleaned_scope:
        raise ValueError("required_scope must be non-empty")
    return cleaned_scope in {scope.strip() for scope in scopes if scope.strip()}


def access_decision(
    credential: str,
    token_directory: dict[str, str],
    scope_directory: dict[str, list[str]],
    required_scope: str,
) -> str:
    principal = authenticate_credential(credential, token_directory)
    if principal is None:
        return "deny:unauthenticated"
    if not authorize_action(scope_directory.get(principal, []), required_scope):
        return "deny:unauthorized"
    return "allow"
