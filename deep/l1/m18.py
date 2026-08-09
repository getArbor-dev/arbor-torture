"""Layer 1 module 18. Generated, seed=20260810."""

from deep.l0.m06 import value_m06
from deep.l0.m11 import value_m11
from deep.l0.m14 import value_m14
from deep.l0.m15 import value_m15
from deep.l0.m24 import value_m24

BASE_18 = 118


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m06(n) + value_m11(n) + value_m14(n) + value_m15(n) + value_m24(n)
