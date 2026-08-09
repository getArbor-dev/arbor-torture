"""Layer 8 module 04. Generated, seed=20260810."""

from deep.l6.m16 import value_m16
from deep.l6.m21 import value_m21
from deep.l6.m22 import value_m22
from deep.l6.m25 import value_m25
from deep.l7.m18 import value_m18

BASE_04 = 804


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m16(n) + value_m21(n) + value_m22(n) + value_m25(n) + value_m18(n)
