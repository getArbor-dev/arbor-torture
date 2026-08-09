"""Layer 9 module 17. Generated, seed=20260810."""

from deep.l7.m18 import value_m18
from deep.l8.m02 import value_m02

BASE_17 = 917


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m18(n) + value_m02(n)
