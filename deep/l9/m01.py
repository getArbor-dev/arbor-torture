"""Layer 9 module 01. Generated, seed=20260810."""

from deep.l7.m10 import value_m10
from deep.l8.m03 import value_m03
from deep.l8.m16 import value_m16

BASE_01 = 901


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m10(n) + value_m03(n) + value_m16(n)
