from secondary_read_after_write_consistency import read_after_write_summary, version


def test_lagging_secondary_can_return_stale_data_after_a_write() -> None:
    versions = [
        version(100, "draft"),
        version(120, "published"),
    ]

    assert read_after_write_summary(versions, last_write_lsn=120, secondary_applied_lsn=100) == {
        "secondary_value": "draft",
        "primary_value": "published",
        "secondary_is_safe": False,
        "recommended_target": "primary",
    }


def test_caught_up_secondary_is_safe_for_read_after_write() -> None:
    versions = [
        version(100, "draft"),
        version(120, "published"),
    ]

    assert read_after_write_summary(versions, last_write_lsn=120, secondary_applied_lsn=120) == {
        "secondary_value": "published",
        "primary_value": "published",
        "secondary_is_safe": True,
        "recommended_target": "secondary",
    }
