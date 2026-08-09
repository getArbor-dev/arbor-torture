"""Layer 1 module 11. Generated, seed=20260810."""

from deep.l0.m06 import value_m06
from deep.l0.m07 import value_m07
from deep.l0.m13 import value_m13

BASE_11 = 111


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m06(n) + value_m07(n) + value_m13(n)
