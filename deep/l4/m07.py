"""Layer 4 module 07. Generated, seed=20260810."""

from deep.l3.m05 import value_m05
from deep.l3.m20 import value_m20

BASE_07 = 407


def value_m07(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m05(n) + value_m20(n)
