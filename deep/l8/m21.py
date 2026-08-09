"""Layer 8 module 21. Generated, seed=20260810."""

from deep.l7.m14 import value_m14

BASE_21 = 821


def value_m21(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_21 * n + value_m14(n)
