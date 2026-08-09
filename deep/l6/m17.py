"""Layer 6 module 17. Generated, seed=20260810."""

from deep.l5.m22 import value_m22

BASE_17 = 617


def value_m17(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_17 * n + value_m22(n)
