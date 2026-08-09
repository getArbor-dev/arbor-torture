"""Layer 1 module 00. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m01 import value_m01
from deep.l0.m11 import value_m11

BASE_00 = 100


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m00(n) + value_m01(n) + value_m11(n)
