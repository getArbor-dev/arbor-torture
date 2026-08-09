"""Layer 2 module 13. Generated, seed=20260810."""

from deep.l0.m16 import value_m16
from deep.l1.m21 import value_m21

BASE_13 = 213


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m16(n) + value_m21(n)
