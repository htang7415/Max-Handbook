from phantom_reads_basics import phantom_summary, task_row


def test_matching_insert_creates_a_phantom_under_read_committed() -> None:
    summary = phantom_summary(
        initial_rows=[task_row(1, 8), task_row(2, 3)],
        inserted_row=task_row(3, 9),
        min_priority=8,
    )

    assert summary == {
        "read_committed": (1, 2),
        "repeatable_read": (1, 1),
        "phantom_under_read_committed": True,
        "phantom_under_repeatable_read": False,
    }


def test_non_matching_insert_does_not_change_the_range_result() -> None:
    summary = phantom_summary(
        initial_rows=[task_row(1, 8), task_row(2, 3)],
        inserted_row=task_row(3, 4),
        min_priority=8,
    )

    assert summary["read_committed"] == (1, 1)
    assert summary["phantom_under_read_committed"] is False
