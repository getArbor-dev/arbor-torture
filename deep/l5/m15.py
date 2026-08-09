"""Layer 5 module 15. Generated, seed=20260810."""

from deep.l4.m06 import value_m06

BASE_15 = 515


def value_m15(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_15 * n + value_m06(n)
