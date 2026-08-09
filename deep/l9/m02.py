"""Layer 9 module 02. Generated, seed=20260810."""

from deep.l6.m05 import value_m05
from deep.l7.m14 import value_m14

BASE_02 = 902


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m05(n) + value_m14(n)
