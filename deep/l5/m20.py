"""Layer 5 module 20. Generated, seed=20260810."""

from deep.l3.m02 import value_m02
from deep.l3.m21 import value_m21
from deep.l4.m11 import value_m11

BASE_20 = 520


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m02(n) + value_m21(n) + value_m11(n)
