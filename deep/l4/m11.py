"""Layer 4 module 11. Generated, seed=20260810."""

from deep.l1.m06 import value_m06
from deep.l3.m24 import value_m24

BASE_11 = 411


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m06(n) + value_m24(n)
