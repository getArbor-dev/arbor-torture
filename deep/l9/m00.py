"""Layer 9 module 00. Generated, seed=20260810."""

from deep.l8.m02 import value_m02

BASE_00 = 900


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m02(n)
