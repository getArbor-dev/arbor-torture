"""Layer 4 module 09. Generated, seed=20260810."""

from deep.l3.m09 import value_m09
from deep.l3.m13 import value_m13

BASE_09 = 409


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m09(n) + value_m13(n)
