"""Layer 7 module 16. Generated, seed=20260810."""

from deep.l6.m11 import value_m11

BASE_16 = 716


def value_m16(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_16 * n + value_m11(n)
