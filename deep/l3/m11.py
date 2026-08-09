"""Layer 3 module 11. Generated, seed=20260810."""

from deep.l1.m09 import value_m09
from deep.l1.m21 import value_m21
from deep.l2.m01 import value_m01

BASE_11 = 311


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m09(n) + value_m21(n) + value_m01(n)
