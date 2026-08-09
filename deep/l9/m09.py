"""Layer 9 module 09. Generated, seed=20260810."""

from deep.l6.m08 import value_m08
from deep.l8.m20 import value_m20

BASE_09 = 909


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m08(n) + value_m20(n)
