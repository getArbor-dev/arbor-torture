"""Layer 7 module 12. Generated, seed=20260810."""

from deep.l5.m09 import value_m09
from deep.l5.m17 import value_m17
from deep.l6.m04 import value_m04

BASE_12 = 712


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m09(n) + value_m17(n) + value_m04(n)
