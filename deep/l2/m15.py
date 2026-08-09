"""Layer 2 module 15. Generated, seed=20260810."""

from deep.l0.m13 import value_m13
from deep.l0.m25 import value_m25

BASE_15 = 215


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m13(n) + value_m25(n)
