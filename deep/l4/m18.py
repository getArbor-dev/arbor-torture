"""Layer 4 module 18. Generated, seed=20260810."""

from deep.l1.m22 import value_m22
from deep.l2.m13 import value_m13
from deep.l3.m04 import value_m04
from deep.l3.m14 import value_m14
from deep.l3.m16 import value_m16

BASE_18 = 418


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m22(n) + value_m13(n) + value_m04(n) + value_m14(n) + value_m16(n)
