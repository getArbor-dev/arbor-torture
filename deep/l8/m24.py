"""Layer 8 module 24. Generated, seed=20260810."""

from deep.l5.m05 import value_m05
from deep.l7.m12 import value_m12

BASE_24 = 824


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m05(n) + value_m12(n)
