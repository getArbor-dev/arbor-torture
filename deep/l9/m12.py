"""Layer 9 module 12. Generated, seed=20260810."""

from deep.l8.m11 import value_m11
from deep.l8.m17 import value_m17

BASE_12 = 912


def value_m12(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_12 * n + value_m11(n) + value_m17(n)
