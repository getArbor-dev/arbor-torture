"""Layer 8 module 18. Generated, seed=20260810."""

from deep.l7.m01 import value_m01
from deep.l7.m11 import value_m11

BASE_18 = 818


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m01(n) + value_m11(n)
