"""Layer 7 module 23. Generated, seed=20260810."""

from deep.l4.m02 import value_m02
from deep.l5.m09 import value_m09
from deep.l6.m23 import value_m23

BASE_23 = 723


def value_m23(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_23 * n + value_m02(n) + value_m09(n) + value_m23(n)
