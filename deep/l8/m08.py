"""Layer 8 module 08. Generated, seed=20260810."""

from deep.l6.m11 import value_m11
from deep.l7.m10 import value_m10

BASE_08 = 808


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m11(n) + value_m10(n)
