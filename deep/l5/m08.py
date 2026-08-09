"""Layer 5 module 08. Generated, seed=20260810."""

from deep.l2.m13 import value_m13
from deep.l2.m20 import value_m20
from deep.l3.m06 import value_m06
from deep.l4.m11 import value_m11
from deep.l4.m22 import value_m22

BASE_08 = 508


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m13(n) + value_m20(n) + value_m06(n) + value_m11(n) + value_m22(n)
