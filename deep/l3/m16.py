"""Layer 3 module 16. Generated, seed=20260810."""

from deep.l1.m08 import value_m08
from deep.l2.m01 import value_m01

BASE_16 = 316


def value_m16(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_16 * n + value_m08(n) + value_m01(n)
