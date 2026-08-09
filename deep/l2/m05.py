"""Layer 2 module 05. Generated, seed=20260810."""

from deep.l1.m01 import value_m01
from deep.l1.m16 import value_m16

BASE_05 = 205


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m01(n) + value_m16(n)
