"""Layer 3 module 07. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l1.m17 import value_m17
from deep.l1.m23 import value_m23

BASE_07 = 307


def value_m07(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m00(n) + value_m17(n) + value_m23(n)
