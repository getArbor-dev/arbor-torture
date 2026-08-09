"""Layer 4 module 25. Generated, seed=20260810."""

from deep.l2.m15 import value_m15
from deep.l3.m18 import value_m18

BASE_25 = 425


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m15(n) + value_m18(n)
