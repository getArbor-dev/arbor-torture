"""Layer 6 module 11. Generated, seed=20260810."""

from deep.l3.m05 import value_m05
from deep.l4.m09 import value_m09

BASE_11 = 611


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m05(n) + value_m09(n)
