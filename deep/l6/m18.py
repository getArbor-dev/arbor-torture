"""Layer 6 module 18. Generated, seed=20260810."""

from deep.l4.m02 import value_m02
from deep.l5.m06 import value_m06
from deep.l5.m13 import value_m13

BASE_18 = 618


def value_m18(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_18 * n + value_m02(n) + value_m06(n) + value_m13(n)
