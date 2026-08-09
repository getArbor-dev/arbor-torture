"""Layer 3 module 04. Generated, seed=20260810."""

from deep.l2.m06 import value_m06
from deep.l2.m14 import value_m14
from deep.l2.m15 import value_m15

BASE_04 = 304


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m06(n) + value_m14(n) + value_m15(n)
