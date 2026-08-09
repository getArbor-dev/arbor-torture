"""Layer 5 module 13. Generated, seed=20260810."""

from deep.l3.m25 import value_m25
from deep.l4.m03 import value_m03
from deep.l4.m09 import value_m09

BASE_13 = 513


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m25(n) + value_m03(n) + value_m09(n)
