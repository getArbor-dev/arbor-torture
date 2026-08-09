"""Layer 7 module 05. Generated, seed=20260810."""

from deep.l6.m04 import value_m04
from deep.l6.m17 import value_m17

BASE_05 = 705


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m04(n) + value_m17(n)
