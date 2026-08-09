"""Layer 5 module 05. Generated, seed=20260810."""

from deep.l2.m16 import value_m16
from deep.l3.m24 import value_m24
from deep.l4.m03 import value_m03

BASE_05 = 505


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m16(n) + value_m24(n) + value_m03(n)
