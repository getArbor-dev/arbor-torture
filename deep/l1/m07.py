"""Layer 1 module 07. Generated, seed=20260810."""

from deep.l0.m03 import value_m03
from deep.l0.m13 import value_m13
from deep.l0.m18 import value_m18

BASE_07 = 107


def value_m07(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m03(n) + value_m13(n) + value_m18(n)
