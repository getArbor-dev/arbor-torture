"""Layer 6 module 06. Generated, seed=20260810."""

from deep.l4.m17 import value_m17
from deep.l5.m19 import value_m19

BASE_06 = 606


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m17(n) + value_m19(n)
