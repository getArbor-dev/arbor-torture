"""Layer 8 module 20. Generated, seed=20260810."""

from deep.l6.m09 import value_m09
from deep.l7.m08 import value_m08

BASE_20 = 820


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m09(n) + value_m08(n)
