"""Layer 3 module 01. Generated, seed=20260810."""

from deep.l0.m13 import value_m13
from deep.l2.m01 import value_m01

BASE_01 = 301


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m13(n) + value_m01(n)
