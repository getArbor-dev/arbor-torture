"""Layer 6 module 07. Generated, seed=20260810."""

from deep.l3.m25 import value_m25
from deep.l5.m24 import value_m24

BASE_07 = 607


def value_m07(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m25(n) + value_m24(n)
