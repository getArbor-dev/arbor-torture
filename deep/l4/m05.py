"""Layer 4 module 05. Generated, seed=20260810."""

from deep.l2.m08 import value_m08
from deep.l3.m04 import value_m04
from deep.l3.m22 import value_m22

BASE_05 = 405


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m08(n) + value_m04(n) + value_m22(n)
