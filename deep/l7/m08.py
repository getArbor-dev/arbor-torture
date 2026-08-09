"""Layer 7 module 08. Generated, seed=20260810."""

from deep.l5.m00 import value_m00
from deep.l6.m08 import value_m08
from deep.l6.m21 import value_m21

BASE_08 = 708


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m00(n) + value_m08(n) + value_m21(n)
