"""Layer 2 module 06. Generated, seed=20260810."""

from deep.l0.m18 import value_m18
from deep.l1.m16 import value_m16
from deep.l1.m24 import value_m24

BASE_06 = 206


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m18(n) + value_m16(n) + value_m24(n)
