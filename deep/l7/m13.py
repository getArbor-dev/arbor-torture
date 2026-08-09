"""Layer 7 module 13. Generated, seed=20260810."""

from deep.l6.m08 import value_m08
from deep.l6.m25 import value_m25

BASE_13 = 713


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m08(n) + value_m25(n)
