from index_write_amplification import update_work, write_summary


def test_more_indexes_raise_total_write_work() -> None:
    light = write_summary(insert_rows=100, update_rows=20, index_count=1, indexed_updates=True)
    heavy = write_summary(insert_rows=100, update_rows=20, index_count=4, indexed_updates=True)

    assert int(heavy["total_work"]) > int(light["total_work"])
    assert float(heavy["amplification_ratio"]) > float(light["amplification_ratio"])


def test_non_indexed_updates_do_not_pay_index_maintenance() -> None:
    assert update_work(update_rows=50, index_count=5, indexed_updates=False) == 50
