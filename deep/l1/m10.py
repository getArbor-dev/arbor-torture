"""Layer 1 module 10. Generated, seed=20260810."""

from deep.l0.m05 import value_m05
from deep.l0.m11 import value_m11

BASE_10 = 110


def value_m10(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_10 * n + value_m05(n) + value_m11(n)
