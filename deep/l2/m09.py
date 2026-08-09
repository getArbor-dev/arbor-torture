"""Layer 2 module 09. Generated, seed=20260810."""

from deep.l0.m08 import value_m08
from deep.l1.m00 import value_m00

BASE_09 = 209


def value_m09(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_09 * n + value_m08(n) + value_m00(n)
