"""Layer 6 module 16. Generated, seed=20260810."""

from deep.l5.m20 import value_m20

BASE_16 = 616


def value_m16(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_16 * n + value_m20(n)
