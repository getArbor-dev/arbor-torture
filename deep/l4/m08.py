"""Layer 4 module 08. Generated, seed=20260810."""

from deep.l3.m20 import value_m20

BASE_08 = 408


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m20(n)
