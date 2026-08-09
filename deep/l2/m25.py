"""Layer 2 module 25. Generated, seed=20260810."""

from deep.l1.m01 import value_m01
from deep.l1.m05 import value_m05
from deep.l1.m20 import value_m20

BASE_25 = 225


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m01(n) + value_m05(n) + value_m20(n)
