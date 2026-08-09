"""Layer 8 module 01. Generated, seed=20260810."""

from deep.l6.m11 import value_m11
from deep.l6.m24 import value_m24
from deep.l7.m21 import value_m21

BASE_01 = 801


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m11(n) + value_m24(n) + value_m21(n)
