"""Layer 9 module 25. Generated, seed=20260810."""

from deep.l8.m06 import value_m06

BASE_25 = 925


def value_m25(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_25 * n + value_m06(n)
