"""Layer 1 module 01. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m03 import value_m03
from deep.l0.m13 import value_m13

BASE_01 = 101


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m00(n) + value_m03(n) + value_m13(n)
