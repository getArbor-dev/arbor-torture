"""Layer 4 module 04. Generated, seed=20260810."""

from deep.l1.m15 import value_m15
from deep.l2.m16 import value_m16

BASE_04 = 404


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m15(n) + value_m16(n)
