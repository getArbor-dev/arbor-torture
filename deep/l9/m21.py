"""Layer 9 module 21. Generated, seed=20260810."""

from deep.l7.m02 import value_m02
from deep.l7.m05 import value_m05
from deep.l8.m12 import value_m12

BASE_21 = 921


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m02(n) + value_m05(n) + value_m12(n)
