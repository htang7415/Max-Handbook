from __future__ import annotations


def _is_pinned(spec: str) -> bool:
    cleaned = spec.strip()
    if not cleaned:
        return False
    floating_markers = ("^", "~", "*", ">", "<", ",")
    if any(marker in cleaned for marker in floating_markers):
        return False
    if cleaned.startswith("=="):
        cleaned = cleaned[2:]
    return bool(cleaned)


def find_unpinned_dependencies(dependencies: dict[str, str]) -> list[str]:
    return sorted(name for name, spec in dependencies.items() if not _is_pinned(spec))


def environment_drift(required: dict[str, str], actual: dict[str, str]) -> dict[str, list[str]]:
    missing = sorted(name for name in required if name not in actual)
    mismatched = sorted(
        name for name, version in required.items() if name in actual and actual[name] != version
    )
    unexpected = sorted(name for name in actual if name not in required)
    return {
        "missing": missing,
        "mismatched": mismatched,
        "unexpected": unexpected,
    }


def missing_reproducibility_controls(
    runtime_version: str | None,
    lockfile_present: bool,
    dependencies: dict[str, str],
) -> list[str]:
    missing_controls: list[str] = []
    if not runtime_version or not runtime_version.strip():
        missing_controls.append("pin runtime version")
    if not lockfile_present:
        missing_controls.append("commit lockfile")

    unpinned = find_unpinned_dependencies(dependencies)
    if unpinned:
        joined = ", ".join(unpinned)
        missing_controls.append(f"pin dependency versions: {joined}")
    return missing_controls
