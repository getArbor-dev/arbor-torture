"""Layer 6 module 20. Generated, seed=20260810."""

from deep.l3.m22 import value_m22
from deep.l4.m07 import value_m07

BASE_20 = 620


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m22(n) + value_m07(n)
