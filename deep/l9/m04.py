"""Layer 9 module 04. Generated, seed=20260810."""

from deep.l7.m12 import value_m12
from deep.l8.m01 import value_m01
from deep.l8.m09 import value_m09
from deep.l8.m15 import value_m15
from deep.l8.m16 import value_m16

BASE_04 = 904


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m12(n) + value_m01(n) + value_m09(n) + value_m15(n) + value_m16(n)
