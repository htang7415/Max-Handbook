from __future__ import annotations


def assign_roles(task: str, role_keywords: dict[str, list[str]]) -> list[str]:
    lowered = task.strip().lower()
    if not lowered:
        return []
    selected: list[str] = []
    for role, keywords in role_keywords.items():
        if any(keyword.strip().lower() in lowered for keyword in keywords if keyword.strip()):
            selected.append(role)
    return selected


def role_owners(roles: list[str]) -> dict[str, str]:
    return {role: f"{role}-worker" for role in roles if role.strip()}


def role_assignment_summary(roles: list[str]) -> str:
    cleaned = [role.strip() for role in roles if role.strip()]
    if not cleaned:
        return "No roles assigned."
    return "Roles: " + ", ".join(cleaned)
