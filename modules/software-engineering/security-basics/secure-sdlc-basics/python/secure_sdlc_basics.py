from __future__ import annotations


def required_security_checks(change_tags: list[str]) -> list[str]:
    normalized_tags = {tag.strip().lower() for tag in change_tags if tag.strip()}
    checks = ["secret-scan"]

    if normalized_tags.intersection({"auth", "permission", "api"}):
        checks.append("authz-review")
    if normalized_tags.intersection({"dependency-change", "package-update"}):
        checks.append("dependency-scan")
    if normalized_tags.intersection({"external-input", "rendering"}):
        checks.append("validation-review")
    return checks


def missing_security_checks(change_tags: list[str], completed_checks: list[str]) -> list[str]:
    required = set(required_security_checks(change_tags))
    completed = {check.strip().lower() for check in completed_checks if check.strip()}
    return sorted(required - completed)


def release_allowed(change_tags: list[str], completed_checks: list[str]) -> bool:
    return not missing_security_checks(change_tags, completed_checks)
