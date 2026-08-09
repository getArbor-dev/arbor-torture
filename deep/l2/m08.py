"""Layer 2 module 08. Generated, seed=20260810."""

from deep.l0.m25 import value_m25
from deep.l1.m00 import value_m00
from deep.l1.m10 import value_m10

BASE_08 = 208


def value_m08(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_08 * n + value_m25(n) + value_m00(n) + value_m10(n)
