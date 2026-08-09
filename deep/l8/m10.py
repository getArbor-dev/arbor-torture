"""Layer 8 module 10. Generated, seed=20260810."""

from deep.l5.m01 import value_m01
from deep.l6.m05 import value_m05
from deep.l7.m07 import value_m07

BASE_10 = 810


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m01(n) + value_m05(n) + value_m07(n)
