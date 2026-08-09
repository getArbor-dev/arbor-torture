"""Layer 7 module 25. Generated, seed=20260810."""

from deep.l4.m02 import value_m02
from deep.l5.m08 import value_m08

BASE_25 = 725


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m02(n) + value_m08(n)
