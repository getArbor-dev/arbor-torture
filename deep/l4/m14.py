"""Layer 4 module 14. Generated, seed=20260810."""

from deep.l3.m04 import value_m04
from deep.l3.m16 import value_m16

BASE_14 = 414


def value_m14(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m04(n) + value_m16(n)
