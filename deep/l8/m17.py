"""Layer 8 module 17. Generated, seed=20260810."""

from deep.l5.m24 import value_m24
from deep.l7.m15 import value_m15

BASE_17 = 817


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m24(n) + value_m15(n)
