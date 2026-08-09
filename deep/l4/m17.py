"""Layer 4 module 17. Generated, seed=20260810."""

from deep.l2.m00 import value_m00
from deep.l2.m10 import value_m10

BASE_17 = 417


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m00(n) + value_m10(n)
