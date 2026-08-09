"""Layer 5 module 07. Generated, seed=20260810."""

from deep.l2.m10 import value_m10
from deep.l4.m00 import value_m00
from deep.l4.m08 import value_m08

BASE_07 = 507


def value_m07(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m10(n) + value_m00(n) + value_m08(n)
