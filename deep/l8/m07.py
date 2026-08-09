"""Layer 8 module 07. Generated, seed=20260810."""

from deep.l7.m17 import value_m17

BASE_07 = 807


def value_m07(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_07 * n + value_m17(n)
