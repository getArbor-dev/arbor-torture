"""Layer 5 module 00. Generated, seed=20260810."""

from deep.l3.m06 import value_m06
from deep.l4.m20 import value_m20

BASE_00 = 500


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m06(n) + value_m20(n)
