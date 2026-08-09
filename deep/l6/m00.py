"""Layer 6 module 00. Generated, seed=20260810."""

from deep.l5.m04 import value_m04

BASE_00 = 600


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m04(n)
