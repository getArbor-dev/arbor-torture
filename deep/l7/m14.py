"""Layer 7 module 14. Generated, seed=20260810."""

from deep.l4.m01 import value_m01
from deep.l4.m22 import value_m22

BASE_14 = 714


def value_m14(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m01(n) + value_m22(n)
