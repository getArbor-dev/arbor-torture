"""Layer 3 module 24. Generated, seed=20260810."""

from deep.l1.m00 import value_m00
from deep.l2.m18 import value_m18

BASE_24 = 324


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m00(n) + value_m18(n)
