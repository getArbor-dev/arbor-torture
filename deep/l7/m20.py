"""Layer 7 module 20. Generated, seed=20260810."""

from deep.l6.m05 import value_m05
from deep.l6.m07 import value_m07

BASE_20 = 720


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m05(n) + value_m07(n)
