"""Layer 7 module 24. Generated, seed=20260810."""

from deep.l4.m00 import value_m00
from deep.l4.m12 import value_m12

BASE_24 = 724


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m00(n) + value_m12(n)
