"""Layer 7 module 04. Generated, seed=20260810."""

from deep.l4.m12 import value_m12
from deep.l4.m22 import value_m22
from deep.l4.m23 import value_m23
from deep.l6.m01 import value_m01
from deep.l6.m08 import value_m08
from deep.l6.m11 import value_m11
from deep.l6.m14 import value_m14
from deep.l6.m16 import value_m16

BASE_04 = 704


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m12(n) + value_m22(n) + value_m23(n) + value_m01(n) + value_m08(n) + value_m11(n) + value_m14(n) + value_m16(n)
