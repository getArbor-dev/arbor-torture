"""Layer 2 module 17. Generated, seed=20260810."""

from deep.l1.m02 import value_m02
from deep.l1.m23 import value_m23

BASE_17 = 217


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m02(n) + value_m23(n)
