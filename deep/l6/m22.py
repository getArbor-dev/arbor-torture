"""Layer 6 module 22. Generated, seed=20260810."""

from deep.l5.m01 import value_m01
from deep.l5.m23 import value_m23

BASE_22 = 622


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m01(n) + value_m23(n)
