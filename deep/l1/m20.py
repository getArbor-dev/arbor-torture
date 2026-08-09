"""Layer 1 module 20. Generated, seed=20260810."""

from deep.l0.m07 import value_m07
from deep.l0.m23 import value_m23

BASE_20 = 120


def value_m20(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_20 * n + value_m07(n) + value_m23(n)
