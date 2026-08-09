"""Layer 4 module 10. Generated, seed=20260810."""

from deep.l1.m14 import value_m14
from deep.l2.m20 import value_m20
from deep.l3.m11 import value_m11

BASE_10 = 410


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m14(n) + value_m20(n) + value_m11(n)
