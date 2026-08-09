"""Layer 2 module 24. Generated, seed=20260810."""

from deep.l0.m07 import value_m07
from deep.l1.m18 import value_m18

BASE_24 = 224


def value_m24(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_24 * n + value_m07(n) + value_m18(n)
