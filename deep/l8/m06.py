"""Layer 8 module 06. Generated, seed=20260810."""

from deep.l7.m16 import value_m16
from deep.l7.m23 import value_m23

BASE_06 = 806


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m16(n) + value_m23(n)
