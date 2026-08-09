"""Layer 7 module 01. Generated, seed=20260810."""

from deep.l5.m00 import value_m00
from deep.l6.m25 import value_m25

BASE_01 = 701


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m00(n) + value_m25(n)
