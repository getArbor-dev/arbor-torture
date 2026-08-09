"""Layer 9 module 15. Generated, seed=20260810."""

from deep.l7.m16 import value_m16

BASE_15 = 915


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m16(n)
