from __future__ import annotations

from repo_layout_and_codegen_boundaries import (
    boundary_warnings,
    classify_repo_path,
    should_edit_by_hand,
)


def test_classify_repo_path_distinguishes_source_generated_and_tests() -> None:
    assert classify_repo_path("docs/guide.md") == "docs"
    assert classify_repo_path("src/generated/client.ts") == "generated"
    assert classify_repo_path("tests/test_api.py") == "tests"
    assert classify_repo_path("web/apps/site/page.tsx") == "source"


def test_should_edit_by_hand_rejects_generated_and_build_outputs() -> None:
    assert not should_edit_by_hand("src/generated/client.ts")
    assert not should_edit_by_hand("dist/bundle.js")
    assert should_edit_by_hand("src/service.py")


def test_boundary_warnings_call_out_generated_and_artifact_changes() -> None:
    assert boundary_warnings(["src/api/spec.yaml", "src/generated/client.ts", "dist/bundle.js"]) == [
        "verify the generator input before hand-editing generated output",
        "review source-of-truth changes separately from generated diffs",
        "avoid committing build artifacts unless the repo explicitly requires them",
    ]
