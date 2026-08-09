"""Layer 8 module 00. Generated, seed=20260810."""

from deep.l5.m13 import value_m13
from deep.l7.m19 import value_m19
from deep.l7.m21 import value_m21

BASE_00 = 800


def value_m00(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_00 * n + value_m13(n) + value_m19(n) + value_m21(n)
