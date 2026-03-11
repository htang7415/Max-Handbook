from connectors_and_pipeline_shapes import (
    classify_pipeline_shape,
    reachable_sinks,
    validate_pipeline,
)


def test_source_transform_sink_pipeline_is_valid() -> None:
    stages = {"db": "source", "clean": "transform", "warehouse": "sink"}
    edges = [("db", "clean"), ("clean", "warehouse")]

    assert validate_pipeline(stages, edges) is True
    assert classify_pipeline_shape(stages, edges) == "source-transform-sink"


def test_fan_out_pipeline_reaches_multiple_sinks() -> None:
    stages = {"db": "source", "warehouse": "sink", "cache": "sink"}
    edges = [("db", "warehouse"), ("db", "cache")]

    assert classify_pipeline_shape(stages, edges) == "fan-out"
    assert reachable_sinks(stages, edges, "db") == ["cache", "warehouse"]


def test_invalid_pipeline_rejects_inbound_edges_into_a_source() -> None:
    stages = {"db": "source", "warehouse": "sink"}
    edges = [("warehouse", "db")]

    assert validate_pipeline(stages, edges) is False
    assert classify_pipeline_shape(stages, edges) == "invalid"
