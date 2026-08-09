"""Layer 9 module 11. Generated, seed=20260810."""

from deep.l6.m01 import value_m01
from deep.l6.m19 import value_m19

BASE_11 = 911


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m01(n) + value_m19(n)
