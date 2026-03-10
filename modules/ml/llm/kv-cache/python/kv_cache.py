def kv_cache_bytes(
    num_layers: int,
    num_tokens: int,
    num_kv_heads: int,
    head_dim: int,
    bytes_per_element: int,
    batch_size: int = 1,
) -> int:
    values = [
        num_layers,
        num_tokens,
        num_kv_heads,
        head_dim,
        bytes_per_element,
        batch_size,
    ]
    if any(value <= 0 for value in values):
        raise ValueError("all arguments must be positive")

    return (
        batch_size
        * num_layers
        * num_tokens
        * num_kv_heads
        * head_dim
        * 2
        * bytes_per_element
    )


def kv_cache_gib(
    num_layers: int,
    num_tokens: int,
    num_kv_heads: int,
    head_dim: int,
    bytes_per_element: int,
    batch_size: int = 1,
) -> float:
    bytes_used = kv_cache_bytes(
        num_layers=num_layers,
        num_tokens=num_tokens,
        num_kv_heads=num_kv_heads,
        head_dim=head_dim,
        bytes_per_element=bytes_per_element,
        batch_size=batch_size,
    )
    return bytes_used / (1024**3)
