"""Layer 9 module 22. Generated, seed=20260810."""

from deep.l8.m06 import value_m06

BASE_22 = 922


def value_m22(n: int = 1) -> int:
    """Sums the layer below, so a change here really does propagate."""
    return BASE_22 * n + value_m06(n)
