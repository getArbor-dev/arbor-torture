"""Layer 8 module 13. Generated, seed=20260810."""

from deep.l5.m04 import value_m04
from deep.l7.m25 import value_m25

BASE_13 = 813


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m04(n) + value_m25(n)
