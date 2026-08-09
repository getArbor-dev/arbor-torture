"""Layer 2 module 11. Generated, seed=20260810."""

from deep.l0.m02 import value_m02
from deep.l1.m11 import value_m11
from deep.l1.m17 import value_m17

BASE_11 = 211


def value_m11(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_11 * n + value_m02(n) + value_m11(n) + value_m17(n)
