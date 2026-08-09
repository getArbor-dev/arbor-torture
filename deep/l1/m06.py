"""Layer 1 module 06. Generated, seed=20260810."""

from deep.l0.m01 import value_m01
from deep.l0.m12 import value_m12

BASE_06 = 106


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m01(n) + value_m12(n)
