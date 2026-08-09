"""Layer 7 module 11. Generated, seed=20260810."""

from deep.l4.m01 import value_m01
from deep.l4.m18 import value_m18
from deep.l6.m02 import value_m02

BASE_11 = 711


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m01(n) + value_m18(n) + value_m02(n)
