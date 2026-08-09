"""Layer 6 module 23. Generated, seed=20260810."""

from deep.l4.m23 import value_m23
from deep.l4.m25 import value_m25

BASE_23 = 623


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m23(n) + value_m25(n)
