"""Layer 1 module 05. Generated, seed=20260810."""

from deep.l0.m00 import value_m00
from deep.l0.m08 import value_m08
from deep.l0.m24 import value_m24

BASE_05 = 105


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m00(n) + value_m08(n) + value_m24(n)
