"""Layer 2 module 00. Generated, seed=20260810."""

from deep.l0.m11 import value_m11
from deep.l1.m17 import value_m17
from deep.l1.m22 import value_m22

BASE_00 = 200


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m11(n) + value_m17(n) + value_m22(n)
