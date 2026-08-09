"""Layer 5 module 09. Generated, seed=20260810."""

from deep.l2.m25 import value_m25
from deep.l4.m04 import value_m04
from deep.l4.m08 import value_m08

BASE_09 = 509


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m25(n) + value_m04(n) + value_m08(n)
