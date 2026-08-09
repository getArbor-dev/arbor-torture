"""Layer 7 module 00. Generated, seed=20260810."""

from deep.l4.m00 import value_m00

BASE_00 = 700


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m00(n)
