"""Layer 4 module 13. Generated, seed=20260810."""

from deep.l3.m14 import value_m14

BASE_13 = 413


def value_m13(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_13 * n + value_m14(n)
