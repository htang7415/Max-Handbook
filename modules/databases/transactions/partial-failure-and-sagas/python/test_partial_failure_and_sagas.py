from partial_failure_and_sagas import run_order_saga


def test_successful_saga_completes_without_compensation() -> None:
    assert run_order_saga() == {
        "inventory_reserved": True,
        "payment_charged": True,
        "shipment_created": True,
        "compensations": [],
        "status": "completed",
    }


def test_failure_after_charge_refunds_and_releases_inventory() -> None:
    assert run_order_saga(fail_after_step="charge") == {
        "inventory_reserved": False,
        "payment_charged": False,
        "shipment_created": False,
        "compensations": ["refund-payment", "release-inventory"],
        "status": "compensated",
    }


def test_failure_after_reserve_only_releases_inventory() -> None:
    assert run_order_saga(fail_after_step="reserve") == {
        "inventory_reserved": False,
        "payment_charged": False,
        "shipment_created": False,
        "compensations": ["release-inventory"],
        "status": "compensated",
    }
