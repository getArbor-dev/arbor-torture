"""Layer 9 module 08. Generated, seed=20260810."""

from deep.l7.m15 import value_m15
from deep.l8.m01 import value_m01
from deep.l8.m24 import value_m24

BASE_08 = 908


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m15(n) + value_m01(n) + value_m24(n)
