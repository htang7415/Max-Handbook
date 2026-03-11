from __future__ import annotations


def classify_repo_path(path: str) -> str:
    normalized = path.strip().lower()
    if not normalized:
        return "unknown"
    if normalized.startswith("docs/"):
        return "docs"
    if normalized.startswith(("build/", "dist/", "target/", "artifacts/")):
        return "build-artifact"
    if "/generated/" in normalized or normalized.startswith(("generated/", "gen/")):
        return "generated"
    if normalized.startswith((".github/", ".gitlab/", "infra/", "config/")) or normalized.endswith(
        (".yaml", ".yml", ".toml", ".json")
    ):
        return "config"
    if normalized.startswith("tests/") or "/tests/" in normalized or normalized.endswith(
        ("_test.rs", "_test.go")
    ) or normalized.rsplit("/", 1)[-1].startswith("test_"):
        return "tests"
    if normalized.startswith(("src/", "app/", "lib/", "services/", "modules/", "web/")):
        return "source"
    return "unknown"


def should_edit_by_hand(path: str) -> bool:
    return classify_repo_path(path) not in {"generated", "build-artifact"}


def boundary_warnings(changed_paths: list[str]) -> list[str]:
    kinds = {classify_repo_path(path) for path in changed_paths if path.strip()}
    warnings: list[str] = []
    manual_kinds = {"source", "config", "docs", "tests"}

    if "generated" in kinds:
        warnings.append("verify the generator input before hand-editing generated output")
    if "generated" in kinds and kinds.intersection(manual_kinds):
        warnings.append("review source-of-truth changes separately from generated diffs")
    if "build-artifact" in kinds:
        warnings.append("avoid committing build artifacts unless the repo explicitly requires them")
    return warnings
