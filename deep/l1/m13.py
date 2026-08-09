"""Layer 1 module 13. Generated, seed=20260810."""

from deep.l0.m05 import value_m05
from deep.l0.m13 import value_m13

BASE_13 = 113


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m05(n) + value_m13(n)
