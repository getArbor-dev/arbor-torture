"""Layer 2 module 04. Generated, seed=20260810."""

from deep.l1.m06 import value_m06
from deep.l1.m16 import value_m16

BASE_04 = 204


def value_m04(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_04 * n + value_m06(n) + value_m16(n)
