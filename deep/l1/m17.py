"""Layer 1 module 17. Generated, seed=20260810."""

from deep.l0.m04 import value_m04
from deep.l0.m25 import value_m25

BASE_17 = 117


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m04(n) + value_m25(n)
