"""Layer 4 module 15. Generated, seed=20260810."""

from deep.l1.m12 import value_m12
from deep.l2.m10 import value_m10
from deep.l3.m01 import value_m01
from deep.l3.m03 import value_m03
from deep.l3.m04 import value_m04
from deep.l3.m18 import value_m18
from deep.l3.m21 import value_m21
from deep.l3.m22 import value_m22

BASE_15 = 415


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m12(n) + value_m10(n) + value_m01(n) + value_m03(n) + value_m04(n) + value_m18(n) + value_m21(n) + value_m22(n)
