"""Layer 5 module 11. Generated, seed=20260810."""

from deep.l4.m05 import value_m05
from deep.l4.m11 import value_m11

BASE_11 = 511


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m05(n) + value_m11(n)
