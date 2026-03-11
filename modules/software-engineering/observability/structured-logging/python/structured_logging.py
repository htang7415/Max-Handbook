from __future__ import annotations


def redact_context(context: dict[str, object], secret_keys: list[str] | None = None) -> dict[str, object]:
    keys_to_redact = {key.strip().lower() for key in (secret_keys or ["token", "password", "secret"]) if key.strip()}
    redacted: dict[str, object] = {}
    for key, value in context.items():
        if key.strip().lower() in keys_to_redact:
            redacted[key] = "[REDACTED]"
        else:
            redacted[key] = value
    return redacted


def make_log_event(
    service: str,
    level: str,
    message: str,
    context: dict[str, object] | None = None,
) -> dict[str, object]:
    cleaned_service = service.strip()
    cleaned_level = level.strip().lower()
    cleaned_message = message.strip()
    if not cleaned_service or not cleaned_message:
        raise ValueError("service and message must be non-empty")
    if cleaned_level not in {"debug", "info", "warn", "error"}:
        raise ValueError("level must be one of debug, info, warn, error")
    safe_context = redact_context(dict(context or {}))
    return {
        "service": cleaned_service,
        "level": cleaned_level,
        "message": cleaned_message,
        "context": safe_context,
    }


def missing_required_log_fields(log_event: dict[str, object], required_fields: list[str]) -> list[str]:
    missing: list[str] = []
    context = dict(log_event.get("context", {}))
    for field in required_fields:
        cleaned_field = field.strip()
        if not cleaned_field:
            continue
        if cleaned_field in log_event:
            if log_event[cleaned_field] in {"", None}:
                missing.append(cleaned_field)
            continue
        if cleaned_field not in context or context[cleaned_field] in {"", None}:
            missing.append(cleaned_field)
    return missing
