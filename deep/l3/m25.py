"""Layer 3 module 25. Generated, seed=20260810."""

from deep.l0.m09 import value_m09
from deep.l2.m12 import value_m12

BASE_25 = 325


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m09(n) + value_m12(n)
