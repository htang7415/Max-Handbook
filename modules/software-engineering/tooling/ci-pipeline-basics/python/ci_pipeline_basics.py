from __future__ import annotations


def required_ci_stages(change_tags: list[str]) -> list[str]:
    normalized_tags = {tag.strip().lower() for tag in change_tags if tag.strip()}
    stages = ["lint", "unit"]

    if normalized_tags.intersection({"api", "schema", "serialization"}):
        stages.append("contract")
    if normalized_tags.intersection({"database", "workflow", "integration"}):
        stages.append("integration")
    if normalized_tags.intersection({"bugfix", "ai-generated", "security"}):
        stages.append("regression")
    if normalized_tags.intersection({"release", "build", "deploy"}):
        stages.append("build")
    return stages


def pipeline_blockers(stage_statuses: dict[str, str], required_stages: list[str]) -> list[str]:
    blockers: list[str] = []
    for stage in required_stages:
        status = stage_statuses.get(stage)
        if status != "passed":
            blockers.append(stage)
    return blockers


def mergeable(stage_statuses: dict[str, str], required_stages: list[str]) -> bool:
    return not pipeline_blockers(stage_statuses, required_stages)
