"""Layer 5 module 24. Generated, seed=20260810."""

from deep.l3.m16 import value_m16
from deep.l4.m02 import value_m02

BASE_24 = 524


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m16(n) + value_m02(n)
