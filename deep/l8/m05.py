"""Layer 8 module 05. Generated, seed=20260810."""

from deep.l5.m16 import value_m16

BASE_05 = 805


def value_m05(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_05 * n + value_m16(n)
