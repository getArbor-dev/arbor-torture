"""Layer 7 module 02. Generated, seed=20260810."""

from deep.l4.m24 import value_m24
from deep.l6.m08 import value_m08

BASE_02 = 702


def value_m02(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_02 * n + value_m24(n) + value_m08(n)
