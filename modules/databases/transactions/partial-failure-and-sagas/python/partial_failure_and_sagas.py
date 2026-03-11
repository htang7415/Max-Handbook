"""partial_failure_and_sagas - compensate earlier steps when a later step fails."""

from __future__ import annotations


def empty_saga_state() -> dict[str, object]:
    return {
        "inventory_reserved": False,
        "payment_charged": False,
        "shipment_created": False,
        "compensations": [],
        "status": "pending",
    }


def reserve_inventory(state: dict[str, object]) -> None:
    state["inventory_reserved"] = True


def charge_payment(state: dict[str, object]) -> None:
    state["payment_charged"] = True


def create_shipment(state: dict[str, object]) -> None:
    state["shipment_created"] = True


def release_inventory(state: dict[str, object]) -> None:
    state["inventory_reserved"] = False
    compensations = state["compensations"]
    assert isinstance(compensations, list)
    compensations.append("release-inventory")


def refund_payment(state: dict[str, object]) -> None:
    state["payment_charged"] = False
    compensations = state["compensations"]
    assert isinstance(compensations, list)
    compensations.append("refund-payment")


def run_order_saga(fail_after_step: str | None = None) -> dict[str, object]:
    state = empty_saga_state()
    try:
        reserve_inventory(state)
        if fail_after_step == "reserve":
            raise RuntimeError("failure after reserving inventory")

        charge_payment(state)
        if fail_after_step == "charge":
            raise RuntimeError("failure after charging payment")

        create_shipment(state)
        if fail_after_step == "ship":
            raise RuntimeError("failure after creating shipment")

        state["status"] = "completed"
        return state
    except RuntimeError:
        if bool(state["shipment_created"]):
            state["shipment_created"] = False
        if bool(state["payment_charged"]):
            refund_payment(state)
        if bool(state["inventory_reserved"]):
            release_inventory(state)
        state["status"] = "compensated"
        return state
