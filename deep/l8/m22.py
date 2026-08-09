"""Layer 8 module 22. Generated, seed=20260810."""

from deep.l7.m04 import value_m04
from deep.l7.m13 import value_m13

BASE_22 = 822


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m04(n) + value_m13(n)
