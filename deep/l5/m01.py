"""Layer 5 module 01. Generated, seed=20260810."""

from deep.l3.m00 import value_m00
from deep.l3.m02 import value_m02
from deep.l3.m12 import value_m12
from deep.l4.m07 import value_m07
from deep.l4.m08 import value_m08
from deep.l4.m21 import value_m21
from deep.l4.m22 import value_m22
from deep.l4.m24 import value_m24

BASE_01 = 501


def value_m01(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_01 * n + value_m00(n) + value_m02(n) + value_m12(n) + value_m07(n) + value_m08(n) + value_m21(n) + value_m22(n) + value_m24(n)
