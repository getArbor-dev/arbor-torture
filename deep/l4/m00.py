"""Layer 4 module 00. Generated, seed=20260810."""

from deep.l1.m06 import value_m06
from deep.l2.m07 import value_m07
from deep.l3.m14 import value_m14

BASE_00 = 400


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m06(n) + value_m07(n) + value_m14(n)
