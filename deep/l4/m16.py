"""Layer 4 module 16. Generated, seed=20260810."""

from deep.l1.m21 import value_m21
from deep.l1.m22 import value_m22
from deep.l3.m17 import value_m17

BASE_16 = 416


def value_m16(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_16 * n + value_m21(n) + value_m22(n) + value_m17(n)
