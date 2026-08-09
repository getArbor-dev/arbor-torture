"""Layer 9 module 20. Generated, seed=20260810."""

from deep.l7.m00 import value_m00
from deep.l7.m09 import value_m09
from deep.l8.m15 import value_m15

BASE_20 = 920


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m00(n) + value_m09(n) + value_m15(n)
