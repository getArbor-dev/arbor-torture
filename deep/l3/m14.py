"""Layer 3 module 14. Generated, seed=20260810."""

from deep.l2.m11 import value_m11
from deep.l2.m23 import value_m23

BASE_14 = 314


def value_m14(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_14 * n + value_m11(n) + value_m23(n)
