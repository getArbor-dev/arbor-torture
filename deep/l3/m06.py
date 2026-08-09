"""Layer 3 module 06. Generated, seed=20260810."""

from deep.l2.m09 import value_m09
from deep.l2.m23 import value_m23

BASE_06 = 306


def value_m06(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_06 * n + value_m09(n) + value_m23(n)
