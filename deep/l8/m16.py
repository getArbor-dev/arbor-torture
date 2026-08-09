"""Layer 8 module 16. Generated, seed=20260810."""

from deep.l5.m00 import value_m00
from deep.l5.m09 import value_m09
from deep.l7.m13 import value_m13

BASE_16 = 816


def value_m16(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_16 * n + value_m00(n) + value_m09(n) + value_m13(n)
