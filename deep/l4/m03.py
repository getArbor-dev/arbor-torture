"""Layer 4 module 03. Generated, seed=20260810."""

from deep.l1.m13 import value_m13
from deep.l1.m23 import value_m23
from deep.l2.m05 import value_m05
from deep.l2.m07 import value_m07
from deep.l2.m22 import value_m22
from deep.l3.m14 import value_m14
from deep.l3.m16 import value_m16
from deep.l3.m17 import value_m17

BASE_03 = 403


def value_m03(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_03 * n + value_m13(n) + value_m23(n) + value_m05(n) + value_m07(n) + value_m22(n) + value_m14(n) + value_m16(n) + value_m17(n)
