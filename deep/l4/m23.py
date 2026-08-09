"""Layer 4 module 23. Generated, seed=20260810."""

from deep.l3.m13 import value_m13
from deep.l3.m14 import value_m14

BASE_23 = 423


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m13(n) + value_m14(n)
