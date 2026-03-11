from __future__ import annotations


def rule_specificity(rule: dict[str, object]) -> int:
    conditions = rule.get("conditions")
    if not isinstance(conditions, dict) or not conditions:
        raise ValueError("rule conditions must be a non-empty dict")
    if "action" not in rule or not str(rule["action"]).strip():
        raise ValueError("rule action must be non-empty")

    specificity = 0
    for signal_name, signal_value in conditions.items():
        if not str(signal_name).strip():
            raise ValueError("condition names must be non-empty")
        if not isinstance(signal_value, bool):
            raise ValueError("condition values must be boolean")
        specificity += 1
    return specificity


def ranked_policy_rules(rules: list[dict[str, object]]) -> list[dict[str, object]]:
    if not rules:
        raise ValueError("rules must be non-empty")

    ranked = []
    for rule in rules:
        action = str(rule.get("action", "")).strip()
        specificity = rule_specificity(rule)
        ranked.append(
            {
                "conditions": dict(rule["conditions"]),
                "action": action,
                "specificity": specificity,
            }
        )

    return sorted(
        ranked,
        key=lambda rule: (-int(rule["specificity"]), str(rule["action"])),
    )


def decision_table_action(
    signals: dict[str, bool],
    rules: list[dict[str, object]],
    default_action: str,
) -> str:
    cleaned_default = default_action.strip()
    if not cleaned_default:
        raise ValueError("default_action must be non-empty")
    if not signals:
        raise ValueError("signals must be non-empty")

    normalized_signals: dict[str, bool] = {}
    for signal_name, signal_value in signals.items():
        cleaned_name = str(signal_name).strip()
        if not cleaned_name:
            raise ValueError("signal names must be non-empty")
        if not isinstance(signal_value, bool):
            raise ValueError("signal values must be boolean")
        normalized_signals[cleaned_name] = signal_value

    for rule in ranked_policy_rules(rules):
        conditions = dict(rule["conditions"])
        if all(normalized_signals.get(str(name).strip()) is value for name, value in conditions.items()):
            return str(rule["action"])
    return cleaned_default
