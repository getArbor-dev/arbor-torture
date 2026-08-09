"""Layer 9 module 13. Generated, seed=20260810."""

from deep.l6.m03 import value_m03
from deep.l6.m16 import value_m16
from deep.l8.m06 import value_m06
from deep.l8.m14 import value_m14
from deep.l8.m17 import value_m17

BASE_13 = 913


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m03(n) + value_m16(n) + value_m06(n) + value_m14(n) + value_m17(n)
