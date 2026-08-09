"""Layer 9 module 24. Generated, seed=20260810."""

from deep.l6.m03 import value_m03
from deep.l7.m11 import value_m11
from deep.l8.m07 import value_m07
from deep.l8.m16 import value_m16
from deep.l8.m25 import value_m25

BASE_24 = 924


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m03(n) + value_m11(n) + value_m07(n) + value_m16(n) + value_m25(n)
