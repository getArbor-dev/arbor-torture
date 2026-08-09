"""Layer 9 module 05. Generated, seed=20260810."""

from deep.l6.m21 import value_m21
from deep.l7.m10 import value_m10
from deep.l8.m13 import value_m13

BASE_05 = 905


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m21(n) + value_m10(n) + value_m13(n)
