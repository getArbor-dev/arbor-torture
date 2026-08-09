"""Layer 1 module 16. Generated, seed=20260810."""

from deep.l0.m03 import value_m03
from deep.l0.m13 import value_m13
from deep.l0.m14 import value_m14

BASE_16 = 116


def value_m16(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_16 * n + value_m03(n) + value_m13(n) + value_m14(n)
