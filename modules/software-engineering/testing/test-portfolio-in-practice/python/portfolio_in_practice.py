from __future__ import annotations


def recommended_test_layers(change_tags: list[str]) -> list[str]:
    normalized_tags = {tag.strip().lower() for tag in change_tags if tag.strip()}
    layers = ["unit"]

    if normalized_tags.intersection({"api", "schema", "serialization"}):
        layers.append("contract")
    if normalized_tags.intersection({"database", "workflow", "queue", "integration"}):
        layers.append("integration")
    if normalized_tags.intersection({"bugfix", "ai-generated", "security"}):
        layers.append("regression")
    if normalized_tags.intersection({"critical-path", "ui-flow", "release"}):
        layers.append("end-to-end")

    return layers


def missing_required_layers(change_tags: list[str], present_layers: list[str]) -> list[str]:
    expected = set(recommended_test_layers(change_tags))
    present = {layer.strip().lower() for layer in present_layers if layer.strip()}
    return sorted(expected - present)


def merge_ready(change_tags: list[str], present_layers: list[str]) -> bool:
    return not missing_required_layers(change_tags, present_layers)
