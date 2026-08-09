"""Layer 4 module 01. Generated, seed=20260810."""

from deep.l1.m06 import value_m06
from deep.l2.m10 import value_m10
from deep.l2.m19 import value_m19
from deep.l3.m01 import value_m01
from deep.l3.m16 import value_m16
from deep.l3.m20 import value_m20
from deep.l3.m21 import value_m21
from deep.l3.m22 import value_m22

BASE_01 = 401


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m06(n) + value_m10(n) + value_m19(n) + value_m01(n) + value_m16(n) + value_m20(n) + value_m21(n) + value_m22(n)
