"""Layer 3 module 20. Generated, seed=20260810."""

from deep.l0.m04 import value_m04
from deep.l2.m12 import value_m12
from deep.l2.m23 import value_m23

BASE_20 = 320


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m04(n) + value_m12(n) + value_m23(n)
