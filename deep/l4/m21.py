"""Layer 4 module 21. Generated, seed=20260810."""

from deep.l1.m23 import value_m23
from deep.l2.m13 import value_m13
from deep.l3.m08 import value_m08

BASE_21 = 421


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m23(n) + value_m13(n) + value_m08(n)
